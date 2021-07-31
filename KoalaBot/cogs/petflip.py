import requests,json,ijson
from operator import itemgetter
from requests.models import Response
import time,itertools,discord, time
import numpy as np
from discord.ext import commands
import traceback
import datetime
names=['Blue Whale','Chicken','Elephant','Pig','Rabbit','Bat','Endermite','Mithril Golem','Rock','Silverfish','Wither Skeleton','Blaze','Enderman','Ghoul','Golem','Horse','Hound','Jerry','Magma Cube','Phoenix','Pigman','Skeleton','Spider','Spirit','Tarantula','Tiger','Turtle','Wolf','Giraffe','Lion','Monkey','Ocelot','Baby Yeti','Dolphin','Flying Fish','Megalodon','Squid','Guardian','Parrot','Sheep','Jellyfish']
price=['15k','75k','900k','9m',
'2k','5k','190k','250k',
'15k','75k','100k','14m',
'2k','5k','190k','250k',
'2k','5k','190k','250k',
'2k','5k','190k','250k',
'1700','5k','190k','250k'
'5k','10k','25k','50k',
'100k','1m','10m','50m',
'2k','5k','190k','250k',
'2k','5k','190k','250k',
'2k','5k','190k','250k',
'1k','5k','10k','40m',
'1k','5k','10k','5m',
'1k','5k','10k','10m',
'2k','5k','200k','250k',
'1k','5k','10k','5m',
'10k','20k','40k','100k',
'2500','5k','10k','500k',
'10k','20k','40k','100m',
'2k','5k','190k','250k',
'2k','5k','190k','250k',
'2k','5k','190k','250k',
'1k','5k','10k','5m',
'1k','5k','10k','5m',
'15k','75k','900k','14m',
'15k','75k','900k','15m',
'2k','5k','190k','250k',
'15k','75k','900k','8m',
'15k','75k','900k','14m',
'15k','75k','900k','17m',
'2k','5k','190k','250k',
'2k','5k','190k','20m',
'100k','1m','10m','50m',
'100k','1m','250k','1m',
'100k','1m','250k','10m',
'20k','100k','500k','3m',
'20k','100k','500k','3m',
'20k','100k','500k','15m',
'2k','5k','200k','250k',
'20k','100k','500k','15m'
]
food=['ENCHANTED_COOKED_FISH','ENCHANTED_COOKED_FISH','ENCHANTED_COOKED_FISH','ENCHANTED_COOKED_FISH',
'ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN',
'ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN',
'PORK','PORK','PORK','PORK',
'RABBIT','RABBIT','RABBIT','RABBIT',
'ENCHANTED_RED_MUSHROOM','ENCHANTED_RED_MUSHROOM','ENCHANTED_RED_MUSHROOM','ENCHANTED_RED_MUSHROOM',
'ENCHANTED_ENDSTONE','ENCHANTED_ENDSTONE','ENCHANTED_ENDSTONE','ENCHANTED_ENDSTONE',
'PORK','PORK','PORK','PORK',
'ENCHANTED_COBBLESTONE','ENCHANTED_COBBLESTONE','ENCHANTED_COBBLESTONE','ENCHANTED_COBBLESTONE',
'ENCHANTED_COBBLESTONE','ENCHANTED_COBBLESTONE','ENCHANTED_COBBLESTONE','ENCHANTED_COBBLESTONE',
'ENCHANTED_COAL_BLOCK','ENCHANTED_COAL_BLOCK','ENCHANTED_COAL_BLOCK','ENCHANTED_COAL_BLOCK',
'ENCHANTED_BLAZE_ROD','ENCHANTED_BLAZE_ROD','ENCHANTED_BLAZE_ROD','ENCHANTED_BLAZE_ROD',
'ENCHANTED_EYE_OF_ENDER','ENCHANTED_EYE_OF_ENDER','ENCHANTED_EYE_OF_ENDER','ENCHANTED_EYE_OF_ENDER',
'REVENANT_FLESH','REVENANT_FLESH','REVENANT_FLESH','REVENANT_FLESH',
'ENCHANTED_IRON_BLOCK','ENCHANTED_IRON_BLOCK','ENCHANTED_IRON_BLOCK','ENCHANTED_IRON_BLOCK',
'ENCHANTED_LEATHER','ENCHANTED_LEATHER','ENCHANTED_LEATHER','ENCHANTED_LEATHER',
'WOLF_TOOTH','WOLF_TOOTH','WOLF_TOOTH','WOLF_TOOTH',
'PORK','PORK','PORK','PORK',
'ENCHANTED_MAGMA_CREAM','ENCHANTED_MAGMA_CREAM','ENCHANTED_MAGMA_CREAM','ENCHANTED_MAGMA_CREAM',
'ENCHANTED_BLAZE_POWDER','ENCHANTED_BLAZE_POWDER','ENCHANTED_BLAZE_POWDER','ENCHANTED_BLAZE_POWDER',
'ENCHANTED_GRILLED_PORK','ENCHANTED_GRILLED_PORK','ENCHANTED_GRILLED_PORK','ENCHANTED_GRILLED_PORK',
'ENCHANTED_BONE','ENCHANTED_BONE','ENCHANTED_BONE','ENCHANTED_BONE',
'ENCHANTED_STRING','ENCHANTED_STRING','ENCHANTED_STRING','ENCHANTED_STRING',
'ENCHANTED_GHAST_TEAR','ENCHANTED_GHAST_TEAR','ENCHANTED_GHAST_TEAR','ENCHANTED_GHAST_TEAR',
'TARANTULA_WEB','TARANTULA_WEB','TARANTULA_WEB','TARANTULA_WEB',
'ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN','ENCHANTED_RAW_CHICKEN',
'ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH',
'ENCHANTED_SPRUCE_LOG','ENCHANTED_SPRUCE_LOG','ENCHANTED_SPRUCE_LOG','ENCHANTED_SPRUCE_LOG',
'ENCHANTED_ACACIA_LOG','ENCHANTED_ACACIA_LOG','ENCHANTED_ACACIA_LOG','ENCHANTED_ACACIA_LOG',
'ENCHANTED_RAW_BEEF','ENCHANTED_RAW_BEEF','ENCHANTED_RAW_BEEF','ENCHANTED_RAW_BEEF',
'PORK','PORK','PORK','PORK',
'ENCHANTED_JUNGLE_LOG','ENCHANTED_JUNGLE_LOG','ENCHANTED_JUNGLE_LOG','ENCHANTED_JUNGLE_LOG',
'ENCHANTED_RAW_SALMON','ENCHANTED_RAW_SALMON','ENCHANTED_RAW_SALMON','ENCHANTED_RAW_SALMON',
'ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH',
'ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH','ENCHANTED_RAW_FISH',
'PORK','PORK','PORK','PORK',
'ENCHANTED_INK_SACK','ENCHANTED_INK_SACK','ENCHANTED_INK_SACK','ENCHANTED_INK_SACK',
'ENCHANTED_PRISMARINE_SHARD','ENCHANTED_PRISMARINE_SHARD','ENCHANTED_PRISMARINE_SHARD','ENCHANTED_PRISMARINE_SHARD',
'ENCHANTED_FEATHER','ENCHANTED_FEATHER','ENCHANTED_FEATHER','ENCHANTED_FEATHER',
'ENCHANTED_MUTTON','ENCHANTED_MUTTON','ENCHANTED_MUTTON','ENCHANTED_MUTTON',
'ENCHANTED_SLIME_BALL','ENCHANTED_SLIME_BALL','ENCHANTED_SLIME_BALL','ENCHANTED_SLIME_BALL'
]
foodamount=['0','0','1','8',
'0','0','0','8',
'0','0','0','0',
'0','0','0','512',
'0','0','0','64',
'0','0','0','64',
'0','0','0','512',
'0','0','0','0',
'0','0','0','64',
'0','0','0','8',
'0','0','0','64',
'0','0','0','8',
'0','0','0','512',
'0','0','0','8',
'0','0','0','8',
'0','0','0','512',
'0','0','0','0',
'0','0','0','16',
'0','0','0','1024',
'0','0','0','8',
'0','0','0','128',
'0','0','0','512',
'0','0','0','64',
'0','0','0','512',
'0','0','0','1024',
'0','0','0','16',
'0','0','0','512',
'1','16','128','512',
'0','0','0','1024',
'0','0','0','0',
'0','0','0','512',
'0','0','0','16',
'0','0','0','16',
'0','0','0','64',
'0','0','0','0',
'0','0','0','8',
'0','0','0','64',
'0','0','0','16',
'0','0','0','512',
'0','0','0','16'
]
kat=['1','2','7','12',
'1','1','1','1',
'1','1','5','10'
,'1','1','1','1',
'1','1','1','1',
'1','1','1','3',
'1','1','3','7',
'1','2','5','20',
'1','2','7','14',
'1','1','1','3',
'1','2','7','5',
'1','2','7','12'
'1','2','6','12',
'1','1','5','10',
'1','2','5','20',
'1','1','1','1',
'1','1','5','10',
'1','1','1','3',
'1','1','5','10',
'1','2','5','20',
'1','1','5','10',
'1','1','1','3',
'1','1','3','7',
'1','1','5','10',
'1','1','5','10',
'1','2','7','12',
'1','1','5','10',
'1','1','2','5',
'1','2','7','12',
'1','2','7','12',
'1','2','7','12',
'1','1','2','5',
'1','2','6','12',
'1','2','7','14',
'1','1','5','10',
'1','2','5','20',
'1','1','2','5',
'1','1','2','5',
'1','1','5','10',
'1','1','3','7',
'1','1','5','10'
]
class Petflip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    #async def petflip(self, ctx):
    async def petflip(self, ctx):
        await ctx.send("Getting profit...")
        items2 = get_pet_price(names,food,price,foodamount,kat)
        items=sorted(items2, key=itemgetter(0),reverse=True)
        try:
            embed = discord.Embed(
                title = '`Profits from pet flipping!`',
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
    '''
    async def on_error(event, *args, **kwargs):
        embed = discord.Embed(title=':x: Event Error', colour=0xe74c3c) #Red
        embed.add_field(name='Event', value=event)
        embed.description = '```py\n%s\n```' % traceback.format_exc()
        embed.timestamp = datetime.datetime.utcnow()
        await Petflip.AppInfo.owner.send(embed=embed)
    '''
def setup(client):
    client.add_cog(Petflip(client))
def get_pet_price(names,food1,price,foodamount,kat):
    q3=[]
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
    for i in range(len(names)):
        q3.insert(0,'COMMON')
        q3.insert(0,'UNCOMMON')
        q3.insert(0,'RARE')
        q3.insert(0,'EPIC')
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
    names=np.repeat(names,4)
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
