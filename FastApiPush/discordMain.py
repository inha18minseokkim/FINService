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
    try:
        await bot.start(TOKEN)
    except KeyboardInterrupt:
        await bot.logout()

async def send_message(msg):
    logger.debug("실행")
    #await client.wait_until_ready()  # Wait for the client to connect and initialize
    logger.debug("wait until ready complete")
    channel = client.get_all_channels()  # Replace channel_id with the ID of your channel
    logger.debug("channel ready")
    await channel.send(msg)  # Send a message to the channel
    logger.debug("완료")
#client.run(TOKEN)