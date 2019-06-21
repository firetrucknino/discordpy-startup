from discord.ext import commands
import os
import traceback
import sys
import discord
from discord.ext impoart tasks
from datetime import datetime
from datetime import *
from time import *

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
