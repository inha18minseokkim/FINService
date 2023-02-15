from fastApi import APIRouter
import sys,os
sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn
from corpCode.models import corpInfo
from pydantic import BaseModel
from loguru import logger
cbRouter = APIRouter()
conn = engineConn()
session = conn.sessionmaker()

@cbRouter.get("/tb_cb_info/getCurCBInfo/{curDate}")
async def selectCBInfo(curDate: str):
    res = session.query(corpInfo).filter(corpInfo.corp_code == corp_code).first()
    if res == None: return {'code' : 1}
    return res

