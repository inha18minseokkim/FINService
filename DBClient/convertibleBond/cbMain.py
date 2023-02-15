from fastApi import APIRouter
import sys,os
sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn
from convertibleBond.models import CBInfo
from pydantic import BaseModel
from loguru import logger
cbRouter = APIRouter()
conn = engineConn()
session = conn.sessionmaker()

@cbRouter.get("/tb_cb_info/CurCBInfo/{curDate}")
async def selectCBInfo(curDate: str): #일자 기준으로 해당하는 데이터가 있는지 조사
    res = session.query(CBInfo).filter(CBInfo.bddd == curDate).all()
    if res == None: return {'code' : 1}

    return res

class RequestBody(BaseModel):
    rcept_no : str #접수번호
    corp_cls : str #법인구분
    corp_code : str #고유번호
    corp_name : str #회사명
    bd_tm : str #사채의 종류(회차)
    bd_knd : str #사채의 종류(종류)
    bd_fta : str #사채의 권면(전자등록)총액 (원)
    atcsc_rmislmt : str #정관상 잔여발행한도(원)
    ovis_fta : str #해외발행(권면(전자등록)총액)
    ovis_fta_crn : str #해외발행(권면(전자)등록총액(통화단위))
    ovis_ster : str #해외발행(기준환율등)
    ovis_isar : str #해외발행(발행지역)
    ovis_mktnm : str #해외발행(해외상장시 시장의 명칭)
    fdpp_fclt : str #자금조달의 목적(시설자금)
    fdpp_bsninh : str #자금조달의 목적(영업양수자금)
    fdpp_op : str #자금조달의 목적(운영자금)
    fdpp_dtrp : str #자금조달의 목적(채무상환자금)
    fdpp_ocsa : str #자금조달의 목적(타법인 증권 취득자금)
    fdpp_etc  : str #자금조달의 목적(기타자금)
    bd_intr_ex : str #사채의 이율(표면이자율)
    bd_intr_sf : str #사채의 이율(만기이자율)
    bd_mtd : str #사채만기일
    bdis_mthn : str #사채발행방법 사모공모
    cv_rt : str  #전환에 관한 사항(전환비율)
    cv_prc : str #전환에 관한 사항(전환가액 (원/주))
    cvisstk_knd : str #전환에 관한 사항(전환에 따라 발행할 주식
    cvisstk_cnt : str #전환에 관한 사항(전환에 따라 발행할 주식수
    cvisstk_tisstk_vs : str #전환에 관한 사항(주식총수 대비 비율)
    cvrqpd_bgd : str #전환청구기간(시작일)
    cvrqpd_edd : str #전환간(종료일)
    act_mktprcfl_cvprc_lwtsprc : str #시가하락에 따른 전환가액 조정(최저 조정가액)
    act_mktprcfl_cvprc_lwtrsprc_bs : str #	전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 근거))
    rmislmt_lt70p : str #전환에 관한 사항(시가하락에 따른 전환가액 조정(발행당시 전환가액의 70% 미만으로 조정가능한 잔여 발행한도 (원)))
    abmg : str #합병 관련 사항
    sbd : str #청약일
    pymd : str #납입일
    rpmcmp : str #대표주관회사
    grint : str #보증기간
    bddd : str #이사회결의일
    od_a_at_t : str #사외이사 참석여부 참석
    od_a_at_b : str #사외이사 참석여부 불참
    adt_a_atn : str #감사위원 참사여부
    rs_sm_atn : str #증권신고서 제출대상 여부
    ex_sm_r : str #면제받은경우 그 사유
    ovis_ltdtl : str #당해 사채의 해외발행과 연계된 대차거래 내역
    ftc_stt_atn : str #공정거래위원회 신고대상 여부

