import sys
from loguru import logger
sys.path.append("../..")

from databaseCmn import engineConn
from sqlalchemy import Column, Integer, Table, TEXT, MetaData, and_

conn = engineConn()

metadata = MetaData()
tbAptCompetitionRate = Table("TB_APT_COMPETITION_RATE",metadata,
Column('HOUSE_MANAGE_NO',Integer,autoincrement=True, primary_key=True),
Column('PBLANC_NO',  Integer,nullable=True, ),
Column('MODEL_NO',TEXT,nullable=True ),
Column('HOUSE_TY',TEXT,nullable=True ),
Column('SUPLY_HSHLDCO',Integer, nullable=True),
Column('SUBSCRPT_RANK_CODE',Integer, nullable=True),
Column('RESIDE_SECD',TEXT,nullable=True ),
Column('RESIDE_SENM',TEXT,nullable=True ),
Column('REQ_CNT',TEXT,nullable=True ),
Column('CMPET_RATE',TEXT,nullable=True ),
Column('LWET_SCORE',Integer, nullable=True),
Column('TOP_SCORE',Integer, nullable=True),
Column('AVRG_SCORE',Integer, nullable=True)
)

def createTable():
    tbAptCompetitionRate.create(conn.engine,checkfirst=True)