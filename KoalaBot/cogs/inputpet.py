
import requests,json,ijson
from operator import itemgetter
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
import traceback
import datetime
def get_pet_price(names,q3,food1,price,foodamount,kat):
    q4=[]
    def value_to_float(x):
        if type(x) == float or type(x) == int:
            return x
        if 'k' in x:
            if len(x) > 1:
                return float(int(x.replace('k', ''))) * 1000
            return 1000.0
        if 'm' in x:
            if len(x) > 1:
                return float(int(x.replace('m', ''))) * 1000000
            return 1000000.0
        return 0.0
    price = [value_to_float(i) for i in price]
    for i in range(len(q3)):
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
    while True:
        try:
            r=requests.get('https://api.hypixel.net/skyblock/auctions?page=0',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
            totalpages=r.json()['totalPages']
            break
        except:
            continue
    finsihedreturn=[]
    o=0
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
                if str(name) in data['item_name'] and '[' in data['item_name']:
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
        fishprice=respons['products'][food1[i]]['quick_status']['buyPrice']
        x=[]         
        if q3[i]=='COMMON':
            try:
                for h in range(int(kat[i])):
                    o=int(katvalues[0]+o)
                    x.append(katvalues.pop(0))
                for h in range(len(x)):
                    katvalues.insert(0,x[h])
                whale1=[item for item in whalevalues if str(names[i]) in item[2]]
                r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
                p=min([item2 for item2 in whale1 if q3[i] in item2[0]])
                finished=o+int(price[i])+int(p[1])+round(fishprice)*int(foodamount[i])
                finsihedreturn.append([round(r[1]-finished),r])
            except Exception as e:
                print(e)
                pass
        elif q3[i]=='UNCOMMON':
            try:
                for h in range(int(kat[i])):
                    o=int(katvalues[0]+o)
                    x.append(katvalues.pop(0))
                for h in range(len(x)):
                    katvalues.insert(0,x[h])
                whale1=[item for item in whalevalues if str(names[i]) in item[2]]
                r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
                p=min([item2 for item2 in whale1 if q3[i] in item2[0]])
                finished=o+int(price[i])+p[1]+round(fishprice)*int(foodamount[i])
                finsihedreturn.append([round(r[1]-finished),r])
            except Exception as e:
                print(e)
                pass
        elif q3[i]=='RARE':
            try:
                for h in range(int(kat[i])):
                    o=int(katvalues[0]+o)
                    x.append(katvalues.pop(0))
                for h in range(len(x)):
                    katvalues.insert(0,x[h])
                whale1=[item for item in whalevalues if str(names[i]) in item[2]]
                r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
                p=min([item2 for item2 in whale1 if q3[i] in item2[0]])
                finished=o+int(price[i])+int(p[1])+round(fishprice)*int(foodamount[i])
                finsihedreturn.append([round(r[1]-finished),r])
            except Exception as e:
                print(e)
                pass
        elif q3[i]=='EPIC':
            try:
                for h in range(int(kat[i])):
                    h=int(katvalues[0]+o)
                    x.append(katvalues.pop(0))
                for h in range(len(x)):
                    katvalues.insert(0,x[h])
                whale1=[item for item in whalevalues if str(names[i]) in item[2]]
                r=min([item2 for item2 in whale1 if q4[i] in item2[0]])
                p=min([item2 for item2 in whale1 if q3[i] in item2[0]])
                finished=o+int(price[i])+int(p[1])+round(fishprice)*int(foodamount[i])
                finsihedreturn.append([round(r[1]-finished),r])
            except Exception as e:
                print(e)
                pass
    return finsihedreturn
class Inputpet(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def petflip(self, ctx):
    async def inputpet(self, ctx,*,arg):
        await ctx.send("Getting profit...")
        x=arg.split()
        y=[]
        for i in range(len(x)):
            y.append([])
            y[i].append(x[i])
        items = get_pet_price(y[0],y[1],y[2],y[3],y[4],y[5])
        
        try:
            embed = discord.Embed(
                title = '`Profits from the Pet!`',
                descrption = 'Made from Hypixel API',
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Made by TheLitblock & DaAwesomeGuy')
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/760479742998085655/868886766675980349/koala-173552701.jpeg?width=1270&height=953')
            for i in range(len(items)):
                embed.add_field(name =  items[i][1][0].title()+' '+items[i][1][2], value = items[i][0], inline = True)
            await ctx.send(embed = embed)
        except Exception as e:
            print(e)
        await ctx.send("Done!")
def setup(client):
    client.add_cog(Inputpet(client))
