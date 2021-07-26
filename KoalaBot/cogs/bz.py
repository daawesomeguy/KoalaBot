
import requests,json,ijson
from operator import itemgetter
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
import traceback
import datetime
from operator import itemgetter
class Bz(commands.Cog, name="Bazaar"):

    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def petflip(self, ctx):
    async def bz(self, ctx):
        """
        : Bazaar flipper command
        """
        await ctx.send("Getting Bazaar...")
        items = bz()
        
        try:
            embed = discord.Embed(
                title = 'Profits from the Bazaar!',
                descrption = 'Made from Hypixel API',
                colour = discord.Colour.blue()
            )

            embed.set_footer(text='Made by TheLitblock & DaAwesomeGuy')
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(len(items)):
                embed.add_field(name =  items[i][0], value = items[i][1], inline = True)
            await ctx.send(embed = embed)
        except Exception as e:
            print(e)
        
        await ctx.send(items)
        await ctx.send("Done!")
def setup(client):
    client.add_cog(Bz(client))

def bz():
    items2=0
    try:
        r=requests.get('https://api.hypixel.net/skyblock/bazaar',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
        x=r.json()['products']
        items = []
        for i in x:
            item = x[i]['quick_status']['productId'] + ": "
            buy = round(x[i]['quick_status']['buyPrice'], 1)
            sell = round(x[i]['quick_status']['sellPrice'], 1)
            margin = round(buy - sell)
            percentage = round(margin/buy * 100, 1)
            #items.append(item + str(buy) + " " + str(sell) + " " + str(margin) + " " + str(percentage))
            weight=str(((buy+sell)/5+margin)*percentage)
            items.append([item,weight])
        #f.write(x[i]['quick_status']['productId'] + ": ")
        #f.write(str(round(x[i]['quick_status']['buyPrice'] - x[i]['quick_status']['sellPrice'], 1)))
        #f.write("\n")
    except Exception as e:
        print(e)
    items2=sorted(items, key=itemgetter(1),reverse=True)
    return items2
    """
    Weight system:
    Buy volume
    Sell volume
    Margin
    Percentage
    """
