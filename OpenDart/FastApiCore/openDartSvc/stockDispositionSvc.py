import json
import sys,os
sys.path.append("../..") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
sys.path.append("..")
from FastApiCore.declaration import crtfc_key, dbUrl, sendDiscordMessage
from .eventPushSvcIntf import CmnEventPushSvcIntf
from DBClient import stockDisposition
'''
사용 파라미터 : 회사코드, 날짜
주요 내용 조립해서 푸시 서버에 보내줌
서버에서 한번 보내줌
'''
#자기주식 처분 결정
import requests
from loguru import logger
class StockDispositionIntf(CmnEventPushSvcIntf):
    def __init__(self):
        self.requestUrl = "https://opendart.fss.or.kr/api/piicDecsn.json"  # 자기주식 처분결정 api url
    def pushMessage(self,msgInfo: dict):
        corpName = msgInfo['corp_name']
        rceptDt = msgInfo['rcept_dt']
        reportNm = msgInfo['report_nm']
        corpCode = msgInfo['corp_code']
        logger.debug(f"{corpName} {reportNm} {rceptDt} {corpCode}")
        param = {"crtfc_key" : crtfc_key, "corp_code" : corpCode, "bgn_de" : rceptDt, "end_de" : rceptDt}
        res = requests.get(self.requestUrl,params=param).json()
        logger.debug(res)
        if res['status'] == '013':
            logger.debug("아무 이벤트 없음")
            super().pushMessage(msgInfo)
            return
        if res['status'] != '000':
            logger.debug("오류 발생")
        #리스트는 여러  element가 있을 수 있음.
        #유상증자와 마찬가지로 기재정정이라고 생각
        res = res['list'][0]
        #해당 데이터 db에 저장
        self.saveDB(res)
        #requests.post(dbUrl + "/tb_paid_increase/setCorpInfo",json=res)
        msg = f"자기주식처분 결정 \n회사명 : {res['corp_name']} \n발행주식 수 : {res['nstk_ostk_cnt']} \n주당액면가 : {res['fv_ps']}" \
              f"\n증자방식 : {res['ic_mthn']} \n접수번호 : {res['rcept_no']}"
        logger.debug(msg)
        #여기에 푸시 보내는 기능 적재예정
        res = sendDiscordMessage(msg)
        logger.debug("메세지 보냄 " + json.dumps(res))
    def saveDB(self,msgInfo: dict):
        #res = requests.post(dbUrl + "/tb_stock_disposition/insertDispositionInfo", json=msgInfo)
        res = stockDisposition.setStockDispositionInfo(msgInfo)
        logger.debug(res)

