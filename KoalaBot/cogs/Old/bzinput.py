
import requests,json,ijson
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
from operator import itemgetter
class Bzin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def petflip(self, ctx):
    async def bzin(self, ctx,arg):
        await ctx.send("Getting Bazaar...")
        items2=bz(arg)
        items = sorted(items2[0], key=itemgetter(1),reverse=True)[:30]
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
                embed.add_field(name =  items[i][0].replace('_',' ').title(), value = str(round(items[i][1],2))+' Weight '+str(round(items[i][2]/60))+' Min '+str(round(items[i][2]%60))+' Secconds', inline = True)
            await ctx.send(embed = embed)
        except Exception as e:
            print(e)
        await ctx.send("Done!")
def setup(client):
    client.add_cog(Bzin(client))
def bz(arg):
    items2=0
    paredo=[]
    paredo2=[]
    r=requests.get('https://api.hypixel.net/skyblock/bazaar',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
    x=r.json()['products']
    items = []
    for i in x:
        try:
            item = x[i]['quick_status']['productId'] + ": "
            buy = round(x[i]['buy_summary'][0]["pricePerUnit"]+0.1, 1)
            sell = round(x[i]['sell_summary'][0]["pricePerUnit"]-0.1, 1)
            margin = sell-buy
            percentage = margin/buy
            weight=percentage*margin
            time=x[i]['quick_status']['sellMovingWeek']+x[i]['quick_status']['buyMovingWeek']
            time2=time/604800
            amount=int(arg)/buy
            finaltime=amount/time2
            items.append([item,weight,finaltime])
        except Exception as e:
            print(e)
    return items
