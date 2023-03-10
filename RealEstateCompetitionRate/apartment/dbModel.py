from loguru import logger
from sqlalchemy import Column, TEXT, INT, BIGINT, UniqueConstraint, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class aptCompetitionRate(Base):
    __tablename__ = "TB_APT_COMPETITION_RATE"
    HOUSE_MANAGE_NO = Column(INT, autoincrement=True, primary_key=True)
    PBLANC_NO = Column(Integer, nullable=True)
    MODEL_NO = Column(VARCHAR(5), nullable=False,primary_key=True)
    HOUSE_TY = Column(VARCHAR(15), nullable=False,primary_key=True)
    SUPLY_HSHLDCO = Column(VARCHAR(5), nullable=True)
    SUBSCRPT_RANK_CODE = Column(VARCHAR(5), nullable=False,primary_key=True)
    RESIDE_SECD = Column(VARCHAR(5), nullable=False,primary_key=True)
    RESIDE_SENM = Column(TEXT, nullable=True)
    REQ_CNT = Column(TEXT, nullable=True)
    CMPET_RATE = Column(TEXT, nullable=True)
    LWET_SCORE = Column(INT, nullable=True)
    TOP_SCORE = Column(INT, nullable=True)
    AVRG_SCORE = Column(INT, nullable=True)
    
    def __init__(self, jsonData):
        self.HOUSE_MANAGE_NO = jsonData.get('HOUSE_MANAGE_NO')
        self.PBLANC_NO = jsonData.get('PBLANC_NO')
        self.MODEL_NO = jsonData.get('MODEL_NO')
        self.HOUSE_TY = jsonData.get('HOUSE_TY')
        self.SUPLY_HSHLDCO = jsonData.get('SUPLY_HSHLDCO')
        self.SUBSCRPT_RANK_CODE = jsonData.get('SUBSCRPT_RANK_CODE')
        self.RESIDE_SECD = jsonData.get('RESIDE_SECD')
        self.RESIDE_SENM = jsonData.get('RESIDE_SENM')
        self.REQ_CNT = jsonData.get('REQ_CNT')
        self.CMPET_RATE = jsonData.get('CMPET_RATE')
        self.LWET_SCORE = jsonData.get('LWET_SCORE')
        self.TOP_SCORE = jsonData.get('TOP_SCORE')
        self.AVRG_SCORE = jsonData.get('AVRG_SCORE')
        
    def to_dict(self):
        return {
            'HOUSE_MANAGE_NO' : self.HOUSE_MANAGE_NO,
            'PBLANC_NO' : self.PBLANC_NO,
            'MODEL_NO' : self.MODEL_NO,
            'HOUSE_TY' : self.HOUSE_TY,
            'SUPLY_HSHLDCO' : self.SUPLY_HSHLDCO,
            'SUBSCRPT_RANK_CODE' : self.SUBSCRPT_RANK_CODE,
            'RESIDE_SECD' : self.RESIDE_SECD,
            'RESIDE_SENM' : self.RESIDE_SENM,
            'REQ_CNT' : self.REQ_CNT,
            'CMPET_RATE' : self.CMPET_RATE,
            'LWET_SCORE' : self.LWET_SCORE,
            'TOP_SCORE' : self.TOP_SCORE,
            'AVRG_SCORE' : self.AVRG_SCORE
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
'HOUSE_MANAGE_NO' : '??????????????????',

'PBLANC_NO' : '????????????',

'HOUSE_NM' : '?????????',

'MODEL_NO'	:'????????????',

'HOUSE_TY'	: '?????????',

'SUPLY_HSHLDCO' :	'???????????????',

'SUBSCRPT_RANK_CODE' :	'??????',

'RESIDE_SECD' :	'???????????? (01: ????????????, 02: ????????????, 03: ????????????)',

'RESIDE_SENM' :	'????????????',

'REQ_CNT'	: '????????????',

'CMPET_RATE'    : '?????????',

'LWET_SCORE' :	'??????????????????',

'TOP_SCORE':	'??????????????????',

'AVRG_SCORE' :	'??????????????????'
}