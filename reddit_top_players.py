import json
from collections import Counter
import sys

teams = json.load(open("reddit.current.json"))
allplayers = json.load(open("players.current.json"))
startercount = Counter()
benchcount = Counter()
captains = Counter()

def get(playerid):
    return allplayers[str(playerid)]

for teamid, players in teams.iteritems():
    for player in players:
        info = get(player["id"])
        if player["sub"]:
            benchcount[info["web_name"]] += 1
        else:
            startercount[info["web_name"]] += 1
        if player["captain"]:
            captains[info["web_name"]] += 1

sys.stdout.write("------- captains ------\n")

for player, count in captains.most_common():
    sys.stdout.write("{}: {}\n".format(player.encode("utf8"), count))

sys.stdout.write("------- starters ------\n")

for player, count in startercount.most_common():
    sys.stdout.write("{}: {}\n".format(player.encode("utf8"), count))

sys.stdout.write("------- bench ------\n")

for player, count in benchcount.most_common():
    sys.stdout.write("{}: {}\n".format(player.encode("utf8"), count))
