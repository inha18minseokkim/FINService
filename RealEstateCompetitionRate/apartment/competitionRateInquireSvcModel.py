from loguru import logger
from sqlalchemy import Column, TEXT, INT, BIGINT, UniqueConstraint, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TB_APT_COMPETITION_RATE(Base):
    __tablename__ = "TB_APT_COMPETITION_RATE"
    HOUSE_MANAGE_NO = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    PBLANC_NO = Column(TEXT, nullable=False)
    
    def __init__(self, jsonData):
        self.HOUSE_MANAGE_NO = jsonData.get('HOUSE_MANAGE_NO')
        self.PBLANC_NO = jsonData.get('PBLANC_NO')
        
    def to_dict(self):
        return {
            'HOUSE_MANAGE_NO' : self.HOUSE_MANAGE_NO,
        'PBLANC_NO' : self.PBLANC_NO,
        
        }
    def getMsg(self):
        curdict = self.to_dict()
        logger.debug(curdict)
        resMsg = ""
        for k,v in curdict.items():
            resMsg += infoDict[k]
            resMsg += " : "
            resMsg += f"{v}"
            resMsg += "\n"
        return resMsg
infoDict = {
'HOUSE_MANAGE_NO' : '주택관리번호',

'PBLANC_NO' : '공고번호',

'HOUSE_NM' : '주택명',

'MODEL_NO'	:'모델번호',

'HOUSE_TY'	: '주택형',

'SUPLY_HSHLDCO' :	'공급세대수',

'SUBSCRPT_RANK_CODE' :	'순위',

'RESIDE_SECD' :	'거주코드 (01: 해당지역, 02: 기타지역, 03: 기타경기)',

'RESIDE_SENM' :	'거주지역',

'REQ_CNT'	: '접수건수',

'CMPET_RATE'    : '경쟁률',

'LWET_SCORE' :	'최저당첨가점',

'TOP_SCORE':	'최고당첨가점',

'AVRG_SCORE' :	'평균당첨가점'
}