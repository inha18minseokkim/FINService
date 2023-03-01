import re
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from loguru import logger

from openDartSvc.stockDispositionSvc import StockDispositionIntf
from openDartSvc.paidIncreaseSvc import PaidIncreaseIntf
from openDartSvc.eventPushSvcIntf import CmnEventPushSvcIntf


def eventHandle(dict) -> CmnEventPushSvcIntf:
    corpName = dict['corp_name']
    rceptDt = dict['rcept_dt']
    reportNm = dict['report_nm']
    corpCode = dict['corp_code']

    if re.search('.*유상증자.*', reportNm):
        logger.debug(f'{corpName} {reportNm} {rceptDt} 유상증자 결정')
        return PaidIncreaseIntf()
    elif re.search('.*자기주식처분.*', reportNm):
        logger.debug(f'{corpName} {rceptDt} 자기주식처분 결정')
        return StockDispositionIntf()
    else:
        logger.debug(f'{corpName} {rceptDt} 기타 사항')
        return CmnEventPushSvcIntf()