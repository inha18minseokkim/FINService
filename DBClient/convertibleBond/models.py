class CBModel:
    rcept_no: str #접수번호
    corp_cls: str #법인구분
    corp_code: str #고유번호
    corp_name: str #회사명
    bd_tm: str #사채의 종류(회차)
    bd_knd: str #사채의 종류(종류)
    bd_fta: str #사채의 권면(전자등록)총액 (원)
    atcsc_rmislmt: str #정관상 잔여발행한도(원)
    ovis_fta: str #해외발행(권면(전자등록)총액)
    ovis_fta_crn: str #해외발행(권면(전자)등록총액(통화단위))
    ovis_ster: str #해외발행(기준환율등)
    ovis_isar: str #해외발행(발행지역)
    ovis_mktnm: str #해외발행(해외상장시 시장의 명칭)
    fdpp_fclt: str #자금조달의 목적(시설자금)
    fdpp_bsninh: str #자금조달의 목적(영업양수자금)
    fdpp_op: str #자금조달의 목적(운영자금)
    fdpp_dtrp: str #자금조달의 목적(채무상환자금)
    fdpp_ocsa: str #자금조달의 목적(타법인 증권 취득자금)
    fdpp_etc : str #자금조달의 목적(기타자금)
    bd_intr_ex: str #사채의 이율(표면이자율)
    bd_intr_sf: str #사채의 이율(만기이자율)
    bd_mtd: str #사채만기일
    bdis_mthn: str #사채발행방법 사모공모
    cv_rt: str  #전환에 관한 사항(전환비율)
    cv_prc: str #전환에 관한 사항(전환가액 (원/주))
    cvisstk_knd: str #전환에 관한 사항(전환에 따라 발행할 주식
    cvisstk_cnt: str #전환에 관한 사항(전환에 따라 발행할 주식수
    cvisstk_tisstk_vs: str #전환에 관한 사항(주식총수 대비 비율)
    cvrqpd_bgd: str #전환청구기간(시작일)
    cvrqpd_edd: str #전환간(종료일)
    act_mktprcfl_cvprc_lwtsprc:str #시가하락에 따른 전환가액 조정(최저 조정가액)
    act_mktprcfl_cvprc_lwtrsprc_bs:str #
    