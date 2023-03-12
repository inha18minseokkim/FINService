import sys
sys.path.append("..")
#from apartment.competitionRateInquireDB import saveDB,createTable
from loguru import logger
from .dbModel import aptCompetitionRate
from declaration import dataPortalKey, sendDiscordMessage

import requests
#아파트 분양정보/경쟁률 조회
requestUrl = "http://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getAPTLttotPblancCmpet"
def executeApi(houseManageNo: str,pageNum : int)-> list: #curDate는 YYYY-MM-dd 형식
    logger.debug(dataPortalKey)
    header = {"Authorization" : f"Infuser {dataPortalKey}"}
    param = {"page" : "1", "perPage" : pageNum, "returnType" : "JSON" ,
             "cond[HOUSE_MANAGE_NO::EQ]" : houseManageNo
             }
    res = requests.get(url=requestUrl,params=param,headers=header)
    logger.debug(res.json())
    if res.status_code != 200:
        logger.debug("오류 발생")
        raise Exception
    res = res.json()
    #logger.debug(res)
    reslist = []
    for ele in res['data']:
        reslist.append(aptCompetitionRate(ele))
    return reslist

# def executeMsg(tb):
#     tmpMsg = tb.getMsg()
#     logger.debug(tmpMsg)
#     sendDiscordMessage(tmpMsg)


if __name__ == "__main__":
    tmplist = executeApi(2022000261,10)
    logger.debug(tmplist)
    #createTable()
    #for ele in tmplist:
    #    executeMsg(ele)
    #    saveDB(ele)
