import sys

from loguru import logger

from .subscriptionInfoInquireSvcModel import TB_APT_SUBSCRIPTION_INFO_INQUIRE

sys.path.append("..")
from databaseCmn import engineConn
from docutils.nodes import tbody
from sqlalchemy import create_engine, Column, Integer, String, Table, TEXT, INT, BIGINT, MetaData, text, insert
metadata = MetaData()
tbSubscriptionInfoInquire = Table("TB_APT_SUBSCRIPTION_INFO_INQUIRE",metadata,
Column('HOUSE_MANAGE_NO',Integer, nullable=False, autoincrement=True, primary_key=True),
Column('PBLANC_NO',TEXT, nullable=False),
Column('HOUSE_NM',TEXT, nullable=True),
Column('HOUSE_SECD',TEXT, nullable=True),
Column('HOUSE_SECD_NM',TEXT, nullable=True),
Column('HOUSE_DTL_SECD',TEXT, nullable=True),
Column('HOUSE_DTL_SECD_NM',TEXT, nullable=True),
Column('RENT_SECD',TEXT, nullable=True),
Column('RENT_SECD_NM',TEXT, nullable=True),
Column('SUBSCRPT_AREA_CODE',TEXT, nullable=True),
Column('SUBSCRPT_AREA_CODE_NM',TEXT, nullable=True),
Column('HSSPLY_ZIP',TEXT, nullable=True),
Column('HSSPLY_ADRES',TEXT, nullable=True),
Column('TOT_SUPLY_HSHLDCO',Integer, nullable=True),
Column('RCRIT_PBLANC_DE',TEXT, nullable=True),
Column('RCEPT_BGNDE',TEXT, nullable=True),
Column('RCEPT_ENDDE',TEXT, nullable=True),
Column('SPSPLY_RCEPT_BGNDE',TEXT, nullable=True),
Column('SPSPLY_RCEPT_ENDDE',TEXT, nullable=True),
Column('GNRL_RNK1_CRSPAREA_RCEPT_PD',TEXT, nullable=True),
Column('GNRL_RNK1_ETC_GG_RCPTDE_PD',TEXT, nullable=True),
Column('GNRL_RNK1_ETC_AREA_RCPTDE_PD',TEXT, nullable=True),
Column('GNRL_RNK2_CRSPAREA_RCEPT_PD',TEXT, nullable=True),
Column('GNRL_RNK2_ETC_GG_RCPTDE_PD',TEXT, nullable=True),
Column('GNRL_RNK2_ETC_AREA_RCPTDE_PD',TEXT, nullable=True),
Column('PRZWNER_PRESNATN_DE',TEXT, nullable=True),
Column('CNTRCT_CNCLS_BGNDE',TEXT, nullable=True),
Column('CNTRCT_CNCLS_ENDDE',TEXT, nullable=True),
Column('HMPG_ADRES',TEXT, nullable=True),
Column('CNSTRCT_ENTRPS_NM',TEXT, nullable=True),
Column('MDHS_TELNO',TEXT, nullable=True),
Column('BSNS_MBY_NM',TEXT, nullable=True),
Column('MVN_PREARNGE_YM',TEXT, nullable=True),
Column('SPECLT_RDN_EARTH_AT',TEXT, nullable=True),
Column('MDAT_TRGET_AREA_SECD',TEXT, nullable=True),
Column('PARCPRC_ULS_AT',TEXT, nullable=True),
Column('IMPRMN_BSNS_AT',TEXT, nullable=True),
Column('PUBLIC_HOUSE_EARTH_AT',TEXT, nullable=True),
Column('LRSCL_BLDLND_AT',TEXT, nullable=True),
Column('NPLN_PRVOPR_PUBLIC_HOUSE_AT',TEXT, nullable=True),
Column('PBLANC_URL',TEXT, nullable=True))


conn = engineConn()
def createTable():
    tbSubscriptionInfoInquire.create(conn.engine,checkfirst=True)

def saveDB(tb: TB_APT_SUBSCRIPTION_INFO_INQUIRE):
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