from fastapi import APIRouter
import sys
sys.path.append("..")
from RealEstateSubscription.common.dbModel import subscriptionInfo
from RealEstateSubscription.declaration import sendDiscordMessage
from RealEstateSubscription.common.dbClient import selectDataByDate, saveDB, selectDataByHouseManageNm
from .svcMain import executeApi

residRouter = APIRouter(tags=["무순위/잔여세대"])

#리스트 받아서 DB에 적재
@residRouter.get("/dailyResidData")
async def dailyResidData(pageNum: int, startDt: str,endDt : str = ""):
    if len(endDt) == 0: endDt = startDt
    resli: list[subscriptionInfo] = executeApi(pageNum,startDt,endDt)
    for i in resli:
        saveDB(i)
    return {'code' : 0, 'startDt' : startDt, 'endDt': endDt}

