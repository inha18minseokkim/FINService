from fastapi import APIRouter
import sys
sys.path.append("..")
from common.dbModel import subscriptionInfo
from declaration import sendDiscordMessage
from common.dbClient import selectDataByDate, saveDB, selectDataByHouseManageNm
from .svcMain import executeApi

studioRouter = APIRouter(tags=["오피스텔/도시형/민간임대"])

#리스트 받아서 DB에 적재
@studioRouter.get("/dailyGetStudioData")
async def dailyGetStudioData(pageNum: int, startDt: str,endDt : str = ""):
    if len(endDt) == 0: endDt = startDt
    resli: list[subscriptionInfo] = executeApi(pageNum,startDt,endDt)
    for i in resli:
        saveDB(i)
    return {'code' : 0, 'startDt' : startDt, 'endDt': endDt}