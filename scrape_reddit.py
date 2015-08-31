#!/usr/bin/env python2
import json
import re
import requests
import shutil
import time

# http://fantasy.premierleague.com/my-leagues/1466/standings/?ls-page=86
PL = "http://fantasy.premierleague.com{}"
pages = 88

teams = {}

for page in range(1, pages):
    if page % 2 == 0: print("page {}".format(page))
    link = "/my-leagues/1466/standings/?ls-page={}".format(page)
    res = requests.get(PL.format(link))
    import ipdb; ipdb.set_trace()
    for rank, teamlink in re.findall('<td>([\d,]+)</td>\s*?<td><a href="(.*?)"', res.text, re.S):
        teamid = re.search('entry/(\d+)', teamlink).group(1)
        res = requests.get(PL.format(teamlink))
        player_json = [json.loads(i) for i in re.findall('ismPitchElement\s*({.*?})', res.text)]
        players = [{"id": j["id"],
                    "captain": j["is_captain"],
                    "vice_captain": j["is_vice_captain"],
                    "sub": False if not j["sub"] else True}
                    for j in player_json]
        teams[teamid] = players

t = str(time.time()).split(".")[0]
fn = "reddit/{}.json".format(t)
with file(fn, 'w') as outfile:
    json.dump(teams, outfile, indent=2)
shutil.copy2(fn, "reddit.current.json")
