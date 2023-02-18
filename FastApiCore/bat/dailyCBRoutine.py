import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from declaration import crtfc_key,dbUrl
import requests
import json
from loguru import logger

url_code = "https://opendart.fss.or.kr/api/cvbdIsDecsn.json"
'''
crtfc_key	API 인증키	    STRING(40)	Y	발급받은 인증키(40자리)
corp_code	고유번호	        STRING(8)	Y	공시대상회사의 고유번호(8자리)
bgn_de	    시작일(최초접수일)	STRING(8)	Y	검색시작 접수일자(YYYYMMDD) ※ 2015년 이후 부터 정보제공
end_de	    종료일(최초접수일)	STRING(8)	Y	검색종료 접수일자(YYYYMMDD) ※ 2015년 이후 부터 정보제공
'''
dbClientUrl = dbUrl + '/tb_cb_info/'

def getCBEvent():
    # db에서 상장주식 목록 가져온다.
    # 오늘 날짜 YYYYMMDD로 가져온다.
    curDate = "20220704"
    # 이벤트 있으면 DB에 적재. 일단 사모든 공모든 적재.
    # 여기다가 for문을 넣어야됨. 그리고 DBClient corp 부분에 한번에 다 select 해서 가져올 수 있는 리퀘스트 받아야함
    for i in range(1): #후에 로직 수정 후 바꿀 예정
        data = {
            "crtfc_key" : crtfc_key,
            "corp_code" : "00797364",
            "bgn_de" : curDate,
            "end_de" : curDate
        }
        res = requests.get(url_code,params=data)

        if res.json()['status'] != '000':
            if res.json()['status'] == '013':
                logger.debug('dailyCBRoutine 아무것도 없음')
                continue #정상 응답이 아니면 그냥 continue
            else:
                logger.debug('dailyCBRoutine 뭔가 조회 실패')
                continue
        resj = res.json()['list'][0]
        logger.debug(resj)
        dbres = requests.post(dbClientUrl + 'setCurCBInfo', json=resj).json()
        logger.debug(dbres)
      #  logger.debug('dailyCBRoutine '+resj['corp_code'] + ' db 반영 호출 실패')
        logger.debug(f"dailyCBRoutine: DB반영 결과 : {dbres['code']}")

    return

if __name__ == "__main__":
    getCBEvent()