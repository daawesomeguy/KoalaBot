# Libs
import discord
from discord import colour
from discord.embeds import Embed # For discord
from discord.ext import commands, tasks # For discord
import logging # For logging
from pathlib import Path # For paths
import os
from itertools import cycle
from discord.ext import commands
import traceback
import datetime
import json

from discord.ext.commands.errors import CommandNotFound
from discord.utils import get
cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Defining a few things
def get_prefix(bot, message):
    with open('KoalaBot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, owner_id=868996601341964368) #other id for 1st bot -> 760479247579480086
bot.remove_command('help')
logging.basicConfig(level=logging.INFO)
status = cycle(['with -help', 'with -', 'Hypixel Skyblock']) #add more 
whitelisted = [390562591333810187, 703042442328408155]

@bot.event
async def on_ready():
    change_status.start()
    #print(f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")
    # Another way to use variables in strings
    print("-----\nLogged in as: {} : {}\n-----".format(bot.user.name, bot.user.id))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=f"Playing with -help")) # This changes the bots 'activity'

@bot.event
async def on_guild_join(guild):
    with open('KoalaBot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = '-'

    with open('KoalaBot/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('KoalaBot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('KoalaBot/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            colour = discord.Colour.red(),
            title = "Help"
        )
        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='Command not Found!', value='Try -pong, -petflip, petinput', inline=False)
        
        await ctx.send(embed=embed)

@bot.command()
async def changeprefix(ctx, prefix):
    with open('KoalaBot/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open('KoalaBot/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

@bot.command()
async def load(ctx, extension):
    if ctx.author.id in whitelisted:
        await ctx.send('Loaded ' + extension)
        bot.load_extension(f'cogs.{extension}')
    else:
        await ctx.send('You cannot run this command')

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id in whitelisted:
        await ctx.send('Unloaded ' + extension)
        bot.unload_extension(f'cogs.{extension}')
    else:
        await ctx.send('You cannot run this command')

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title = 'Info on KoalaBot',
        descrption = 'Made from Hypixel API',
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Made by TheLitblock & DaAwesomeGuy')
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
    embed.add_field(name = 'What does this bot do?', value = 'It finds items to flip in the Bazaar and AH to flip!', inline = True)

    await ctx.send(embed = embed)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    channel = await author.create_dm()
    try:
        embed = discord.Embed(
            colour = discord.Colour.orange(),
            title = "Help"
        )

        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
        embed.set_footer(text='Made by TheLitblock & DaAwesomeGuy')
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name='-ping', value='pong!', inline=False)
        embed.add_field(name='-petflip', value='Return profits of flipping certain pets!', inline=False)
        embed.add_field(name='-inputpet', value='Input values to get profit of a petflip!', inline=False)
        embed.add_field(name='-bz', value='Bazaar weights and best items to flip!', inline=False)

        await channel.send(embed=embed)

    except Exception as e:
        print(e)


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))

for filename in os.listdir('KoalaBot/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("ODY4OTk2NjAxMzQxOTY0MzY4.YP3yJg.xwCWoypuPCjwKzfvOw91M2ZrIoc") # Runs our bot 1st bot -> NzYwNDc5MjQ3NTc5NDgwMDg2.X3MpfQ.Gnm_q982rxCqDM1w-nN2VxlzY2o
