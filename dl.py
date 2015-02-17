import requests, json, shutil, time, hashlib, glob, os

all = {}
errorout = open("errors.log", "a")

n = 0
misses = 0
playerurl = "http://fantasy.premierleague.com/web/api/elements/{}/"
while 1:
    r = requests.get(playerurl.format(n))
    n += 1
    if r.status_code != 200:
        misses += 1
        # if we get 25 misses in a row, assume we've found all players
        if misses >= 25:
            break
        continue

    misses = 0

    if n%10 == 0: print(n)

    try:
        all[n] = r.json()
    except ValueError:
        print("failed parsing player {}".format(n))
        errorout.write("Failed to parse player {}: {}\n".format(n, r.content))

t = str(time.time()).split(".")[0]
fn = "data/players.{}.json".format(t)
with file(fn, 'w') as outfile:
    json.dump(all, outfile, indent=2)

shutil.copy2(fn, "players.current.json")
