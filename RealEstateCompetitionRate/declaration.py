import requests
from loguru import logger
USERNAME_DB = "root"
PASSWORD_DB = "rlaalstjr99!"
#HOST_DB = "mysql-service.default.svc.cluster.local"
HOST_DB = "172.28.166.206"
#PORT_DB = "3306"
PORT_DB = "32379"
NAME_DB = "FINService"


dataPortalKey = "Rujw+Isa8li+a/gKuQ2M5xnXH9wNS8evvDQnU1h+pRTcm+QpzUcAMi7woS1urDmsbRycaM0/cBhToF1ut2BQyw=="

pushUrl = "http://fastapi-push.default.svc.cluster.local:8084" #"http://172.28.166.206:32224"

def sendDiscordMessage(txt: str):
    res = requests.post(pushUrl + f"/sendDiscordMessage/",json={"txt":txt})
    logger.debug(res)
    return res.json()