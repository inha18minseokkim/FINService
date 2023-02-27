import json

import requests
from loguru import logger
import re
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from FastApiCore.declaration import dbUrl, sendDiscordMessage
from paidIncreaseSvc import PaidIncreaseIntf
from stockDispositionSvc import StockDispositionIntf
class CmnEventPushSvcIntf:
    def pushMessage(self,msgInfo: dict):
        corpName = msgInfo['corp_name']
        reportNm = msgInfo['report_nm']
        rceptDt = msgInfo['rcept_dt']
        msg = f"이벤트 발생 \n 회사명 : {corpName} \n 이벤트 : {reportNm} \n 발생일 : {rceptDt} "
        logger.debug(msg)
        # 여기에 푸시 보내는 기능 적재예정
        res = sendDiscordMessage(msg)
        logger.debug("메세지 보냄 " + json.dumps(res))

def eventHandle(dict):
    corpName = dict['corpName']
    rceptDt = dict['rceptDt']
    reportNm = dict['reportNm']
    corpCode = dict['corpCode']

    if re.search('.*유상증자.*', reportNm):
        logger.debug(f'{corpName} {reportNm} {rceptDt} 유상증자 결정')
        PaidIncreaseIntf().pushMessage(dict)
    elif re.search('.*자기주식처분.*', reportNm):
        logger.debug(f'{corpName} {rceptDt} 자기주식처분 결정')
        StockDispositionIntf().pushMessage(dict)
    else:
        logger.debug(f'{corpName} {rceptDt} 기타 사항')
        CmnEventPushSvcIntf().pushMessage(dict)