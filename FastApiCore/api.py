from fastapi import FastAPI
import requests

from scheduler import app as app_rocketry
from loguru import logger
import sys
import asyncio
sys.path.append('/..') #부모 디렉터리 강제로 import 안하면 안됨 왜??????
from batRes import dailyCBRoutine, dailyCodeRoutine, initCodeRoutine, dailyPaidIncreaseRoutine
from mainSvc import openDartAnnouncementSvc
from declaration import dbUrl

app = FastAPI()
session = app_rocketry.session
#배치 조회용 fastapi서버. 온라인은 다른곳에 기술하자.
@app.get("/")
def helloWorld():
    return {"Hello" : "World"}

@app.on_event("startup")
def onStartUp():
    logger.debug("start")
    
@app.get("/tasks")
async def read_tasks():
    return list(session.tasks)

@app.get("/passiveRoutine/dailyBWRoutine")
async def execDailyBWRoutine():
    return "Not Prepared"
@app.get("/passiveRoutine/dailyCBRoutine")
async def execDailyCBRoutine():
    asyncio.run(await dailyCBRoutine.getCBEvent())
    return "Finished"
@app.get("/passiveRoutine/dailyCodeRoutine")
async def execDailyCodeRoutine():
    asyncio.run(await dailyCodeRoutine.updateCode())
    return "Finished"
@app.get("/passiveRoutine/initCodeRoutine")
async def execInitCodeRoutine():
    await initCodeRoutine.initCode()
    return "Finished"
@app.get("/passiveRoutine/dailyPaidIncreaseRoutine")
async def execPaidIncreaseRoutine():
    asyncio.run(await dailyPaidIncreaseRoutine.getPaidIncreaseEvent())
    return "Finished"

@app.get("/getAnnounceInfo/{corpCode}/{bgnDe}/{endDe}/{pblntfTy}")
async def getAnnounceInfo(corpCode: str,bgnDe: str,endDe: str, pblntfTy: str):
    logger.debug(f"{corpCode} {bgnDe} {endDe} {pblntfTy}")
    res = openDartAnnouncementSvc.getAnnounceInfo(corpCode, bgnDe, endDe, pblntfTy)
    if res is None: return {'list' : []}
    return res
@app.get("/getCorpCodeByName/{corpName}")
async def getCorpCodeByName(corpName: str):
    logger.debug(f"{corpName} 찾기 시작")
    res = requests.get(dbUrl + f"/tb_corp_code/getCorpCodeByName/{corpName}")
    logger.debug(res.json())
    logger.debug(res.status_code)
    if res.status_code == 200:
        return res.json()['corp_code']
    else:
        return ""

@app.get("/getStockCodeByName/{corpName}")
async def getStockCodeByName(corpName: str):
    logger.debug(f"{corpName} 찾기 시작")
    res = requests.get(dbUrl + f"/tb_corp_code/getCorpStockCodeByName/{corpName}")
    logger.debug(res.json())
    logger.debug(res.status_code)
    if res.status_code == 200:
        return res.json()['stock_code']
    else:
        return ""