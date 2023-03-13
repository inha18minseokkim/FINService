from fastapi import APIRouter
from apartment import dbClient,mainSvc,dbModel
from loguru import logger
import requests

apartmentRouter = APIRouter(tags=["아파트"])

@apartmentRouter.get("/dailyApartmentData")
async def dailyApartmentData(startDate: str, endDate: str):
    rqstUrl = f"http://realestate-service.default.svc.cluster.local:8083/getHouseManageNmByDay?startDate={startDate}&endDate={endDate}"
    res = requests.get(rqstUrl)
    if res.status_code != 200:
        return {'code' : 1}
    res = res.json()
    logger.debug(res)
    portalUrl = "https://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getAPTLttotPblancCmpet?page=1&perPage=1000"
    dbClient.createTable()
    for num in res['list']:
        competition:list[dbModel.aptCompetitionRate] = mainSvc.executeApi(num, 1000)
        for ele in competition:
            logger.debug(ele.to_dict())
            dbClient.saveDB(ele)

    return res
@apartmentRouter.get("/getApartmentCmpByHouseManageNm")
async def getApartmentCmpByHouseManageNm(houseManageNm: str):
    res:list[dbModel.aptCompetitionRate] = dbClient.selectDataByHouseManageNm(houseManageNm)
    resarr = []
    for ele in res:
        resarr.append(ele.to_dict())
    return {"list": resarr}


