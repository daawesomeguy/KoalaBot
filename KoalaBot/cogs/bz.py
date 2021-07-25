import requests,json,ijson
from operator import itemgetter
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
import traceback
import datetime
class Bz(commands.Cog, name="Bazaar"):

    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def petflip(self, ctx):
    async def bz(self, ctx):
        """
        : Bazaar flipper command
        """
        await ctx.send("Getting profit...")
        await ctx.send(bz())
        await ctx.send("Done!")
def setup(client):
    client.add_cog(Bz(client))

def bz():
    r=requests.get('https://api.hypixel.net/skyblock/bazaar',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
    x=r.json()['products']
    f = open("bazaar.txt", "a")
    items = []
    for i in x:
        item = x[i]['quick_status']['productId'] + ": "
        buy = round(x[i]['quick_status']['buyPrice'], 1)
        sell = round(x[i]['quick_status']['sellPrice'], 1)
        margin = round(buy - sell)
        try:
            percentage = round(margin/buy * 100, 1)
            items.append(item + str(buy) + " " + str(sell) + " " + str(margin) + " " + str(percentage))
        except:
            print("error")

        #f.write(x[i]['quick_status']['productId'] + ": ")
        #f.write(str(round(x[i]['quick_status']['buyPrice'] - x[i]['quick_status']['sellPrice'], 1)))
        #f.write("\n")
    return items
    """
    Weight system:

    Buy volume
    Sell volume
    Margin
    Percentage
    """
