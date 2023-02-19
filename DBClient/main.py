from fastapi import FastAPI
from databaseCmn import engineConn
from corpCode.corpCodeMain import corpCodeRouter
from convertibleBond.cbMain import cbRouter
from paidIncrease.paidIncreaseMain import paidIncreaseRouter
app = FastAPI()
conn = engineConn()
session = conn.sessionmaker()

app.include_router(corpCodeRouter)
app.include_router(cbRouter)
app.include_router(paidIncreaseRouter)
#meta_data = MetaData(bind=conn,reflect=True)
#finServiceTable = meta_data.tables['TB_CORP_CODE']
@app.get("/")
async def test():
    return "DBClient Server is in good condition"

@app.get("/raiseError")
async def raiseError():
    raise Exception
    return "Exit"