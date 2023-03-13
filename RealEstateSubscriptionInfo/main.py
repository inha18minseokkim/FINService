from fastapi import FastAPI
from apartment.api import apartmentRouter
from studio.api import studioRouter
from residual.api import residRouter
from common.dbClient import selectDataByHouseManageNm, selectDataByDate
from declaration import sendDiscordMessage

app = FastAPI()
app.include_router(apartmentRouter)
app.include_router(studioRouter)
app.include_router(residRouter)

@app.get("/")
async def test():
    return "RealEstateSubscriptionInfo 정상 작동중"

@app.get("/getSubscriptionInfoByDay")
async def getSubscriptionInfoByDay(startDate: str, endDate: str):
    res = selectDataByDate(startDate,endDate)
    resarr = []
    for i in res:
        resarr.append(i.to_dict())
    return {"list" : resarr}

@app.get("/getHouseManageNmByDay")
async def getHouseManageNmByDay(startDate: str,endDate: str):
    res = selectDataByDate(startDate,endDate)
    resarr = []
    for i in res:
        resarr.append(i.HOUSE_MANAGE_NO)
    return {"list" : resarr}

@app.get("/getSubscriptionInfoByHouseManageNm")
async def getSubscriptionInfoByHouseManageNm(houseManageNm: str):
    res = selectDataByHouseManageNm(houseManageNm)
    return res.to_dict()

@app.get("/pushSubscriptionInfoByDay")
async def pushSubscriptionInfoByDay(startDate: str, endDate: str):
    res = selectDataByDate(startDate,endDate)
    for i in res:
        sendDiscordMessage(i.getMsg())
    return {'code' : 0}