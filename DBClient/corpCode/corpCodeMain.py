from fastapi import APIRouter, Request
import sys,os

from sqlalchemy import Table, MetaData, BIGINT, Column, TEXT, UniqueConstraint

sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn
from corpCode.models import corpInfo
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.sql import text
corpCodeRouter = APIRouter()
conn = engineConn()
#session = conn.sessionmaker()
metadata = MetaData()
tbCorpCode = Table('TB_CORP_CODE',metadata,
    Column('IDX',BIGINT,nullable=False,autoincrement=True,primary_key=True),
    Column('corp_code',TEXT(length=8), nullable=False),
    Column('corp_name',TEXT, nullable=False),
    Column('stock_code',TEXT, nullable=False),
    Column('modify_date',TEXT, nullable=False),
    )
tbCorpCode.create(conn.engine,checkfirst=True)

@corpCodeRouter.get("/tb_corp_code/")
async def codeInfoMain():
    return "codeInfo runs successfully"

@corpCodeRouter.get("/tb_corp_code/selectCorpInfoFixed")
async def selectCorpInfoFixed():
    if not hasattr(selectCorpInfoFixed, "counter"):
        selectCorpInfoFixed.startIdx = 0
    endIdx = selectCorpInfoFixed.startIdx + 510

    logger.debug(f"{selectCorpInfoFixed.startIdx} {endIdx}")
    if selectCorpInfoFixed.startIdx > 3545:
        selectCorpInfoFixed.startIdx = 0
    try:
        exec = conn.engine.connect()
        stmt = text(f"select idx,corp_code,corp_name,stock_code from TB_CORP_CODE where idx >= {selectCorpInfoFixed.startIdx} and idx <= {endIdx}")
        res = exec.execute(stmt)
        selectCorpInfoFixed.startIdx += 510
    except:
        return {'code' : 1}
    li = []
    for i in res:
        dict = {}
        dict['idx'] = i[0]
        dict['corp_code'] = i[1]
        dict['corp_name'] = i[2]
        dict['stock_code'] = i[3]
        li.append(dict)
    return {'list': li, 'code' : 0}
@corpCodeRouter.get("/tb_corp_code/selectCorpInfo/{corp_code}")
async def selectCorpInfo(corp_code: str):
    session = conn.sessionmaker()
    res = session.query(corpInfo).filter(corpInfo.corp_code == corp_code).first()
    if res == None: return {'code' : 1}
    session.close()
    return res

@corpCodeRouter.get("/tb_corp_code/selectCorpInfoByRange/{startIdx}/{endIdx}")
async def selectCorpInfoByRange(startIdx: int, endIdx: int):
    logger.debug(f"{startIdx} {endIdx}")
    try:
        exec = conn.engine.connect()
        stmt = text(f"select idx,corp_code,corp_name,stock_code from TB_CORP_CODE where idx >= {startIdx} and idx <= {endIdx}")
        res = exec.execute(stmt)
    except:
        return {'code' : 1}
    li = []
    for i in res:
        dict = {}
        dict['idx'] = i[0]
        dict['corp_code'] = i[1]
        dict['corp_name'] = i[2]
        dict['stock_code'] = i[3]
        li.append(dict)
    return {'res': li, 'code' : 0}


class RequestBody(BaseModel):
    corp_code: int
    corp_name: str
    stock_code: str
    modify_date: str

@corpCodeRouter.post("/tb_corp_code/insertCorpInfo")
async def insertCorpInfo(body: RequestBody):
    session = conn.sessionmaker()
    res = corpInfo()
    print(body.corp_code)
    res.corp_code = body.corp_code
    res.corp_name = body.corp_name
    res.stock_code = body.stock_code
    res.modify_date = body.modify_date
    try:
        session.add(res)
        session.commit()
    except:
        session.rollback()
        session.close()
        return {"code": 1}
    return {"code" : 0}

@corpCodeRouter.post("/tb_corp_code/updateCorpInfo")
async def updateCorpInfo(body: RequestBody):
    res = session.query(corpInfo).filter(corpInfo.corp_code == body.corp_code)
    res.update({'corp_name' : body.corp_name})
    res.update( {'stock_code' : body.stock_code})
    res.update({'modify_date' : body.modify_date})
    logger.debug("수정중")
    try:
        session.commit()
        logger.debug("수정완료")
    except:
        session.rollback()
        return {"code" : 1}
    return {"code" : 0}

@corpCodeRouter.post("/tb_corp_code/insertOrUpdateCorpInfoArr")
async def insertOrUpdateCorpInfoArr(body: Request): # body안에는 "list" : [{}{}{}] 각각 code에 대한 json 리스트.
    logger.debug(body)
    dict = await body.json()
    for ele in dict['list']:
        tmpCorpInfo = corpInfo()
        tmpCorpInfo.corp_code = ele['corp_code']
        tmpCorpInfo.corp_name = ele['corp_name']
        tmpCorpInfo.stock_code = ele['stock_code']
        tmpCorpInfo.modify_date = ele['modify_date']
        session.merge(tmpCorpInfo)
    session.commit()
    return {'code' : 0}

