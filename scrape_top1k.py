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
    teamlink = "/drf/entry/{}/event/6/picks"
    link = "/drf/leagues-classic-standings/313?phase=1&le-page=1&ls-page={}"
    res = requests.get(PL.format(link)).json()
    for team in teams['standings']:
        teamid = team['entry']
        team_roster = requests.get(PL.format(teamlink.format(teamid))).json()
        players = team_roster['picks']
        players = [{"id": j["id"],
                    "captain": j["is_captain"],
                    "vice_captain": j["is_vice_captain"],
                    "sub": False if not j["sub"] else True}
                    for j in player_json]
        teams[teamid] = players

t = str(time.time()).split(".")[0]
fn = "top1k/{}.json".format(t)
with file(fn, 'w') as outfile:
    json.dump(teams, outfile, indent=2)
shutil.copy2(fn, "top1k.current.json")

