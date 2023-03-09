from loguru import logger
import sys
sys.path.append("c:\\users\\bjm77\\anaconda3\\lib\\site-packages")
from sqlalchemy import Column, TEXT, INT, BIGINT, UniqueConstraint, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class subscriptionInfo(Base):
    __tablename__ = "TB_SUBSCRIPTION_INFO_INQUIRE"
    HOUSE_MANAGE_NO = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    PBLANC_NO = Column(TEXT, nullable=False)
    HOUSE_NM = Column(TEXT, nullable=True)
    HOUSE_SECD = Column(TEXT, nullable=True)
    HOUSE_SECD_NM = Column(TEXT, nullable=True)
    HOUSE_DTL_SECD = Column(TEXT, nullable=True)
    HOUSE_DTL_SECD_NM = Column(TEXT, nullable=True)
    RENT_SECD = Column(TEXT, nullable=True)
    RENT_SECD_NM = Column(TEXT, nullable=True)
    SUBSCRPT_AREA_CODE = Column(TEXT, nullable=True)
    SUBSCRPT_AREA_CODE_NM = Column(TEXT, nullable=True)
    HSSPLY_ZIP = Column(TEXT, nullable=True)
    HSSPLY_ADRES = Column(TEXT, nullable=True)
    TOT_SUPLY_HSHLDCO = Column(Integer, nullable=True)
    RCRIT_PBLANC_DE = Column(TEXT, nullable=True)
    RCEPT_BGNDE = Column(TEXT, nullable=True)
    RCEPT_ENDDE = Column(TEXT, nullable=True)
    SPSPLY_RCEPT_BGNDE = Column(TEXT, nullable=True)
    SPSPLY_RCEPT_ENDDE = Column(TEXT, nullable=True)
    GNRL_RNK1_CRSPAREA_RCEPT_PD = Column(TEXT, nullable=True)
    GNRL_RNK1_ETC_GG_RCPTDE_PD = Column(TEXT, nullable=True)
    GNRL_RNK1_ETC_AREA_RCPTDE_PD = Column(TEXT, nullable=True)
    GNRL_RNK2_CRSPAREA_RCEPT_PD = Column(TEXT, nullable=True)
    GNRL_RNK2_ETC_GG_RCPTDE_PD = Column(TEXT, nullable=True)
    GNRL_RNK2_ETC_AREA_RCPTDE_PD = Column(TEXT, nullable=True)
    PRZWNER_PRESNATN_DE = Column(TEXT, nullable=True)
    CNTRCT_CNCLS_BGNDE = Column(TEXT, nullable=True)
    CNTRCT_CNCLS_ENDDE = Column(TEXT, nullable=True)
    HMPG_ADRES = Column(TEXT, nullable=True)
    CNSTRCT_ENTRPS_NM = Column(TEXT, nullable=True)
    MDHS_TELNO = Column(TEXT, nullable=True)
    BSNS_MBY_NM = Column(TEXT, nullable=True)
    MVN_PREARNGE_YM = Column(TEXT, nullable=True)
    SPECLT_RDN_EARTH_AT = Column(TEXT, nullable=True)
    MDAT_TRGET_AREA_SECD = Column(TEXT, nullable=True)
    PARCPRC_ULS_AT = Column(TEXT, nullable=True)
    IMPRMN_BSNS_AT = Column(TEXT, nullable=True)
    PUBLIC_HOUSE_EARTH_AT = Column(TEXT, nullable=True)
    LRSCL_BLDLND_AT = Column(TEXT, nullable=True)
    NPLN_PRVOPR_PUBLIC_HOUSE_AT = Column(TEXT, nullable=True)
    PBLANC_URL = Column(TEXT, nullable=True)
    SEARCH_HOUSE_SECD = Column(TEXT, nullable=True)
    GNRL_RCEPT_BGNDE = Column(TEXT, nullable=True)
    GNRL_RCEPT_ENDDE = Column(TEXT, nullable=True)
    def __init__(self, jsonData):
        self.HOUSE_MANAGE_NO = jsonData.get('HOUSE_MANAGE_NO')
        self.PBLANC_NO = jsonData.get('PBLANC_NO')
        self.HOUSE_NM = jsonData.get('HOUSE_NM')
        self.HOUSE_SECD = jsonData.get('HOUSE_SECD')
        self.HOUSE_SECD_NM = jsonData.get('HOUSE_SECD_NM')
        self.HOUSE_DTL_SECD = jsonData.get('HOUSE_DTL_SECD')
        self.HOUSE_DTL_SECD_NM = jsonData.get('HOUSE_DTL_SECD_NM')
        self.RENT_SECD = jsonData.get('RENT_SECD')
        self.RENT_SECD_NM = jsonData.get('RENT_SECD_NM')
        self.SUBSCRPT_AREA_CODE = jsonData.get('SUBSCRPT_AREA_CODE')
        self.SUBSCRPT_AREA_CODE_NM = jsonData.get('SUBSCRPT_AREA_CODE_NM')
        self.HSSPLY_ZIP = jsonData.get('HSSPLY_ZIP')
        self.HSSPLY_ADRES = jsonData.get('HSSPLY_ADRES')
        self.TOT_SUPLY_HSHLDCO = jsonData.get('TOT_SUPLY_HSHLDCO')
        self.RCRIT_PBLANC_DE = jsonData.get('RCRIT_PBLANC_DE')
        self.RCEPT_BGNDE = jsonData.get('RCEPT_BGNDE')
        self.RCEPT_ENDDE = jsonData.get('RCEPT_ENDDE')
        self.SPSPLY_RCEPT_BGNDE = jsonData.get('SPSPLY_RCEPT_BGNDE')
        self.SPSPLY_RCEPT_ENDDE = jsonData.get('SPSPLY_RCEPT_ENDDE')
        self.GNRL_RNK1_CRSPAREA_RCEPT_PD = jsonData.get('GNRL_RNK1_CRSPAREA_RCEPT_PD')
        self.GNRL_RNK1_ETC_GG_RCPTDE_PD = jsonData.get('GNRL_RNK1_ETC_GG_RCPTDE_PD')
        self.GNRL_RNK1_ETC_AREA_RCPTDE_PD = jsonData.get('GNRL_RNK1_ETC_AREA_RCPTDE_PD')
        self.GNRL_RNK2_CRSPAREA_RCEPT_PD = jsonData.get('GNRL_RNK2_CRSPAREA_RCEPT_PD')
        self.GNRL_RNK2_ETC_GG_RCPTDE_PD = jsonData.get('GNRL_RNK2_ETC_GG_RCPTDE_PD')
        self.GNRL_RNK2_ETC_AREA_RCPTDE_PD = jsonData.get('GNRL_RNK2_ETC_AREA_RCPTDE_PD')
        self.PRZWNER_PRESNATN_DE = jsonData.get('PRZWNER_PRESNATN_DE')
        self.CNTRCT_CNCLS_BGNDE = jsonData.get('CNTRCT_CNCLS_BGNDE')
        self.CNTRCT_CNCLS_ENDDE = jsonData.get('CNTRCT_CNCLS_ENDDE')
        self.HMPG_ADRES = jsonData.get('HMPG_ADRES')
        self.CNSTRCT_ENTRPS_NM = jsonData.get('CNSTRCT_ENTRPS_NM')
        self.MDHS_TELNO = jsonData.get('MDHS_TELNO')
        self.BSNS_MBY_NM = jsonData.get('BSNS_MBY_NM')
        self.MVN_PREARNGE_YM = jsonData.get('MVN_PREARNGE_YM')
        self.SPECLT_RDN_EARTH_AT = jsonData.get('SPECLT_RDN_EARTH_AT')
        self.MDAT_TRGET_AREA_SECD = jsonData.get('MDAT_TRGET_AREA_SECD')
        self.PARCPRC_ULS_AT = jsonData.get('PARCPRC_ULS_AT')
        self.IMPRMN_BSNS_AT = jsonData.get('IMPRMN_BSNS_AT')
        self.PUBLIC_HOUSE_EARTH_AT = jsonData.get('PUBLIC_HOUSE_EARTH_AT')
        self.LRSCL_BLDLND_AT = jsonData.get('LRSCL_BLDLND_AT')
        self.NPLN_PRVOPR_PUBLIC_HOUSE_AT = jsonData.get('NPLN_PRVOPR_PUBLIC_HOUSE_AT')
        self.PBLANC_URL = jsonData.get('PBLANC_URL')
        self.SEARCH_HOUSE_SECD = jsonData.get('SEARCH_HOUSE_SECD')
        self.GNRL_RCEPT_BGNDE = jsonData.get('GNRL_RCEPT_BGNDE')
        self.GNRL_RCEPT_ENDDE = jsonData.get('GNRL_RCEPT_ENDDE')
    def to_dict(self):
        return {
            'HOUSE_MANAGE_NO' : self.HOUSE_MANAGE_NO,
        'PBLANC_NO' : self.PBLANC_NO,
        'HOUSE_NM' : self.HOUSE_NM,
        'HOUSE_SECD' : self.HOUSE_SECD,
        'HOUSE_SECD_NM' : self.HOUSE_SECD_NM,
        'HOUSE_DTL_SECD' : self.HOUSE_DTL_SECD,
        'HOUSE_DTL_SECD_NM' : self.HOUSE_DTL_SECD_NM,
        'RENT_SECD' : self.RENT_SECD,
        'RENT_SECD_NM' : self.RENT_SECD_NM,
        'SUBSCRPT_AREA_CODE' : self.SUBSCRPT_AREA_CODE,
        'SUBSCRPT_AREA_CODE_NM' : self.SUBSCRPT_AREA_CODE_NM,
        'HSSPLY_ZIP' : self.HSSPLY_ZIP,
        'HSSPLY_ADRES' : self.HSSPLY_ADRES,
        'TOT_SUPLY_HSHLDCO' : self.TOT_SUPLY_HSHLDCO,
        'RCRIT_PBLANC_DE' : self.RCRIT_PBLANC_DE,
        'RCEPT_BGNDE' : self.RCEPT_BGNDE,
        'RCEPT_ENDDE' : self.RCEPT_ENDDE,
        'SPSPLY_RCEPT_BGNDE' : self.SPSPLY_RCEPT_BGNDE,
        'SPSPLY_RCEPT_ENDDE' : self.SPSPLY_RCEPT_ENDDE,
        'GNRL_RNK1_CRSPAREA_RCEPT_PD' : self.GNRL_RNK1_CRSPAREA_RCEPT_PD,
        'GNRL_RNK1_ETC_GG_RCPTDE_PD' : self.GNRL_RNK1_ETC_GG_RCPTDE_PD,
        'GNRL_RNK1_ETC_AREA_RCPTDE_PD' : self.GNRL_RNK1_ETC_AREA_RCPTDE_PD,
        'GNRL_RNK2_CRSPAREA_RCEPT_PD' : self.GNRL_RNK2_CRSPAREA_RCEPT_PD,
        'GNRL_RNK2_ETC_GG_RCPTDE_PD' : self.GNRL_RNK2_ETC_GG_RCPTDE_PD,
        'GNRL_RNK2_ETC_AREA_RCPTDE_PD' : self.GNRL_RNK2_ETC_AREA_RCPTDE_PD,
        'PRZWNER_PRESNATN_DE' : self.PRZWNER_PRESNATN_DE,
        'CNTRCT_CNCLS_BGNDE' : self.CNTRCT_CNCLS_BGNDE,
        'CNTRCT_CNCLS_ENDDE' : self.CNTRCT_CNCLS_ENDDE,
        'HMPG_ADRES' : self.HMPG_ADRES,
        'CNSTRCT_ENTRPS_NM' : self.CNSTRCT_ENTRPS_NM,
        'MDHS_TELNO' : self.MDHS_TELNO,
        'BSNS_MBY_NM' : self.BSNS_MBY_NM,
        'MVN_PREARNGE_YM' : self.MVN_PREARNGE_YM,
        'SPECLT_RDN_EARTH_AT' : self.SPECLT_RDN_EARTH_AT,
        'MDAT_TRGET_AREA_SECD' : self.MDAT_TRGET_AREA_SECD,
        'PARCPRC_ULS_AT' : self.PARCPRC_ULS_AT,
        'IMPRMN_BSNS_AT' : self.IMPRMN_BSNS_AT,
        'PUBLIC_HOUSE_EARTH_AT' : self.PUBLIC_HOUSE_EARTH_AT,
        'LRSCL_BLDLND_AT' : self.LRSCL_BLDLND_AT,
        'NPLN_PRVOPR_PUBLIC_HOUSE_AT' : self.NPLN_PRVOPR_PUBLIC_HOUSE_AT,
        'PBLANC_URL' : self.PBLANC_URL,
            'SEARCH_HOUSE_SECD': self.SEARCH_HOUSE_SECD,
            'GNRL_RCEPT_BGNDE': self.GNRL_RCEPT_BGNDE,
            'GNRL_RCEPT_ENDDE': self.GNRL_RCEPT_ENDDE
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

'HOUSE_SECD' : '주택구분코드(01:APT,10:신혼희망타운)',

'HOUSE_SECD_NM' : '주택구분코드명',

'HOUSE_DTL_SECD' : '주택상세구분코드(01:민영,03:국민)',

'HOUSE_DTL_SECD_NM' : '주택상세구분코드명',

'RENT_SECD' : '분양구분코드(0:분양주택,1:분양전환 가능임대,2:분양전환불가임대)',

'RENT_SECD_NM' : '분양구분코드명',

'SUBSCRPT_AREA_CODE' : '공급지역코드',

'SUBSCRPT_AREA_CODE_NM' : '공급지역명',

'HSSPLY_ZIP' : '공급위치우편번호',

'HSSPLY_ADRES' : '공급위치',

'TOT_SUPLY_HSHLDCO' : '공급규모',

'RCRIT_PBLANC_DE' : '모집공고일(YYYY-MM-DD)',

'RCEPT_BGNDE' : '청약접수시작일',

'RCEPT_ENDDE' : '청약접수종료일',

'SPSPLY_RCEPT_BGNDE' : '특별공급접수시작일',

'SPSPLY_RCEPT_ENDDE' : '특별공급접수종료일',

'GNRL_RNK1_CRSPAREA_RCEPT_PD' : '1순위접수일해당지역',

'GNRL_RNK1_ETC_GG_RCPTDE_PD' : '1순위접수일경기지역',

'GNRL_RNK1_ETC_AREA_RCPTDE_PD' : '1순위접수일기타지역',

'GNRL_RNK2_CRSPAREA_RCEPT_PD' : '2순위접수일해당지역',

'GNRL_RNK2_ETC_GG_RCPTDE_PD' : '2순위접수일경기지역',

'GNRL_RNK2_ETC_AREA_RCPTDE_PD' : '2순위접수일기타지역',

'PRZWNER_PRESNATN_DE' : '당첨자발표일',

'CNTRCT_CNCLS_BGNDE' : '계약시작일',

'CNTRCT_CNCLS_ENDDE' : '계약종료일',

'HMPG_ADRES' : '홈페이지주소',

'CNSTRCT_ENTRPS_NM' : '건설업체명(시공사)',

'MDHS_TELNO' : '문의처',

'BSNS_MBY_NM' : '사업주체명(시행사)',

'MVN_PREARNGE_YM' : '입주예정월',

'SPECLT_RDN_EARTH_AT' : '투기과열지구',

'MDAT_TRGET_AREA_SECD' : '조정대상지역(Y:과열지역,N:미대상주택,S:위축지역)',

'PARCPRC_ULS_AT' : '분양가상한제',

'IMPRMN_BSNS_AT' : '정비사업',

'PUBLIC_HOUSE_EARTH_AT' : '공공주택지구',

'LRSCL_BLDLND_AT' : '대규모택지개발지구',

'NPLN_PRVOPR_PUBLIC_HOUSE_AT' : '수도권내민영공공주택지구',

'PBLANC_URL' : '모집공고URL',

'SEARCH_HOUSE_SECD' : '주택구분 (0201:도시형생활주택, 0202:오피스텔, 0203:민간임대, 0303:공공지원민간임대)',
'GNRL_RCEPT_BGNDE' : '일반공급접수 시작일',
'GNRL_RCEPT_ENDDE' : '일반공급접수 종료일',
}