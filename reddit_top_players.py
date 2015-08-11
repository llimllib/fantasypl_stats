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
        points = info["event_total"]
        positions[position][(name, points)] += 1
        if player["sub"]:
            benchcount[info["web_name"]] += 1
        else:
            startercount[info["web_name"]] += 1
        if player["captain"]:
            captains[info["web_name"]] += 1


# Foo | Bar
# ---|---
# Foo | Bar
sys.stdout.write("Goalkeeper | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | ------ | -- | --\n")

for player, count in positions["Goalkeeper"].most_common(20):
    name, points = player
    captained = captains[name]
    started = startercount[name]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name.encode("utf8"), points, count, started, captained))

sys.stdout.write("\nDefender | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | -- | -- | --\n")

for player, count in positions["Defender"].most_common(30):
    name, points = player
    captained = captains[name]
    started = startercount[name]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name.encode("utf8"), points, count, started, captained))

sys.stdout.write("\nMidfielder | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | -- | -- | --\n")

for player, count in positions["Midfielder"].most_common(30):
    name, points = player
    captained = captains[name]
    started = startercount[name]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name.encode("utf8"), points, count, started, captained))

sys.stdout.write("\nForward | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | ------ | -------- | --\n")

for player, count in positions["Forward"].most_common(30):
    name, points = player
    captained = captains[name]
    started = startercount[name]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name.encode("utf8"), points, count, started, captained))
