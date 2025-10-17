
import discord
import requests,json,ijson
from operator import itemgetter
from requests.models import Response

def get_pet_price(name,q3,q4,price1,price2,price3,price4,food1,foodamount,kat,kat1,kat2,kat3):
    r=requests.get('https://api.hypixel.net/skyblock/auctions?page=0',data={'auth':'key'})
    o=0
    totalpages=r.json()['totalPages']
    katvalues=[]
    whalevalues=[]
    for i in range(0,totalpages):
        while True:
            try:
                r=requests.get('https://api.hypixel.net/skyblock/auctions?page='+str(i),data={'auth':'key'})
                x=r.json()
                break
            except:
                continue
        for data in x['auctions']:
            try:
                if 'Kat Flower' in data['item_name']:
                    if data['bin']==True:
                        katvalues.append(data['starting_bid'])
            except KeyError:
                pass
        for data in x['auctions']:
            if str(name) in data['item_name'] and 'Skin' not in data['item_name']:
                try:
                    if data['bin']==True:
                        whalevalues.append([data['tier'],data['starting_bid'],data['item_name']])
                except KeyError:
                    pass
    katvalues.sort()
    whalevalues.sort(key=itemgetter(1))
    while True:
        try:
            m=requests.get('https://api.hypixel.net/skyblock/bazaar')
            respons=m.json()
            break
        except:
            continue
    fishprice=respons['products'][food1]['quick_status']['buyPrice']
    if q3=='COMMON':
        for i in range(kat):
            o=int(katvalues[0]+o)
            katvalues.pop(0)
        finished=o+int(price1)+int(whalevalues[0][1])+fishprice*int(foodamount)
        return round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished)
    elif q3=='UNCOMMON':
        for i in range(kat1):
            o=int(katvalues[0]+o)
            katvalues.pop(0)
        finished=int(katvalues[0])+katvalues[1]+int(price2)+int(whalevalues[0][1])+fishprice*int(foodamount)
        return round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished)
    elif q3=='RARE':
        for i in range(kat2):
            o=int(katvalues[0]+o)
            katvalues.pop(0)
        finished=o+int(katvalues[0])+int(price3)+int(whalevalues[0][1])+fishprice*int(foodamount)
        [t for t in whalevalues if t[0].startswith(q4)]
        return round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished)
    elif q3=='EPIC':
        for i in range(kat3):
            o=int(katvalues[0]+o)
            katvalues.pop(0)
        finished=o+int(katvalues[0])+int(price4)+int(whalevalues[0][1])+fishprice*int(foodamount)
        return round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished)
    return min([t for t in whalevalues if t[0].startswith(q4)])
    return min([t for t in whalevalues if t[0].startswith(q3)])
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
    if message.content.startswith('!petflip'):
        x=message.content[8:].split()
        response=get_pet_price(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12])
        await message.channel.send(response)
    
client.run('NzYwNDc5MjQ3NTc5NDgwMDg2.X3MpfQ.Gnm_q982rxCqDM1w-nN2VxlzY2o')
