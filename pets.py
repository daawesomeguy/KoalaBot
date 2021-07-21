import requests,json,ijson
q1=int(input('how many u want'))
q2=int(input('how many whales'))
r=requests.get('https://api.hypixel.net/skyblock/auctions',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7','page':'0'})
totalpages=r.json()['totalPages']
katvalues=[]
whalevalues=[]
for i in range(1,totalpages):
    r=requests.get('https://api.hypixel.net/skyblock/auctions',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7','page':i})
    x=r.json()
    for data in x['auctions']:
        if 'Kat Flower' in data['item_name']:
            if data['bin']==True:
                katvalues.append(data['starting_bid'])
            else:
                katvalues.append(data['highest_bid'])
    for data in x['auctions']:
        if 'Blue Whale' in data['item_name']:
            if data['bin']==True:
                #whalevalues[data['starting_bid']]=data['tier']
                whalevalues.append([data['starting_bid'],data['tier'],data['item_name']])
            else:
                #whalevalues[data['highest_bid']]=data['tier']
                whalevalues.append([data['highest_bid'],data['tier'],data['item_name']])
z=katvalues.sort()
for i in range(q1):
    print(katvalues[0])
    katvalues.pop(0)
print(whalevalues)
