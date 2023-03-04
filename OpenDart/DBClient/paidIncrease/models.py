from sqlalchemy import Column, TEXT, INT, BIGINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class paidIncreaseInfo(Base):
    __tablename__ = "TB_PAID_INCREASE_INFO"
    rcept_no = Column(BIGINT, nullable=False,primary_key=True,unique=True)
    corp_cls = Column(TEXT, nullable=False)
    corp_code = Column(TEXT, nullable=False)
    corp_name = Column(TEXT, nullable=False)
    nstk_ostk_cnt = Column(TEXT, nullable=False)
    nstk_estk_cnt = Column(TEXT, nullable=False)
    fv_ps = Column(TEXT, nullable=False)
    bfic_tisstk_ostk = Column(TEXT, nullable=False)
    bfic_tisstk_estk = Column(TEXT, nullable=False)
    fdpp_fclt = Column(TEXT, nullable=False)
    fdpp_bsninh = Column(TEXT, nullable=False)
    fdpp_op = Column(TEXT, nullable=False)
    fdpp_dtrp = Column(TEXT, nullable=False)
    fdpp_ocsa = Column(TEXT, nullable=False)
    fdpp_etc = Column(TEXT, nullable=False)
    ic_mthn = Column(TEXT, nullable=False)
    ssl_at = Column(TEXT, nullable=False)
    ssl_bgd = Column(TEXT, nullable=False)
    ssl_edd = Column(TEXT, nullable=False)