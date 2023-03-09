import sys
sys.path.append("..")
from loguru import logger
from declaration import dataPortalKey, sendDiscordMessage
from common.dbModel import subscriptionInfo
import requests
#한국부동산원 청약홈 분양정보 조회 서비스 오피스텔
requestUrl = "http://api.odcloud.kr/api/ApplyhomeInfoDetailSvc/v1/getUrbtyOfctlLttotPblancDetail"
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
        reslist.append(subscriptionInfo(ele))
        #logger.debug(reslist[-1].to_dict())
    #print(reslist)
    return reslist

def executeMsg(tb: subscriptionInfo):
    tmpMsg = tb.getMsg()
    logger.debug(tmpMsg)
    sendDiscordMessage(tmpMsg)


if __name__ == "__main__":
    logger.debug("OK")
    tmplist = executeApi(10,"2022-01-01","2022-09-01")

    #createTable()
    #for ele in tmplist:
    #    executeMsg(ele)
    #    saveDB(ele)
