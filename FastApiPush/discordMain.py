# This example requires the 'message_content' intent.

import discord
from declaration import TOKEN
from loguru import logger
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logger.debug(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

async def send_message(msg):
    logger.debug("실행")
    #await client.wait_until_ready()  # Wait for the client to connect and initialize
    logger.debug("wait until ready complete")
    channel = client.get_all_channels()  # Replace channel_id with the ID of your channel
    logger.debug("channel ready")
    await channel.send(msg)  # Send a message to the channel
    logger.debug("완료")
#client.run(TOKEN)