# This example requires the 'message_content' intent.

import discord
from declaration import TOKEN
from discord.ext import commands
from loguru import logger
# intents = discord.Intents.default()
# intents.message_content = True
#
# client = discord.Client(intents=
intents = discord.Intents.default()  # Enable the default intents
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.event
async def on_ready():
    logger.debug(f'We have logged in as {bot.user}')

@bot.command()
async def on_message(ctx: commands.Context, member: discord.Member):
    logger.debug(f"logged in as {bot.user} running together with FastApi")

async def runDiscordBot():
    logger.debug("discordbot 시작")
    try:
        logger.debug("시작중")
        await bot.start(TOKEN)
        logger.debug(bot.get_all_channels().send("start"))
        logger.debug("시작완료")
    except KeyboardInterrupt:
        await bot.logout()
