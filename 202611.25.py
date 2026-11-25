import csv
import os


def dp(name):
    here = os.path.dirname(os.path.abspath(__file__))
    for c in (
        os.path.join("data", name),
        os.path.join(here, "data", name),
        os.path.join(here, "..", "data", name),
    ):
        if os.path.exists(c):
            return c
    return os.path.join("data", name)


with open(dp("17_열처리_공정.csv"), encoding="utf-8-sig") as f:
    r = csv.reader(f)
    header = next(r)
    rows = list(r)

print("실습1")
print("*" * 60)

print("행:", len(rows))
print("열:", len(header))

print(header)
