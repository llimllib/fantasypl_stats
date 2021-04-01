import requests, json, shutil, time, hashlib, glob, os

all = {}
errorout = open("errors.log", "a")

n = 0
misses = 0
playerurl = 'https://fantasy.premierleague.com/drf/bootstrap-static'
players = requests.get(playerurl).json()["elements"]
t = str(time.time()).split(".")[0]
fn = "data/players.{}.json".format(t)
print(f"Writing {fn}")
with open(fn, 'w') as outfile:
    json.dump(all, outfile, indent=2)

shutil.copy2(fn, "players.current.json")
