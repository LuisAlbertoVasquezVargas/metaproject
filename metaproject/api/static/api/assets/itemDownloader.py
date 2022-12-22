import json
import urllib.request

itemStats = json.load(open("itemStats.json"))

for key, val in itemStats.items():
    try:
        imgURL = "https://cdn.cloudflare.steamstatic.com" + val['img']
        urllib.request.urlretrieve(imgURL, "./items/" + str(val['id']) + ".png")
    except:
        print(key)