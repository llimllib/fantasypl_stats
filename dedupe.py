import subprocess
from glob import glob

sums = {}
for f in glob("data/*.json"):
    md5 = subprocess.check_output(["md5", "-q", f]).strip()
    sums.setdefault(md5, []).append(f)

for sum, files in sums.items():
    for f in files[1:]:
        print("git rm {}".format(f))
        subprocess.call(["git", "rm", f])
