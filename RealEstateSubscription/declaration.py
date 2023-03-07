import requests
from loguru import logger

dataPortalKey = "Rujw+Isa8li+a/gKuQ2M5xnXH9wNS8evvDQnU1h+pRTcm+QpzUcAMi7woS1urDmsbRycaM0/cBhToF1ut2BQyw=="

pushUrl = "http://172.28.166.206:32224"#"http://fastapi-push.default.svc.cluster.local:8084"

def sendDiscordMessage(txt: str):
    res = requests.post(pushUrl + f"/sendDiscordMessage/",json={"txt":txt})
    logger.debug(res)
    return res.json()