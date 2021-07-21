import requests
r=requests.get('https://api.slothpixel.me/api/skyblock/auctions',data={'sortBy':'idk'})
print(r.text)
