from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class CBInfo(Base):
    __tablename__ = "TB_CB_INFO"
    rcept_no =  Column(INT, nullable=False, autoincrement=True, primary_key=True) #접수번호
    corp_cls =  Column(TEXT, nullable=False) #법인구분
    corp_code =  Column(TEXT, nullable=False) #고유번호
    corp_name =  Column(TEXT, nullable=False) #회사명
    bd_tm =  Column(TEXT, nullable=False) #사채의 종류(회차)
    bd_knd =  Column(TEXT, nullable=False) #사채의 종류(종류)
    bd_fta =  Column(TEXT, nullable=False) #사채의 권면(전자등록)총액 (원)
    atcsc_rmislmt =  Column(TEXT, nullable=False) #정관상 잔여발행한도(원)
    ovis_fta =  Column(TEXT, nullable=False) #해외발행(권면(전자등록)총액)
    ovis_fta_crn =  Column(TEXT, nullable=False) #해외발행(권면(전자)등록총액(통화단위))
    ovis_ster =  Column(TEXT, nullable=False) #해외발행(기준환율등)
    ovis_isar =  Column(TEXT, nullable=False) #해외발행(발행지역)
    ovis_mktnm =  Column(TEXT, nullable=False) #해외발행(해외상장시 시장의 명칭)
    fdpp_fclt =  Column(TEXT, nullable=False) #자금조달의 목적(시설자금)
    fdpp_bsninh =  Column(TEXT, nullable=False) #자금조달의 목적(영업양수자금)
    fdpp_op =  Column(TEXT, nullable=False) #자금조달의 목적(운영자금)
    fdpp_dtrp =  Column(TEXT, nullable=False) #자금조달의 목적(채무상환자금)
    fdpp_ocsa =  Column(TEXT, nullable=False) #자금조달의 목적(타법인 증권 취득자금)
    fdpp_etc  =  Column(TEXT, nullable=False) #자금조달의 목적(기타자금)
    bd_intr_ex =  Column(TEXT, nullable=False) #사채의 이율(표면이자율)
    bd_intr_sf =  Column(TEXT, nullable=False) #사채의 이율(만기이자율)
    bd_mtd =  Column(TEXT, nullable=False) #사채만기일
    bdis_mthn =  Column(TEXT, nullable=False) #사채발행방법 사모공모
    cv_rt =  Column(TEXT, nullable=False)  #전환에 관한 사항(전환비율)
    cv_prc =  Column(TEXT, nullable=False) #전환에 관한 사항(전환가액 (원/주))
    cvisstk_knd =  Column(TEXT, nullable=False) #전환에 관한 사항(전환에 따라 발행할 주식
    cvisstk_cnt =  Column(TEXT, nullable=False) #전환에 관한 사항(전환에 따라 발행할 주식수
    cvisstk_tisstk_vs =  Column(TEXT, nullable=False) #전환에 관한 사항(주식총수 대비 비율)
    cvrqpd_bgd =  Column(TEXT, nullable=False) #전환청구기간(시작일)
    cvrqpd_edd =  Column(TEXT, nullable=False) #전환간(종료일)
    act_mktprcfl_cvprc_lwtsprc = Column(TEXT, nullable=False) #시가하락에 따른 전환가액 조정(최저 조정가액)
    act_mktprcfl_cvprc_lwtrsprc_bs = Column(TEXT, nullable=False) #	전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 근거))
    rmislmt_lt70p = Column(TEXT, nullable=False) #전환에 관한 사항(시가하락에 따른 전환가액 조정(발행당시 전환가액의 70% 미만으로 조정가능한 잔여 발행한도 (원)))
    abmg = Column(TEXT, nullable=False) #합병 관련 사항
    sbd = Column(TEXT, nullable=False) #청약일
    pymd = Column(TEXT, nullable=False) #납입일
    rpmcmp = Column(TEXT, nullable=False) #대표주관회사
    grint = Column(TEXT, nullable=False) #보증기간
    bddd = Column(TEXT, nullable=False) #이사회결의일
    od_a_at_t = Column(TEXT, nullable=False) #사외이사 참석여부 참석
    od_a_at_b = Column(TEXT, nullable=False) #사외이사 참석여부 불참
    adt_a_atn = Column(TEXT, nullable=False) #감사위원 참사여부
    rs_sm_atn = Column(TEXT, nullable=False) #증권신고서 제출대상 여부
    ex_sm_r = Column(TEXT, nullable=False) #면제받은경우 그 사유
    ovis_ltdtl = Column(TEXT, nullable=False) #당해 사채의 해외발행과 연계된 대차거래 내역
    ftc_stt_atn = Column(TEXT, nullable=False) #공정거래위원회 신고대상 여부