from fastapi import APIRouter
import sys,os
sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn
from corpCode.models import corpInfo
from pydantic import BaseModel
from loguru import logger
from sqlalchemy.sql import text
corpCodeRouter = APIRouter()
conn = engineConn()
session = conn.sessionmaker()
@corpCodeRouter.get("/tb_corp_code/")
async def codeInfoMain():
    return "codeInfo runs successfully"

@corpCodeRouter.get("/tb_corp_code/selectCorpInfo/{corp_code}")
async def selectCorpInfo(corp_code: str):
    res = session.query(corpInfo).filter(corpInfo.corp_code == corp_code).first()
    if res == None: return {'code' : 1}
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
