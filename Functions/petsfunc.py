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
get_pet_price('Blue Whale','COMMON','UNCOMMON',100,2000,3000,10000,'ENCHANTED_COOKED_FISH',1,1,2,3,4)
