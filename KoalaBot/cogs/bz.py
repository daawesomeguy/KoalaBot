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
    async def petflip(self, ctx):
        """
        Bazaar flipper command
        """
        await ctx.send("Getting profit...")
        await ctx.send("Done!")
def setup(client):
    client.add_cog(Bz(client))
