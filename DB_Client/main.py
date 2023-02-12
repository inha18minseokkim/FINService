from fastapi import FastAPI, Body
from database import engineConn
from models import corpInfo
from pydantic import BaseModel
from sqlalchemy import insert,update,Table,MetaData
app = FastAPI()
conn = engineConn()
session = conn.sessionmaker()

#meta_data = MetaData(bind=conn,reflect=True)
#finServiceTable = meta_data.tables['TB_CORP_CODE']
@app.get("/")
async def test():
    return "DBClient Server is in good condition"

@app.get("/tb_corp_code/selectCorpInfo/{corp_code}")
async def selectCorpInfo(corp_code: str):
    res = session.query(corpInfo).filter(corpInfo.corp_code == corp_code).first()
    return res

class RequestBody(BaseModel):
    corp_code: int
    corp_name: str
    stock_code: str 
    modify_date: str
        
@app.post("/tb_corp_code/insertCorpInfo")
async def insertCorpInfo(body: RequestBody):

    res = corpInfo()
    print(body.corp_code)
    res.corp_code = body.corp_code
    res.corp_name = body.corp_name
    res.stock_code = body.stock_code
    res.modify_date = body.modify_date
    session.add(res)
    session.commit()

    return {"code" : 0}

@app.post("/tb_corp_code/updateCorpInfo")
async def updateCorpInfo(body: RequestBody):
    res = session.query(corpInfo).filter(corpInfo.corp_code == body.corp_code).first()
    res.corp_name = body.corp_name
    res.stock_code = body.stock_code
    res.modify_date = body.modify_date
    session.commit()
    return {"code" : 0}