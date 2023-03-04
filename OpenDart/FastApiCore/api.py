from fastapi import FastAPI, APIRouter
import requests

from .scheduler import app as app_rocketry
from loguru import logger
import sys
import asyncio
sys.path.append('../..') #부모 디렉터리 강제로 import 안하면 안됨 왜??????
sys.path.append("..")
from .batRes import dailyCBRoutine, dailyCodeRoutine, initCodeRoutine, dailyPaidIncreaseRoutine
from .mainSvc import openDartAnnouncementSvc
from .declaration import dbUrl

coreRouter = APIRouter()
session = app_rocketry.session
#배치 조회용 fastapi서버. 온라인은 다른곳에 기술하자.
@coreRouter.get("/")
def helloWorld():
    return {"Hello" : "World"}

@coreRouter.on_event("startup")
def onStartUp():
    logger.debug("start")
    
@coreRouter.get("/tasks")
async def read_tasks():
    return list(session.tasks)

@coreRouter.get("/passiveRoutine/dailyBWRoutine")
async def execDailyBWRoutine():
    return "Not Prepared"
@coreRouter.get("/passiveRoutine/dailyCBRoutine")
async def execDailyCBRoutine():
    asyncio.run(await dailyCBRoutine.getCBEvent())
    return "Finished"
@coreRouter.get("/passiveRoutine/dailyCodeRoutine")
async def execDailyCodeRoutine():
    asyncio.run(await dailyCodeRoutine.updateCode())
    return "Finished"
@coreRouter.get("/passiveRoutine/initCodeRoutine")
async def execInitCodeRoutine():
    await initCodeRoutine.initCode()
    return "Finished"
@coreRouter.get("/passiveRoutine/dailyPaidIncreaseRoutine")
async def execPaidIncreaseRoutine():
    asyncio.run(await dailyPaidIncreaseRoutine.getPaidIncreaseEvent())
    return "Finished"

@coreRouter.get("/getAnnounceInfo/{corpCode}/{bgnDe}/{endDe}/{pblntfTy}")
async def getAnnounceInfo(corpCode: str,bgnDe: str,endDe: str, pblntfTy: str):
    logger.debug(f"{corpCode} {bgnDe} {endDe} {pblntfTy}")
    res = openDartAnnouncementSvc.getAnnounceInfo(corpCode, bgnDe, endDe, pblntfTy)
    if res is None: return {'list' : []}
    return res

