from fastapi import APIRouter

from common.dbModel import subscriptionInfo
from declaration import sendDiscordMessage
from common.dbClient import selectDataByDate, saveDB, selectDataByHouseManageNm
from apartment.svcMain import executeApi
apartmentRouter = APIRouter(tags=["청약서비스"])


@apartmentRouter.get("/getSubscriptionInfoByDay/")
async def getSubscriptionInfoByDay(startDate: str, endDate: str):
    res = selectDataByDate(startDate,endDate)
    resarr = []
    for i in res:
        resarr.append(i.to_dict())
    return resarr
@apartmentRouter.get("/getSubscriptionInfoByHouseManageNm")
async def getSubscriptionInfoByHouseManageNm(houseManageNm: str):
    res = selectDataByHouseManageNm(houseManageNm)
    return res.to_dict()
@apartmentRouter.get("/pushSubscriptionInfoByDay/")
async def pushSubscriptionInfoByDay(startDate: str, endDate: str):
    res = selectDataByDate(startDate,endDate)
    for i in res:
        sendDiscordMessage(i.getMsg())
    return {'code' : 0}


#리스트 받아서 DB에 적재
@apartmentRouter.get("/dailyGetApartmentData")
async def dailyGetApartmentData(pageNum: int, startDt: str,endDt : str = ""):
    if len(endDt) == 0: endDt = startDt
    resli: list[subscriptionInfo] = executeApi(pageNum,startDt,endDt)
    for i in resli:
        saveDB(i)
    return {'code' : 0, 'startDt' : startDt, 'endDt': endDt}