@cbRouter.post("/tb_cb_info/CurCBInfo/")
async def setCBInfo(body: RequestBody):
    res = CBInfo()
    try:
        res.rcept_no = int(body.rcept_no)  # 접수번호
    except:
        logger.debug("Int 변환 실패")
        return {'code' : 1, 'msg' : 'setCBInfo : Int 변환 실패'}
    res.corp_cls  = body.corp_cls # 법인구분
    res.corp_code = body.corp_code # 고유번호
    res.corp_name = body.corp_name # 회사명
    res.bd_tm  = body.bd_tm# 사채의 종류(회차)
    res.bd_knd = body.bd_knd# 사채의 종류(종류)
    res.bd_fta  = body.bd_fta# 사채의 권면(전자등록)총액 (원)
    res.atcsc_rmislmt = body.atcsc_rmislmt # 정관상 잔여발행한도(원)
    res.ovis_fta = body.ovis_fta # 해외발행(권면(전자등록)총액)
    res.ovis_fta_crn = body.ovis_fta_crn # 해외발행(권면(전자)등록총액(통화단위))
    res.ovis_ster = body.ovis_ster # 해외발행(기준환율등)
    res.ovis_isar = body.ovis_isar # 해외발행(발행지역)
    res.ovis_mktnm = body.ovis_mktnm # 해외발행(해외상장시 시장의 명칭)
    res.fdpp_fclt = body.fdpp_fclt # 자금조달의 목적(시설자금)
    res.fdpp_bsninh = body.fdpp_bsninh # 자금조달의 목적(영업양수자금)
    res.fdpp_op = body.fdpp_op# 자금조달의 목적(운영자금)
    res.fdpp_dtrp = body.fdpp_dtrp # 자금조달의 목적(채무상환자금)
    res.fdpp_ocsa = body.fdpp_ocsa # 자금조달의 목적(타법인 증권 취득자금)
    res.fdpp_etc = body.fdpp_etc # 자금조달의 목적(기타자금)
    res.bd_intr_ex = body.bd_intr_ex  # 사채의 이율(표면이자율)
    res.bd_intr_sf  = body.bd_intr_sf# 사채의 이율(만기이자율)
    res.bd_mtd = body.bd_mtd # 사채만기일
    res.bdis_mthn = body.bdis_mthn # 사채발행방법 사모공모
    res.cv_rt = body.cv_rt # 전환에 관한 사항(전환비율)
    res.cv_prc = body.cv_prc # 전환에 관한 사항(전환가액 (원/주))
    res.cvisstk_knd = body.cvisstk_knd # 전환에 관한 사항(전환에 따라 발행할 주식
    res.cvisstk_cnt = body.cvisstk_cnt # 전환에 관한 사항(전환에 따라 발행할 주식수
    res.cvisstk_tisstk_vs = body.cvisstk_tisstk_vs# 전환에 관한 사항(주식총수 대비 비율)
    res.cvrqpd_bgd = body.cvrqpd_bgd # 전환청구기간(시작일)
    res.cvrqpd_edd = body.cvrqpd_edd # 전환간(종료일)
    res.act_mktprcfl_cvprc_lwtsprc = body.act_mktprcfl_cvprc_lwtsprc # 시가하락에 따른 전환가액 조정(최저 조정가액)
    res.act_mktprcfl_cvprc_lwtrsprc_bs = body.act_mktprcfl_cvprc_lwtrsprc_bs  # 전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 근거))
    res.rmislmt_lt70p = body.rmislmt_lt70p # 전환에 관한 사항(시가하락에 따른 전환가액 조정(발행당시 전환가액의 70% 미만으로 조정가능한 잔여 발행한도 (원)))
    res.abmg = body.abmg # 합병 관련 사항
    res.sbd = body.sbd # 청약일
    res.pymd = body.pymd # 납입일
    res.rpmcmp = body.rpmcmp # 대표주관회사
    res.grint = body.grint # 보증기간
    res.bddd = body.bddd # 이사회결의일
    res.od_a_at_t = body.od_a_at_t # 사외이사 참석여부 참석
    res.od_a_at_b = body.od_a_at_b # 사외이사 참석여부 불참
    res.adt_a_atn = body.adt_a_atn # 감사위원 참사여부
    res.rs_sm_atn = body.rs_sm_atn # 증권신고서 제출대상 여부
    res.ex_sm_r = body.ex_sm_r # 면제받은경우 그 사유
    res.ovis_ltdtl = body.ovis_ltdtl # 당해 사채의 해외발행과 연계된 대차거래 내역
    res.ftc_stt_atn = body.ftc_stt_atn # 공정거래위원회 신고대상 여부
    try:
        session.commit()
        logger.debug("삽입완료")
    except:
        session.rollback()
        logger.debug("삽입실패")
        return {'code' : 1, 'msg' : 'setCBInfo : 삽입 실패' }
    return {'code' : 0}