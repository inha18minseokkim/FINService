from rocketry import Rocketry
from rocketry.conds import every, after_success

app = Rocketry(config={"task_execution": "async"})

@app.task(every("10 seconds"))
async def do_things():
    return ""
    #logger.debug("listener do well")
    #print("listener do well")
    
@app.task(after_success("do_things"))
async def after_do_things():
    #logger.debug("muyaho")
    return ""
'''
@app.task(every("1 hours"))
async def openDart():
    logger.debug("openDart 공시 조회 시작")
    targetList = requests.get(dbUrl+"/tb_corp_code/selectCorpInfoFixed")
    logger.debug(targetList.json()['list'])
    openDartAnnRoutine.mainRoutine(targetList.json()['list'],'20230223','I')
'''