import discord
import asyncio
from discord.ext import commands
from utils import *

TOKEN = open("token.txt", "r").read()
bot = commands.Bot(command_prefix="r!!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

bot.run(TOKEN)
