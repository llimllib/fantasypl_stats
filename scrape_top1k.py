import json
import re
import requests
import shutil
import time

PL = "http://fantasy.premierleague.com{}"
pages = 20

teams = {}

for page in range(1, pages):
    if page % 2 == 0: print("page {}".format(page))
    link = "/my-leagues/313/standings/?ls-page={}".format(page)
    res = requests.get(PL.format(link))
    for rank, teamlink in re.findall('<td>(\d+)</td>\s*?<td><a href="(.*?)"', res.text, re.S):
        teamid = re.search('entry/(\d+)', teamlink).group(1)
        res = requests.get(PL.format(teamlink))
        player_ids = re.findall('<a href="#(\d+)" class="ismInfo', res.text)
        starters, bench = player_ids[:11], player_ids[-4:]
        teams[teamid] = [starters, bench]

t = str(time.time()).split(".")[0]
fn = "top1k/{}.json".format(t)
with file(fn, 'w') as outfile:
    json.dump(teams, outfile, indent=2)
shutil.copy2(fn, "top1k.current.json")

