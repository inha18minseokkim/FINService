from fastapi import FastAPI
from DBClient.databaseCmn import engineConn
from DBClient.corpCode.corpCodeMain import corpCodeRouter
from DBClient.convertibleBond.cbMain import cbRouter
from DBClient.paidIncrease.paidIncreaseMain import paidIncreaseRouter
from DBClient.stockDisposition.stockDispositionMain import stockDispositionRouter
from DBClient.corpCmnAnn.corpCmnAnnMain import corpCmnAnnRouter
from FastApiCore.api import coreRouter
app = FastAPI()
conn = engineConn()
session = conn.sessionmaker()

app.include_router(corpCodeRouter)
app.include_router(cbRouter)
app.include_router(paidIncreaseRouter)
app.include_router(stockDispositionRouter)
app.include_router(corpCmnAnnRouter)
app.include_router(coreRouter)
app.include_router(coreRouter)
#meta_data = MetaData(bind=conn,reflect=True)
#finServiceTable = meta_data.tables['TB_CORP_CODE']


@app.get("/")
async def test():
    return "Server is in good condition"

@app.get("/raiseError")
async def raiseError():
    raise Exception
    return "Exit"