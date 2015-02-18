import json
from collections import Counter
import sys

teams = json.load(open("top1k.current.json"))
players = json.load(open("players.current.json"))
startercount = Counter()
benchcount = Counter()

for teamid, (starters, bench) in teams.iteritems():
    for playerid in starters:
        player = players[playerid]
        startercount[player["web_name"]] += 1
    for playerid in bench:
        player = players[playerid]
        benchcount[player["web_name"]] += 1

sys.stdout.write("------- starters ------\n")

for player, count in startercount.most_common():
    sys.stdout.write("{}: {}\n".format(player.encode("utf8"), count))

sys.stdout.write("------- bench ------\n")

for player, count in benchcount.most_common():
    sys.stdout.write("{}: {}\n".format(player.encode("utf8"), count))
