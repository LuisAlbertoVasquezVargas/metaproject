import requests
import numpy
import time

#heroID = 108
#itemName = 'rod_of_atos'

def getStats2(heroID: int, itemName: str):
    start = time.time()

    print("getstats2 Begin")
    print("SQL1")

    sql1 = f"""
        SELECT MATCH_ID, HERO_ID, PLAYER_SLOT, PURCHASE
        FROM PLAYER_MATCHES
        WHERE HERO_ID = {heroID} AND MATCH_ID >= 6571554679
    """

    payload = {'sql':sql1}
    r = requests.get("https://api.opendota.com/api/explorer", params = payload)
    if r.status_code != 200:
        return {"err:" : "Error in sql request 1, player_matches table."}
    print("sql1 run correctly")
    playerMatches = r.json()["rows"]

    print("SQL2")
    sql2 = f"""
        SELECT match_id, radiant_win
        FROM MATCHES
        WHERE MATCHES.start_time >= extract(epoch from timestamp '2022-06-17T00:13:17.943Z')
    """
    print(sql2)
    payload = {'sql':sql2}
    r = requests.get("https://api.opendota.com/api/explorer", params = payload)
    if r.status_code != 200:
        return {"err:" : "Error in sql request 2, matches table."}
    print("sql2 run correctly")
    matches = r.json()["rows"]

    WI = numpy.zeros((2, 2))
    total = 0

    matchToRadWin = {}
    for match in matches:
        matchToRadWin[str(match['match_id'])] = str(match['radiant_win'])

    for playerMatch in playerMatches:
        matchID = str(playerMatch['match_id'])
        if matchID not in matchToRadWin:
            continue
        radWin = 1 if matchToRadWin[matchID] == "True" else 0
        player_slot = int(playerMatch['player_slot'])
        x = 1 if (player_slot < 128) == radWin else 0
        y = 0 if playerMatch.get('purchase', '0') is None or playerMatch.get('purchase', '0').get(itemName, '0') == "0" else 1
        total += 1
        WI[x][y] += 1
    
    usage = 0 if total == 0 else (WI[0][1] + WI[1][1]) / total
    winrate = 0 if (WI[1][1] + WI[0][1]) == 0 else (WI[1][1]) / (WI[1][1] + WI[0][1])

    end = time.time()
    print("getstats2 End")

    duration = end - start
    ans = {
        "totalMatches" : total,
        "usage" : '{:.2%}'.format(usage),
        "winrate" : '{:.2%}'.format(winrate),
        "queryTime" : '{0:.5f}'.format(duration) + ' seconds',
        "heroName" : None,
        "itemName" : None
    }
    return ans

