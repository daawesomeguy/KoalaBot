import requests,json,ijson
r=requests.get('https://api.hypixel.net/skyblock/bazaar',data={'auth':'378bce43-202d-469b-b357-e2cd995236b7'})
x=r.json()['products']
f = open("bazaar.txt", "a")
for i in x:
    f.write(x[i]['quick_status']['productId'] + ": ")
    f.write(str(round(x[i]['quick_status']['buyPrice'] - x[i]['quick_status']['sellPrice'], 1)))
    f.write("\n")
    
    
