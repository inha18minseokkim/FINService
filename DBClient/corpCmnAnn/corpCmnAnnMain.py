import sqlalchemy
from fastapi import APIRouter, Request
import sys,os

from sqlalchemy import Table, MetaData, BIGINT, Column, TEXT, UniqueConstraint, insert
from sqlalchemy.engine import CursorResult

sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn
from corpCmnAnn.models import corpCmnAnn
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.sql import text
corpCmnAnnRouter = APIRouter()
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

@corpCmnAnnRouter.post("/tb_corp_cmn_ann/insertCorpCmnAnn")
async def insertCorpCmnAnn(body: Request):
    session = conn.sessionmaker()
    json_str = await body.json()
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