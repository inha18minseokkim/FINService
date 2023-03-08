import sys
sys.path.append("..")
from apartment.competitionRateInquireDB import saveDB,createTable
from loguru import logger
from declaration import dataPortalKey, sendDiscordMessage
from subscriptionInfoInquireSvcModel import TB_SUBSCRIPTION_INFO_INQUIRE, infoDict
import requests
#아파트 분양정보/경쟁률 조회
requestUrl = "http://api.odcloud.kr/api/ApplyhomeInfoCmpetRtSvc/v1/getAPTLttotPblancCmpet"
def executeApi(pageNum: int,startDate: str, endDate: str)-> list: #curDate는 YYYY-MM-dd 형식
    logger.debug(dataPortalKey)
    header = {"Authorization" : f"Infuser {dataPortalKey}"}
    param = {"page" : "1", "perPage" : pageNum, "returnType" : "JSON" ,
             "cond[RCRIT_PBLANC_DE::GTE]" : startDate,
             "cond[RCRIT_PBLANC_DE::LTE]" : endDate
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
        reslist.append(TB_SUBSCRIPTION_INFO_INQUIRE(ele))
        #logger.debug(reslist[-1].to_dict())
    #print(reslist)
    return reslist

def executeMsg(tb: TB_SUBSCRIPTION_INFO_INQUIRE):
    tmpMsg = tb.getMsg()
    logger.debug(tmpMsg)
    sendDiscordMessage(tmpMsg)


if __name__ == "__main__":
    tmplist = executeApi(1000,"2023-01-01","2023-03-08")
    createTable()
    for ele in tmplist:
        executeMsg(ele)
        saveDB(ele)
