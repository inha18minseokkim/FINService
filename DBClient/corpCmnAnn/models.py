from sqlalchemy import Column, TEXT, INT, BIGINT, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class corpCmnAnn(Base):
    __tablename__ = "TB_CORP_CMN_ANN"
    rcept_no = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True,unique=True)
    corp_code = Column(TEXT, nullable=False)
    corp_name = Column(TEXT, nullable=False)
    report_nm = Column(TEXT, nullable=False)
    rcept_dt = Column(TEXT, nullable=True)