from rocketry import Rocketry
from rocketry.conds import every, after_success
from loguru import logger

app = Rocketry(config={"task_execution": "async"})

@app.task(every("10 seconds"))
async def do_things():
    logger.debug("listener do well")
    print("listener do well")
    
@app.task(after_success("do_things"))
async def after_do_things():
    logger.debug("muyaho")