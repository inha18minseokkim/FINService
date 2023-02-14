from fastapi import FastAPI
from databaseCmn import engineConn
from corpCode.corpCodeMain import corpCodeRouter
app = FastAPI()
conn = engineConn()
session = conn.sessionmaker()

app.include_router(corpCodeRouter)
#meta_data = MetaData(bind=conn,reflect=True)
#finServiceTable = meta_data.tables['TB_CORP_CODE']
@app.get("/")
async def test():
    return "DBClient Server is in good condition"

@app.get("/raiseError")
async def raiseError():
    raise Exception
    return "Exit"