from fastapi import FastAPI
from loguru import logger

import apartment.dbClient
import apartment.dbModel
from apartment.mainSvc import executeApi

import requests

import declaration

app = FastAPI()


@app.get("/")
async def test():
    return "RealEstateSubscription 정상 작동중"

@app.get("/dailyApartmentData")
async def dailyApartmentData(startDate: str, endDate: str):
    rqstUrl = f"http://172.28.166.206:32221/getHouseManageNmByDay?startDate={startDate}&endDate={endDate}"
    res = requests.get(rqstUrl)
    if res.status_code != 200:
        return {'code' : 1}
    res = res.json()
    logger.debug(res)
    portalUrl = "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getAPTLttotPblancCmpet?page=1&perPage=1000"
    apartment.dbClient.createTable()
    for num in res['list']:
        competition:list[apartment.dbModel.aptCompetitionRate] = executeApi(num, 1000)
        for ele in competition:
            logger.debug(ele.to_dict())
            apartment.dbClient.saveDB(ele)

    return res
@app.get("/getApartmentCmpByHouseManageNm")
async def getApartmentCmpByHouseManageNm(houseManageNm: str):
    res:list[apartment.dbModel.aptCompetitionRate] = apartment.dbClient.selectDataByHouseManageNm(houseManageNm)
    resarr = []
    for ele in res:
        resarr.append(ele.to_dict())
    return {"list": resarr}


