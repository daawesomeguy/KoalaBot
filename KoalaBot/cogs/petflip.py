import discord
import requests
from discord.ext import commands
"""names=['Blue Whale'
,'Armadillo','Horse']
q3=[
    'COMMON',
    'RARE',
    'EPIC'
    ]
price=['1000','1000','1000']
food=['SPOOKY_SHARD','BROWN_MUSHROOM','BROWN_MUSHROOM']
foodamount=['1','1','1']
kat=['1','1','1']"""
class Petflip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def petflip(self, ctx, names, q3, food, price, foodamount, kat):
        await ctx.send(get_pet_price(names,q3,food,price,foodamount,kat))
    
def setup(client):
    client.add_cog(Petflip(client))

def get_pet_price(names,q3,food1,price,foodamount,kat):
    q4=[]
    for i in range(len(names)):
        q4.append('idk')
        if q3[i]=='COMMON' or q3[i]=='common' or q3[i]=='Common':
            q3[i]='COMMON'
            q4[i]='UNCOMMON'
        if q3[i]=='UNCOMMON' or q3[i]=='uncommon' or q3[i]=='Uncommon':
            q3[i]='UNCOMMON'
            q4[i]='RARE'
        if q3[i]=='RARE' or q3[i]=='Rare' or q3[i]=='rare':
            q3[i]='RARE'
            q4[i]='EPIC'
        if q3[i]=='EPIC' or q3[i]=='Epic' or q3[i]=='epic':
            q3[i]='EPIC'
            q4[i]='LEGENDARY'
    r=requests.get('https://api.hypixel.net/skyblock/auctions?page=0',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
    o=0
    finsihedreturn=[]
    totalpages=r.json()['totalPages']
    katvalues=[]
    whalevalues=[]
    for i in range(0,totalpages):
        while True:
            try:
                r=requests.get('https://api.hypixel.net/skyblock/auctions?page='+str(i),data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
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
        for name in names:
            for data in x['auctions']:
                if str(name) in data['item_name'] and 'Skin' not in data['item_name']:
                    try:
                        if data['bin']==True:
                            whalevalues.append([data['tier'],data['starting_bid'],data['item_name']])
                    except KeyError:
                        pass
    katvalues.sort()
    while True:
        try:
            m=requests.get('https://api.hypixel.net/skyblock/bazaar')
            respons=m.json()
            break
        except:
            continue
    for i in range(int(len(names))):
        x=0
        fishprice=respons['products'][food1[i]]['quick_status']['buyPrice']
        x=[]         
        if q3[i]=='COMMON':
            for h in range(int(kat[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for h in range(len(x)):
                katvalues.insert(0,x[h])
            whale1=[item for item in whalevalues if str(names[i]) in item[2]]
            r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
            print(r)
            finished=o+int(price[i])+int(r[1])+round(fishprice)*int(foodamount[i])
            finsihedreturn.append(round(r[1]-finished))
        elif q3[i]=='UNCOMMON':
            for h in range(int(kat[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for h in range(len(x)):
                katvalues.insert(0,x[h])
            print(i)
            whale1=[item for item in whalevalues if str(names[i]) in item[2]]
            r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
            print(r)
            finished=o+int(price[i])+r[1]+round(fishprice)*int(foodamount[i])
            finsihedreturn.append(round(r[1]-finished))
        elif q3[i]=='RARE':
            for h in range(int(kat[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for h in range(len(x)):
                katvalues.insert(0,x[h])
            whale1=[item for item in whalevalues if str(names[i]) in item[2]]
            r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
            print(r)
            finished=o+int(price[i])+int(r[1])+round(fishprice)*int(foodamount[i])
            finsihedreturn.append(round(r[1]-finished))
        elif q3[i]=='EPIC':
            for h in range(int(kat[i])):
                h=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for h in range(len(x)):
                katvalues.insert(0,x[h])
            whale1=[item for item in whalevalues if str(names[i]) in item[2]]
            r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
            print(r)
            finished=o+int(price[i])+int(r[1])+round(fishprice)*int(foodamount[i])
            finsihedreturn.append(round(r[1]-finished))
    return finsihedreturn
