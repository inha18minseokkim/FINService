from fastapi import FastAPI 
from scheduler import app as app_rocketry
from loguru import logger
import asyncio
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