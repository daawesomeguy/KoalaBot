
import discord


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == '!ping':
        response = "pong"
        await message.channel.send(response)

client.run('NzYwNDc5MjQ3NTc5NDgwMDg2.X3MpfQ.Gnm_q982rxCqDM1w-nN2VxlzY2o')
