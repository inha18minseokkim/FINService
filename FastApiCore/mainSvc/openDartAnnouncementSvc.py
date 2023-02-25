import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from declaration import crtfc_key,dbUrl
import requests
import json
from datetime import datetime, timedelta
from loguru import logger
import re
from Svc.paidIncreaseSvc import pushPaidIncreaseInfo

url = "https://opendart.fss.or.kr/api/list.json"

def mainRoutine(corpCodeList: list, date: str, pblntf_ty: str):
    logger.debug("openDartAnnRoutine : 공시검색 시작")
    for ele in corpCodeList:
        logger.debug(ele)
        logger.debug(f"{ele['corp_code']}, {date}, {date}, {pblntf_ty}")
        getAnnounceInfo(ele['corp_code'], date, date, pblntf_ty)
        logger.debug("완료")

def eventHandle(dict):
    corpName = dict['corpName']
    rceptDt = dict['rceptDt']
    reportNm = dict['reportNm']
    corpCode = dict['corpCode']
    if re.search('.*유상증자.*', reportNm):
        logger.debug(f'{corpName} {reportNm} {rceptDt} 유상증자 결정')
        pushPaidIncreaseInfo(dict)
    if re.search('.*자기주식처분.*', reportNm):
        logger.debug(f'{corpName} {rceptDt} 자기주식처분 결정')


def getAnnounceInfo(corp_code: str, bgn_de: str, end_de: str, pblntf_ty: str):
    logger.debug("ASDF")
    logger.debug(f"{corp_code} {bgn_de} {end_de} {pblntf_ty}")
    param = {
        'crtfc_key' : crtfc_key,
        'corp_code' : corp_code,
        'bgn_de': bgn_de,
        'end_de' : end_de,
        'pblntf_ty' : pblntf_ty
    }
    logger.debug(param)
    res = requests.get(url,params=param).json()
    #logger.debug(res)
    logger.debug(res)
    if res['status'] == '000':
        logger.debug("정상응답")
    if res['status'] == '013':
        logger.debug("아무것도 없음")
        return
    msg = []
    for i in res['list']:
        corpName = i['corp_name']
        reportNm = i['report_nm']
        rceptDt = i['rcept_dt']
        logger.debug(f"{corpName} {reportNm} {rceptDt}")
        eventCallDict = {"corpName":corpName,"reportNm":reportNm,"rceptDt":rceptDt,"corpCode":corp_code}
        msg.append(eventCallDict)
        eventHandle(eventCallDict)
    logger.debug("완료")
    return msg
