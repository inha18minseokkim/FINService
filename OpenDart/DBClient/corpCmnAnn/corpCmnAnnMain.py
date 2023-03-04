import sqlalchemy
from fastapi import APIRouter, Request
import sys,os

from sqlalchemy import Table, MetaData, BIGINT, Column, TEXT, UniqueConstraint, insert
from sqlalchemy.engine import CursorResult

sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from DBClient.databaseCmn import engineConn
from .models import corpCmnAnn
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.sql import text
corpCmnAnnRouter = APIRouter(tags=['일반공시'])
conn = engineConn()
#session = conn.sessionmaker()
metadata = MetaData()
tbCorpCmnAnn = Table('TB_CORP_CMN_ANN',metadata,
    Column('rcept_no',BIGINT,nullable=False,unique=True,primary_key=True),
    Column('corp_name',TEXT, nullable=False),
    Column('corp_code',TEXT, nullable=False),
    Column('report_nm',TEXT, nullable=False),
    Column('rcept_dt',TEXT, nullable=False)
    )
tbCorpCmnAnn.create(conn.engine,checkfirst=True)

@corpCmnAnnRouter.get("/tb_corp_cmn_ann/")
async def codeInfoMain():
    return "CommonAnnouncement runs successfully"

def insertCorpCmnAnn(json_str: dict):
    session = conn.sessionmaker()
    #json_str = await body.json()
    try:
        logger.debug(f"삽입 시도{body}")
        json_str['rcept_no'] = int(json_str['rcept_no'])
        stmt = insert(tbCorpCmnAnn).values(json_str)
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
# 얘는 FEP에 가야함
# @corpCmnAnnRouter.post("/tb_corp_cmn_ann/selectAnnInfoByRceptNo/{rceptNo}")
# async def selectAnnInfoByRceptNo(rceptNo: str):
#     try:
#         exec = conn.engine.connect()
#         stmt = text(
#             f"select rcpet_no,corp_name,report_nm,rcept_dt from TB_CORP_CMN_ANN where rcept_no = '{rceptNo}'")
#         res: CursorResult = exec.execute(stmt)
#     except:
#         return {'code': 1}
#     res = tuple(res.first())
#
#     try:
#         logger.debug(f"튜플 변환 완료 {res[0]} {res[1]} {res[2]} {res[3]}")
#         return {'code' : 0, 'rcept_no' : res[0], 'corp_name' : res[1], 'report_nm' : res[2], 'rcept_dt' : res[3]}
#     except:
#         logger.debug("변환 실패")
#         return {'code' : 1, 'rcept_no' : "", 'corp_name' : "", 'report_nm' : "", 'rcept_dt' : ""}