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

def fullname(player):
    return "{} {}".format(player["first_name"].encode("utf8"), player["second_name"].encode("utf8"))

for teamid, players in teams.iteritems():
    for player in players:
        position = get(player["id"])["type_name"]
        positions[position][player["id"]] += 1

        if player["sub"]:
            benchcount[player["id"]] += 1
        else:
            startercount[player["id"]] += 1
        if player["captain"]:
            captains[player["id"]] += 1


# Foo | Bar
# ---|---
# Foo | Bar
sys.stdout.write("Goalkeeper | Points | Owned | Started | Captained\n")
sys.stdout.write("-- | -- | -- | -- | --\n")

for player_id, count in positions["Goalkeeper"].most_common(20):
    player = get(player_id)
    name = fullname(player)
    points = player["event_points"]
    captained = captains[player_id]
    started = startercount[player_id]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name, points, count, started, captained))

sys.stdout.write("\nDefender | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | -- | -- | --\n")

for player_id, count in positions["Defender"].most_common(30):
    player = get(player_id)
    name = fullname(player)
    points = player["event_points"]
    captained = captains[player_id]
    started = startercount[player_id]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name, points, count, started, captained))

sys.stdout.write("\nMidfielder | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | -- | -- | --\n")

for player_id, count in positions["Midfielder"].most_common(30):
    player = get(player_id)
    name = fullname(player)
    points = player["event_points"]
    captained = captains[player_id]
    started = startercount[player_id]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name, points, count, started, captained))

sys.stdout.write("\nForward | Points | Owned | Started | Captained\n")
sys.stdout.write("---------- | ----- | ------ | -------- | --\n")

for player_id, count in positions["Forward"].most_common(30):
    player = get(player_id)
    name = fullname(player)
    points = player["event_points"]
    captained = captains[player_id]
    started = startercount[player_id]
    sys.stdout.write("{} | {} | {} | {} | {}\n".format(name, points, count, started, captained))
