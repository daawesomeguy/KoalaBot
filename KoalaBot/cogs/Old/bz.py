
import requests,json,ijson
from operator import itemgetter
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
import traceback
import datetime
from operator import itemgetter
class Bz(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bz(self, ctx, page):
        await ctx.send("Getting Bazaar...")
        items = bz()
        try:
            page1= discord.Embed(
                title = '`Profits from the Bazaar! Pg.1`',
                colour = discord.Colour.blue()
            )
            page1.set_footer(text='Made by TheLitblock & DaAwesomeGuy') 
            page1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            page1.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(25):
                page1.add_field(name =  items[i][0].replace('_',' ').title(), value = str(round(items[i][1],2))+' Weight', inline = True)

            page2=discord.Embed(
                title = '`Profits from the Bazaar!`',
                colour = discord.Colour.blue()
            )
            page2.set_footer(text='Made by TheLitblock & DaAwesomeGuy, Page 2') 
            page2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            page2.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(25):
                page2.add_field(name =  items[i+25][0].replace('_',' ').title(), value = str(round(items[i+25][1],2))+' Weight', inline = True)
            
            page3=discord.Embed(
                title = '`Profits from the Bazaar!`',
                colour = discord.Colour.blue()
            )
            page3.set_footer(text='Made by TheLitblock & DaAwesomeGuy, Page 3') 
            page3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            page3.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(25):
                page3.add_field(name =  items[i+50][0].replace('_',' ').title(), value = str(round(items[i+50][1],2))+' Weight', inline = True)

            page4=discord.Embed(
                title = '`Profits from the Bazaar!`',
                colour = discord.Colour.blue()
            )
            page4.set_footer(text='Made by TheLitblock & DaAwesomeGuy, Page 4') 
            page4.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            page4.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(2):
                page4.add_field(name =  items[i+75][0].replace('_',' ').title(), value = str(round(items[i+75][1],2))+' Weight', inline = True)


            pages = [page1, page2, page3, page4]

            await ctx.send(embed = pages[int(page) - 1])
        except Exception as e:
            if (str(e) == "list index out of range"):
                await ctx.send("`Error. Try a number between 1, 4.`")
            else:
                print(e)

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
            weight=int(((buy+sell)/5+margin)*percentage)
            items.append([item,weight])
        #f.write(x[i]['quick_status']['productId'] + ": ")
        #f.write(str(round(x[i]['quick_status']['buyPrice'] - x[i]['quick_status']['sellPrice'], 1)))
        #f.write("\n")
    except Exception as e:
        print(e)
    items2=sorted(items, key=itemgetter(1),reverse=True)
    print(len(items2))
    return items2
    """
    Weight system:
    Buy volume
    Sell volume
    Margin
    Percentage
    """

"""class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reaction()
        except  discord.HTTPException:
            pass
"""
