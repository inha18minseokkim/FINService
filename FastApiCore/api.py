from fastapi import FastAPI
from scheduler import app as app_rocketry
from loguru import logger
import sys
import asyncio
sys.path.append('/..') #부모 디렉터리 강제로 import 안하면 안됨 왜??????
from batRes import dailyCBRoutine, dailyCodeRoutine, initCodeRoutine, dailyPaidIncreaseRoutine

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
    asyncio.run(await initCodeRoutine.initCode())
    return "Finished"
@app.get("/passiveRoutine/dailyPaidIncreaseRoutine")
async def execPaidIncreaseRoutine():
    asyncio.run(await dailyPaidIncreaseRoutine.getPaidIncreaseEvent())
    return "Finished"