# Libs
import discord # For discord
from discord.ext import commands, tasks # For discord
import logging # For logging
from pathlib import Path # For paths
import os
from itertools import cycle
from discord.ext import commands
import traceback
import datetime

from discord.ext.commands.errors import CommandNotFound
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Defining a few things
bot = commands.Bot(command_prefix='-', case_insensitive=True, owner_id=760479247579480086)
logging.basicConfig(level=logging.INFO)
status = cycle(['with -help', 'with -', 'Hypixel Skyblock']) #add more 

@bot.event
async def on_ready():
    change_status.start()
    #print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    # Another way to use variables in strings
    print("-----\nLogged in as: {} : {}\n-----\nMy current prefix is: -\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Playing with -help")) # This changes the bots 'activity'

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Check -help for commands.")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

for filename in os.listdir('KoalaBot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("NzYwNDc5MjQ3NTc5NDgwMDg2.X3MpfQ.Gnm_q982rxCqDM1w-nN2VxlzY2o") # Runs our bot
