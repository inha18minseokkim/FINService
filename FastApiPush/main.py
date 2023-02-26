import asyncio

from fastapi import FastAPI
from loguru import logger
import discord
import nest_asyncio
from discordMain import client,send_message
from declaration import TOKEN
app = FastAPI()
nest_asyncio.apply()

async def startBot():
    TOKEN = "your bot token here"
    # Create a new event loop
    loop = asyncio.get_event_loop()
    # Start the Discord bot in a separate task
    task = loop.create_task(client.start(TOKEN))
    # Continue running other tasks in the event loop
    await asyncio.sleep(0)
    # Do other stuff here
    logger.debug("Bot is running!")

@app.on_event("startup")
async def onStartUp():
    logger.debug("FastApiPush 시작")
    #asyncio.new_event_loop().run_in_executor(client.run(TOKEN))
    asyncio.run(startBot())
    logger.debug("discord Connection 끝")

@app.get("/test")
async def testMthd():
    logger.debug("실행")
    channel = client.get_all_channels()
    #await channel.send("Message for test in FastApiPushServer")
    await send_message("ASDF")
    return