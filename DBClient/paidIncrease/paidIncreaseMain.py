import sqlalchemy.exc
from fastapi import APIRouter, Request
import sys,os
sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn
from paidIncrease.models import paidIncreaseInfo
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.sql import text
from sqlalchemy import Column, Table, TEXT, BIGINT, MetaData, insert, cast, String

paidIncreaseRouter = APIRouter()
conn = engineConn()
#session = conn.sessionmaker()
metadata = MetaData()
tbPaidIncreaseInfo =  Table('TB_PAID_INCREASE_INFO',metadata,
    Column('rcept_no',BIGINT, nullable=False,primary_key=True,unique=True),
    Column('corp_cls',TEXT, nullable=False),
    Column('corp_code',TEXT, nullable=False),
    Column('corp_name',TEXT, nullable=False),
    Column('nstk_ostk_cnt',TEXT, nullable=False),
    Column('nstk_estk_cnt',TEXT, nullable=False),
    Column('fv_ps',TEXT, nullable=False) ,
    Column('bfic_tisstk_ostk',TEXT, nullable=False),
    Column('bfic_tisstk_estk',TEXT, nullable=False) ,
    Column('fdpp_fclt',TEXT, nullable=False),
    Column('fdpp_bsninh',TEXT, nullable=False) ,
    Column('fdpp_op',TEXT, nullable=False),
    Column('fdpp_dtrp',TEXT, nullable=False),
    Column('fdpp_ocsa',TEXT, nullable=False),
    Column('fdpp_etc',TEXT, nullable=False),
    Column('ic_mthn',TEXT, nullable=False),
    Column('ssl_at',TEXT, nullable=False),
    Column('ssl_bgd',TEXT, nullable=False),
    Column('ssl_edd',TEXT, nullable=False))
tbPaidIncreaseInfo.create(conn.engine,checkfirst=True)

@paidIncreaseRouter.get("/tb_paid_increase/")
async def paidIncreaseMain():
    return "paidIncrease runs successfully"

@paidIncreaseRouter.get("/tb_paid_increase/selectCorpInfoByDay/{startDate}/{endDate}") #json 리스트로 줌
async def selectCorpInfo(startDate: int,endDate: int):
    session = conn.sessionmaker()
    #rcept_no_str = cast(paidIncreaseInfo.rcept_no, String)
    #resli = session.query(paidIncreaseInfo).filter(rcept_no_str.like(f'{day}%')).all()
    resli = session.query(paidIncreaseInfo).filter(paidIncreaseInfo.rcept_no >= startDate, paidIncreaseInfo.rcept_no <= endDate).all()
    if resli == None or len(resli) == 0: return {'code': 1}
    res = {}
    res['list'] = resli
    res['code'] = 0
    session.close()
    return res

@paidIncreaseRouter.post("/tb_paid_increase/setCorpInfo")
async def setCorpInfo(body: Request):
    session = conn.sessionmaker()
    json_str = await body.json()
    logger.info(json_str)
    try:
        json_str['rcept_no'] = int(json_str['rcept_no'])
        stmt = insert(tbPaidIncreaseInfo).values(json_str)
        session.execute(stmt)
        session.commit()
        logger.debug("삽입완료")
    except sqlalchemy.exc.IntegrityError as e:
        logger.debug("삽입 중 오류, 이미 들어가있음 {e}", e=e, exc_info=True)
        session.rollback()
    except Exception as e:
        logger.debug("삽입 중 오류 {e}",e=e,exc_info=True)
        session.rollback()
    session.close()
    return {'code': 0}