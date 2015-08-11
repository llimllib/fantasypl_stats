import json
from collections import Counter
import sys

teams = json.load(open("reddit.current.json"))
allplayers = json.load(open("players.current.json"))
startercount = Counter()
benchcount = Counter()
captains = Counter()
positions = {
    "Goalkeeper": Counter(),
    "Defender": Counter(),
    "Midfielder": Counter(),
    "Forward": Counter(),
}

def get(playerid):
    return allplayers[str(playerid)]

for teamid, players in teams.iteritems():
    for player in players:
        info = get(player["id"])
        position = info["type_name"]
        name = info["web_name"]
        positions[position][name] += 1
        if player["sub"]:
            benchcount[info["web_name"]] += 1
        else:
            startercount[info["web_name"]] += 1
        if player["captain"]:
            captains[info["web_name"]] += 1


# Foo | Bar
# ---|---
# Foo | Bar
sys.stdout.write("Goalkeeper | Count\n")
sys.stdout.write("---------- | -----\n")

for player, count in positions["Goalkeeper"].most_common(20):
    sys.stdout.write("{} | {}\n".format(player.encode("utf8"), count))

sys.stdout.write("\nDefender | Count\n")
sys.stdout.write("---------- | -----\n")

for player, count in positions["Defender"].most_common(20):
    sys.stdout.write("{} | {}\n".format(player.encode("utf8"), count))

sys.stdout.write("\nMidfielder | Count\n")
sys.stdout.write("---------- | -----\n")

for player, count in positions["Midfielder"].most_common(20):
    sys.stdout.write("{} | {}\n".format(player.encode("utf8"), count))

sys.stdout.write("\nForward | Count\n")
sys.stdout.write("---------- | -----\n")

for player, count in positions["Forward"].most_common(20):
    sys.stdout.write("{} | {}\n".format(player.encode("utf8"), count))
