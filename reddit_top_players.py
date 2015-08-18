import json
from collections import Counter, OrderedDict
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

def tableheader(position):
    sys.stdout.write("{} | Points | Owned | Started | Captained\n".format(position))
    sys.stdout.write("-- | -- | -- | -- | --\n")

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

display_counts = OrderedDict([
    ("Goalkeeper", 20),
    ("Defender", 40),
    ("Midfielder", 40),
    ("Forward", 30),
])

for position, display_count in display_counts.iteritems():
    tableheader(position)
    for player_id, count in positions[position].most_common(display_count):
        player = get(player_id)
        name = fullname(player)
        points = player["event_points"]
        captained = captains[player_id]
        started = startercount[player_id]
        sys.stdout.write("{} | {} | {} | {} | {}\n".format(name, points, count, started, captained))
    sys.stdout.write("\n")
