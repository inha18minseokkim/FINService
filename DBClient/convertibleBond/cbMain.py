import json

from fastapi import APIRouter
import sys,os

from sqlalchemy.orm import DeclarativeMeta

sys.path.append("../DBClient") #상위 경로를 현재 경로에 넣어 declaration 파일 임포트 가능
from databaseCmn import engineConn,MyEncoder
from convertibleBond.models import CBInfo
from pydantic import BaseModel
from loguru import logger
from sqlalchemy import create_engine, Column, Integer, String, Table, TEXT, INT, BIGINT, MetaData, text, insert

cbRouter = APIRouter()
conn = engineConn()
session = conn.sessionmaker()
metadata = MetaData()

tbCbInfo =  Table('TB_CB_INFO',metadata,
    Column('IDX',BIGINT,nullable=False,autoincrement=True,primary_key=True),
    Column('rcept_no',TEXT, nullable=False),
    Column('corp_cls',TEXT, nullable=False),
    Column('corp_code',TEXT, nullable=False),
       Column('corp_name',TEXT, nullable=False),
       Column('bd_tm',TEXT, nullable=False),
       Column('bd_knd',TEXT, nullable=False),
       Column('bd_fta',TEXT, nullable=False) ,
       Column('atcsc_rmislmt',TEXT, nullable=False),
       Column('ovis_fta',TEXT, nullable=False) ,
       Column('ovis_fta_crn',TEXT, nullable=False),
       Column('ovis_ster',TEXT, nullable=False) ,
       Column('ovis_isar',TEXT, nullable=False),
       Column('ovis_mktnm',TEXT, nullable=False),
       Column('fdpp_fclt',TEXT, nullable=False),
       Column('fdpp_bsninh',TEXT, nullable=False),
       Column('fdpp_op',TEXT, nullable=False),
       Column('fdpp_dtrp',TEXT, nullable=False),
       Column('fdpp_ocsa',TEXT, nullable=False),
      Column('fdpp_etc',TEXT, nullable=False),
      Column('bd_intr_ex',TEXT, nullable=False),
      Column('bd_intr_sf',TEXT, nullable=False),
      Column('bd_mtd',TEXT, nullable=False),
      Column('bdis_mthn',TEXT, nullable=False),
      Column('cv_rt',TEXT, nullable=False),
      Column('cv_prc',TEXT, nullable=False),
       Column('cvisstk_knd',TEXT, nullable=False),
       Column('cvisstk_cnt',TEXT, nullable=False),
      Column('cvisstk_tisstk_vs',TEXT, nullable=False),
       Column('cvrqpd_bgd',TEXT, nullable=False),
       Column('cvrqpd_edd',TEXT, nullable=False),
      Column('act_mktprcfl_cvprc_lwtrsprc',TEXT, nullable=False),
      Column('act_mktprcfl_cvprc_lwtrsprc_bs',TEXT, nullable=False),
      Column('rmislmt_lt70p',TEXT, nullable=False),
      Column('abmg',TEXT, nullable=False),
      Column('sbd',TEXT, nullable=False),
      Column('pymd',TEXT, nullable=False),
      Column('rpmcmp',TEXT, nullable=False),
      Column('grint',TEXT, nullable=False),
      Column('bddd',TEXT, nullable=False),
      Column('od_a_at_t',TEXT, nullable=False),
      Column('od_a_at_b',TEXT, nullable=False),
      Column('adt_a_atn',TEXT, nullable=False),
      Column('rs_sm_atn',TEXT, nullable=False),
      Column('ex_sm_r',TEXT, nullable=False),
      Column('ovis_ltdtl',TEXT, nullable=False),
      Column('ftc_stt_atn',TEXT, nullable=False))
tbCbInfo.create(conn.engine,checkfirst=True)

@cbRouter.get("/tb_cb_info/")
async def cbInfoMain():
    return "CBInfo runs successfully"

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
    act_mktprcfl_cvprc_lwtrsprc : str #시가하락에 따른 전환가액 조정(최저 조정가액)
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



@cbRouter.post("/tb_cb_info/setCurCBInfo/")
async def setCBInfo(body: RequestBody):
    json_str = json.loads(json.dumps(body, cls = MyEncoder))

    logger.info(json_str)

    stmt = insert(tbCbInfo).values(json_str)
    session.execute(stmt)
    session.commit()

    logger.debug("삽입완료")

    return {'code' : 0}