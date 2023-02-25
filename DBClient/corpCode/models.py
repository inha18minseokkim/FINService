from sqlalchemy import Column, TEXT, INT, BIGINT, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class corpInfo(Base):
    __tablename__ = "TB_CORP_CODE"
    idx = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    corp_code = Column(TEXT(length=8), nullable=False)
    corp_name = Column(TEXT, nullable=False)
    stock_code = Column(TEXT, nullable=False)
    modify_date = Column(TEXT, nullable=True)