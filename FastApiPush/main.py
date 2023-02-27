import asyncio

from fastapi import FastAPI
from loguru import logger
import discord
import nest_asyncio
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
    return
    logger.debug("discord Connection 끝")

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
        if isinstance(channel, discord.TextChannel):
            await channel.send(txt)
    return {"code" : 0, "msg" : txt}