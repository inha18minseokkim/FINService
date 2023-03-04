import sqlalchemy.exc
from fastapi import APIRouter, Request
import sys,os
sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
sys.path.append("../..")
from DBClient.databaseCmn import engineConn
from .models import StockDispositionInfo
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.sql import text
from sqlalchemy import Column, Table, TEXT, BIGINT, MetaData, insert, cast, String

stockDispositionRouter = APIRouter(tags=['주요사항보고서:자기주식처분결정'])
conn = engineConn()
#session = conn.sessionmaker()
metadata = MetaData()
tbStockDispositionInfo =  Table('TB_STOCK_DISPOSITION_INFO',metadata,
    Column('rcept_no',BIGINT, nullable=False,primary_key=True,unique=True),
    Column('corp_cls',TEXT, nullable=False),
    Column('corp_code',TEXT, nullable=False),
    Column('corp_name',TEXT, nullable=False),
    Column('dppln_stk_ostk',TEXT, nullable=False),
    Column('dppln_stk_estk',TEXT, nullable=False),
    Column('dpstk_prc_ostk',TEXT, nullable=False) ,
    Column('dpstk_prc_estk',TEXT, nullable=False),
    Column('dppln_prc_ostk',TEXT, nullable=False) ,
    Column('dppln_prc_estk',TEXT, nullable=False),
    Column('dpprpd_bgd',TEXT, nullable=False) ,
    Column('dpprpd_edd',TEXT, nullable=False),
    Column('dp_pp',TEXT, nullable=False),
    Column('dp_m_mkt',TEXT, nullable=False),
    Column('dp_m_ovtm',TEXT, nullable=False),
    Column('dp_m_otc',TEXT, nullable=False),
    Column('dp_m_etc',TEXT, nullable=False),
    Column('cs_iv_bk',TEXT, nullable=False),
    Column('aq_wtn_div_ostk',TEXT, nullable=False),
    Column('aq_wtn_div_ostk_rt',TEXT, nullable=False),
    Column('aq_wtn_div_estk',TEXT, nullable=False),
    Column('aq_wtn_div_estk_rt',TEXT, nullable=False),
    Column('eaq_ostk',TEXT, nullable=False),
    Column('eaq_ostk_rt',TEXT, nullable=False),
    Column('eaq_estk',TEXT, nullable=False),
    Column('eaq_estk_rt',TEXT, nullable=False),
    Column('dp_dd',TEXT, nullable=False),
    Column('od_a_at_t',TEXT, nullable=False),
    Column('od_a_at_b',TEXT, nullable=False),
    Column('adt_a_atn',TEXT, nullable=False),
    Column('d1_slodlm_ostk',TEXT, nullable=False),
    Column('d1_slodlm_estk',TEXT, nullable=False),
    )
tbStockDispositionInfo.create(conn.engine,checkfirst=True)

@stockDispositionRouter.get("/tb_stock_disposition/")
async def paidIncreaseMain():
    return "stockDisposition runs successfully"

@stockDispositionRouter.get("/tb_stock_disposition/selectStockDispositionInfoByDay/{startDate}/{endDate}") #json 리스트로 줌
async def selectStockDispositionInfoByDay(startDate: int,endDate: int):
    session = conn.sessionmaker()
    #rcept_no_str = cast(paidIncreaseInfo.rcept_no, String)
    #resli = session.query(paidIncreaseInfo).filter(rcept_no_str.like(f'{day}%')).all()
    resli = session.query(tbStockDispositionInfo).filter(tbStockDispositionInfo.rcept_no >= startDate, tbStockDispositionInfo.rcept_no <= endDate).all()
    if resli == None or len(resli) == 0: return {'code': 1}
    res = {}
    res['list'] = resli
    res['code'] = 0
    session.close()
    return res

#@stockDispositionRouter.post("/tb_stock_disposition/setStockDispositionInfo")
async def setStockDispositionInfo(json_str: dict):
    session = conn.sessionmaker()
    #json_str = await body.json()
    logger.info(json_str)
    try:
        json_str['rcept_no'] = int(json_str['rcept_no'])
        stmt = insert(tbStockDispositionInfo).values(json_str)
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