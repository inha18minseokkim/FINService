import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from declaration import crtfc_key
url = "url = https://opendart.fss.or.kr/api/cvbdIsDecsn.json"
'''
crtfc_key	API 인증키	STRING(40)	Y	발급받은 인증키(40자리)
corp_code	고유번호	STRING(8)	Y	공시대상회사의 고유번호(8자리)
※ 개발가이드 > 공시정보 > 고유번호 참고
bgn_de	시작일(최초접수일)	STRING(8)	Y	검색시작 접수일자(YYYYMMDD) ※ 2015년 이후 부터 정보제공
end_de	종료일(최초접수일)	STRING(8)	Y	검색종료 접수일자(YYYYMMDD) ※ 2015년 이후 부터 정보제공
'''
def getCBEvent():
    # db에서 상장주식 목록 가져온다.
    # 오늘 날짜 YYYYMMDD로 가져온다.
    # 이벤트 있으면 DB에 적재. 일단 사모든 공모든 적재.
    return