import requests,json,ijson
r=requests.get('https://api.hypixel.net/skyblock/bazaar',data={'auth':'key'})
x=r.json()['products']
f = open("bazaar.txt", "a")
for i in x:
    item = x[i]['quick_status']['productId'] + ": "
    buy = round(x[i]['quick_status']['buyPrice'], 1)
    sell = round(x[i]['quick_status']['sellPrice'], 1)
    margin = round(buy - sell)
    try:
        percentage = round(margin/buy * 100, 1)
        print(item + str(buy) + " " + str(sell) + " " + str(margin) + " " + str(percentage))
    except:
        print("error")

    #f.write(x[i]['quick_status']['productId'] + ": ")
    #f.write(str(round(x[i]['quick_status']['buyPrice'] - x[i]['quick_status']['sellPrice'], 1)))
    #f.write("\n")

"""
Weight system:

Buy volume
Sell volume
Margin
Percentage
"""
