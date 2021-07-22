import requests,json,ijson
from operator import itemgetter
from requests.models import Response
#name,q3,q4,price1,price2,price3,price4,food1,foodamount,kat,kat1,kat2,kat3
def get_pet_price(names,q3,q4,price1,price2,price3,price4,food1,foodamount,kat,kat1,kat2,kat3):
    r=requests.get('https://api.hypixel.net/skyblock/auctions?page=0',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
    o=0
    totalpages=r.json()['totalPages']
    katvalues=[]
    whalevalues={}
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
                            whalevalues[data['tier'],data['starting_bid'],data['item_name']]=name
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
    print(int(len(names)))
    for i in range(int(len(names))):
        fishprice=respons['products'][food1[0]]['quick_status']['buyPrice']
        print(q3[i])
        print(kat[i])
        x=[]
        print('debug3')
        if q3[i]=='COMMON':
            print('debug')
            for i in range(int(kat[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for i in range(len(x)):
                katvalues.insert(0,x[i])
            print(min({k:v for (k,v) in whalevalues.items() if q3[i] in k}))
            finished=o+int(price1[i])+int(min({k:v for (k,v) in whalevalues.items() if q3[i] in k})[1])+fishprice*int(foodamount[i][0])
            return round(-finished+min({k:v for (k,v) in whalevalues.items() if q4[i] in k})[1])
        elif q3[i]=='UNCOMMON':
            for i in range(int(kat1[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for i in range(len(x)):
                katvalues.insert(0,x[i])
            finished=o+int(price1[i])+int(min({k:v for (k,v) in whalevalues.items() if q3[i] in k})[1])+fishprice*int(foodamount[i][0])
            return round(-finished+min({k:v for (k,v) in whalevalues.items() if q4[i] in k})[1])
        elif q3[i]=='RARE':
            print('debug2')
            for i in range(int(kat2[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for i in range(len(x)):
                katvalues.insert(0,x[i])
            finished=o+int(price1[i])+int(min({k:v for (k,v) in whalevalues.items() if q3[i] in k})[1])+fishprice*int(foodamount[i][0])
            return round(-finished+min({k:v for (k,v) in whalevalues.items() if q4[i] in k})[1])
        elif q3[i]=='EPIC':
            print('debug')
            for i in range(int(kat3[i])):
                o=int(katvalues[0]+o)
                x.append(katvalues.pop(0))
            for i in range(len(x)):
                katvalues.insert(0,x[i])
            finished=o+int(price1[i])+int(min({k:v for (k,v) in whalevalues.items() if q3[i] in k})[1])+fishprice*int(foodamount[i][0])
            return round(-finished+min({k:v for (k,v) in whalevalues.items() if q4[i] in k})[1])
names=['Blue Whale'
,'Armadillo']
q3=[
    'COMMON',
    'RARE'
]
q4=[
    'UNCOMMON',
    'EPIC'
]
price1=['1000','1000']
price2=['1000','1000']
price3=['1000','1000']
price4=['1000','1000']
food1=['SPOOKY_SHARD','BROWN_MUSHROOM']
foodamount=['1','2','3','4']
kat=['1','1']
kat1=['2','2']
kat2=['3','3']
kat3=['4','4']
print(get_pet_price(names,q3,q4,price1,price2,price3,price4,food1,foodamount,kat,kat1,kat2,kat3))
