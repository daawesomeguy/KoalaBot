
import requests,json,ijson
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
from operator import itemgetter
class pbz(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def petflip(self, ctx):
    async def pbz(self, ctx,arg):
        await ctx.send("Getting Bazaar...")
        items2=bz(arg)
        paredofinal2=[]
        items = sorted(items2[0], key=itemgetter(1),reverse=True)
        for i in items2[1]:
            paredofinal2.append(items2[2][i])
        items=[x for x in items if x[0] in paredofinal2]
        print(items)
        try:
            embed = discord.Embed(
                title = 'Profits from the Bazaar!',
                descrption = 'Made from Hypixel API',
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Made by TheLitblock & DaAwesomeGuy') 
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(len(paredofinal2)):
                embed.add_field(name =  paredofinal2[i].replace('_',' ').title(), value = str(round(items[i][1],2))+' Weight '+str(round(items[i][2]/60))+' Min '+str(round(items[i][2]%60))+' Secconds', inline = True)
            await ctx.send(embed = embed)
        except Exception as e:
            print(e)
        await ctx.send("Done!")
def setup(client):
    client.add_cog(pbz(client))
def is_pareto_efficient(costs):
    is_efficient = np.ones(costs.shape[0], dtype = bool)
    idx=[]
    for i, c in enumerate(costs):
        if is_efficient[i]:
            is_efficient[is_efficient] = np.any(costs[is_efficient]<c, axis=1)  # Keep any point with a lower cost
            is_efficient[i] = True
            idx.append(i)
    return idx
def bz(arg):
    items2=0
    paredo=[]
    paredo2=[]
    r=requests.get('https://api.hypixel.net/skyblock/bazaar',data={'auth':'key'})
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
            paredo.append((percentage,margin))
            paredo2.append(item)
            time=x[i]['quick_status']['sellMovingWeek']+x[i]['quick_status']['buyMovingWeek']
            time2=time/604800
            amount=int(arg)/buy
            finaltime=amount/time2
            items.append([item,weight,finaltime])
        except Exception as e:
            print(e)
    paredoarray=np.array(paredo)
    paredofinal=is_pareto_efficient(paredoarray)
    return [items,paredofinal,paredo2]
