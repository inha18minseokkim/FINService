import json
from loguru import logger
import sys
sys.path.append("../..") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
sys.path.append("../")
from DBClient.corpCmnAnn import corpCmnAnnMain
from FastApiCore.declaration import dbUrl, sendDiscordMessage

class CmnEventPushSvcIntf:
    def pushMessage(self,msgInfo: dict):
        logger.debug(msgInfo)
        corpName = msgInfo['corp_name']
        reportNm = msgInfo['report_nm']
        rceptDt = msgInfo['rcept_dt']
        rceptNo = msgInfo['rcept_no']
        msg = f"이벤트 발생 \n 회사명 : {corpName} \n 이벤트 : {reportNm} \n 발생일 : {rceptDt} \n접수번호 : {rceptNo}"
        logger.debug(msg)
        # 여기에 푸시 보내는 기능 적재예정
        res = sendDiscordMessage(msg)
        logger.debug("메세지 보냄 " + json.dumps(res))
        self.saveDB(msgInfo)
    def saveDB(self,msgInfo: dict):
        logger.debug(msgInfo)
        #res = requests.post(dbUrl + "/tb_corp_cmn_ann/insertCorpCmnAnn",json=msgInfo)
        res = corpCmnAnnMain.insertCorpCmnAnn(msgInfo)
        logger.debug(res)


