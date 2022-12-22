import json
import urllib.request

heroStats = json.load(open("heroStats.json"))

for heroStat in heroStats:
    imgURL = "https://cdn.cloudflare.steamstatic.com/" + heroStat['img']
    urllib.request.urlretrieve(imgURL, "./heroes/" + str(heroStat['id']) + ".png")