import requests,json,ijson
from operator import itemgetter
import os

from requests.models import Response
o=0
#q2=int(input('how many whales')) FIX ME
q2=1
q3=input('what rarity? (ALL CAPS):')
q4=input('what finished rarity (ALL CAPS):')
r=requests.get('https://api.hypixel.net/skyblock/auctions?page=0',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
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
                #else:
                    #katvalues.append(data['highest_bid'])
        except KeyError:
            pass
    for data in x['auctions']:
        if 'Blue Whale' in data['item_name'] and 'Skin' not in data['item_name']:
            try:
                if data['bin']==True:
                    #whalevalues[data['starting_bid']]=data['tier']
                    whalevalues.append([data['tier'],data['starting_bid'],data['item_name']])
            except KeyError:
                pass
            #else:
                #whalevalues[data['highest_bid']]=data['tier']
                #whalevalues.append([data['highest_bid'],data['tier'],data['item_name']])
while True:
        try:
            m=requests.get('https://api.hypixel.net/skyblock/bazaar')
            respons=m.json()
            break
        except:
            continue
fishprice=respons['products']['ENCHANTED_COOKED_FISH']['quick_status']['buyPrice']
z=katvalues.sort()
whalevalues.sort(key=itemgetter(1))
for i in range(q2):
    if q3=='COMMON':
        finished=int(katvalues[0])+15000+int(whalevalues[0][1])
        print(round(min([t for t in whalevalues or t[0].startswith(q4)], key = lambda t: t[1])[1]-finished))
        katvalues.pop(0)
    elif q3=='UNCOMMON':
        finished=int(katvalues[0])+katvalues[1]+75000+int(whalevalues[0][1])
        print(round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished))
        katvalues.pop(0)
    elif q3=='RARE':
        for i in range(7):
            o=int(katvalues[0]+o)
            katvalues.pop(0)
        finished=o+int(katvalues[0])+900000+int(whalevalues[0][1])+fishprice
        [t for t in whalevalues if t[0].startswith(q4)]
        print(round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished))
    elif q3=='EPIC':
        for i in range(12):
            o=int(katvalues[0]+o)
            katvalues.pop(0)
        finished=o+int(katvalues[0])+9000000+int(whalevalues[0][1])+fishprice*6
        print(round(min([t for t in whalevalues if t[0].startswith(q4)], key = lambda t: t[1])[1]-finished))
print(min([t for t in whalevalues if t[0].startswith(q4)]))
