import discord
from discord.ext import commands

class Petflip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def petflip(self, ctx):
        await ctx.send('test')

def setup(client):
    client.add_cog(Petflip(client))