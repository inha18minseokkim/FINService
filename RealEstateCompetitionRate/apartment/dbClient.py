import sys
from loguru import logger
sys.path.append("..")

from databaseCmn import engineConn
from sqlalchemy import Column, Integer, Table, TEXT, MetaData, and_, VARCHAR
from .dbModel import aptCompetitionRate

conn = engineConn()

metadata = MetaData()
tbAptCompetitionRate = Table("TB_APT_COMPETITION_RATE",metadata,
Column('HOUSE_MANAGE_NO',Integer,autoincrement=True, primary_key=True),
Column('PBLANC_NO',  Integer,nullable=True ),
Column('MODEL_NO',VARCHAR(5),nullable=False,primary_key=True),
Column('HOUSE_TY',VARCHAR(15),nullable=False,primary_key=True ),
Column('SUPLY_HSHLDCO',VARCHAR(5), nullable=True),
Column('SUBSCRPT_RANK_CODE',VARCHAR(5), nullable=False,primary_key=True),
Column('RESIDE_SECD',VARCHAR(5),nullable=False,primary_key=True),
Column('RESIDE_SENM',TEXT,nullable=True ),
Column('REQ_CNT',TEXT,nullable=True ),
Column('CMPET_RATE',TEXT,nullable=True ),
Column('LWET_SCORE',Integer, nullable=True),
Column('TOP_SCORE',Integer, nullable=True),
Column('AVRG_SCORE',Integer, nullable=True)
)

def createTable():
    tbAptCompetitionRate.create(conn.engine,checkfirst=True)

def selectDataByHouseManageNm(houseManageNm: str) -> aptCompetitionRate:
    session = conn.sessionmaker()
    res = session.query(aptCompetitionRate).filter(aptCompetitionRate.HOUSE_MANAGE_NO == houseManageNm).all()
    session.close()
    return res


def saveDB(tb: aptCompetitionRate):
    session = conn.sessionmaker()
    try:
        session.add(tb)
        session.commit()
    except Exception as e:
        logger.debug("삽입 중 오류 {e}", e=e, exc_info=True)
        session.rollback()
        session.close()
        return {'code': 1}
    logger.debug("삽입완료")

    return {'code': 0}