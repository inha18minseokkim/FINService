from fastapi import FastAPI 
from scheduler import app as app_rocketry

app = FastAPI()
session = app_rocketry.session

@app.get("/")
def helloWorld():
    return {"Hello" : "World"}

@app.on_event("startup")
def onStartUp():
    task = session["do_things"]
    task.force_run = True
    
@app.get("/tasks")
async def read_tasks():
    return list(session.tasks)