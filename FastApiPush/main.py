import asyncio

from fastapi import FastAPI
from loguru import logger
import discord
import nest_asyncio
from pydantic import BaseModel

import discordMain
from declaration import TOKEN
app = FastAPI()
nest_asyncio.apply()
asyncio.create_task(discordMain.runDiscordBot())
@app.on_event("startup")
async def onStartUp():
    logger.debug("FastApiPush 시작")
    #asyncio.new_event_loop().run_in_executor(client.run(TOKEN))
    for channel in discordMain.bot.get_all_channels():
        if isinstance(channel, discord.TextChannel):
            await channel.send("FastApi 서버 기동")

    logger.debug("discord Connection 끝")
    return

@app.get("/test")
async def testMthd():
    logger.debug("실행")
    for channel in discordMain.bot.get_all_channels():
        if isinstance(channel, discord.TextChannel):
            await channel.send("test")
    return "test complete"

@app.get("/sendDiscordMessage/{txt}")
async def sendDiscordMessage(txt: str):
    logger.debug("실행")
    for channel in discordMain.bot.get_all_channels():
        try:
            if isinstance(channel, discord.TextChannel):
                await channel.send(txt)
        except:
            return {'code' : 1 , "msg" : txt , "errorMsg" : channel.id}
    return {"code" : 0, "msg" : txt}

class item(BaseModel):
    txt: str
@app.post("/sendDiscordMessage/")
async def sendDiscordMessage(items: item):
    txt = items.txt
    logger.debug("실행")
    for channel in discordMain.bot.get_all_channels():
        try:
            if isinstance(channel, discord.TextChannel):
                logger.debug("메세지 보내기 시작" + txt)
                await channel.send(txt)
        except:
            return {'code': 1, "msg": txt, "errorMsg": channel.id}
    return {"code": 0, "msg": txt}

@app.get("/getStatus")
async def getStatus():
    return f"{discordMain.bot.status}"
