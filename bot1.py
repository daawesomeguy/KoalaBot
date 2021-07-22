# Libs
import discord # For discord
from discord.ext import commands # For discord
import logging # For logging
from pathlib import Path # For paths

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Defining a few things
bot = commands.Bot(command_prefix='-', case_insensitive=True, owner_id=760479247579480086)
logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    # Another way to use variables in strings
    print("-----\nLogged in as: {} : {}\n-----\nMy current prefix is: -\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(activity=discord.Game(name=f"Playing with -help")) # This changes the bots 'activity'

@bot.command(name='ping')
async def _hi(ctx):
    """
    pong
    """
    await ctx.send("pong")
    # Another way to do this code is (user object).mention
    #await ctx.send(f"Hi <@{ctx.author.id}>!")
bot.run("NzYwNDc5MjQ3NTc5NDgwMDg2.X3MpfQ.Gnm_q982rxCqDM1w-nN2VxlzY2o") # Runs our bot