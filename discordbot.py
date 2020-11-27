from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!')
token = os.environ["DISCORD_BOT_TOKEN"]


@client.event
async def on_message(message):
    global channel
    if message.content == prefix + 'setchannel':
        channel = message.channel
    if channel:
        channel.send(message.content)


bot.run(token)
