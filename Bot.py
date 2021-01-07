from discord.ext import commands
import discord
import asyncio
from utils import *

TOKEN = TOKEN
bot = commands.Bot(command_prefix="r!", case_insentitive=True)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(
type=discord.ActivityType.streaming, name="Test", url="https://twitch.com/twitch"))
  print('girildi.')
  print('reritobot!')


@bot.command()
async def yardim(ctx):
  await ctx.send("gelcek onlar")

bot.run(TOKEN)
