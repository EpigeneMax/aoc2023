import argparse

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

constraints = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open(args.INPUT) as f:
    res = 0
    for line in f.readlines():
        game, line = line.split(':')
        gameid = int(game[5:])

        steps = line.split(";")
        steps = [[c.strip() for c in s.split(",")] for s in steps]
        maxcol = { col: max([int(c[:-len(col)-1]) for step in steps for c in step if c.endswith(col)]) for col in constraints.keys() }
        if all(maxcol[col] <= constraints[col] for col in constraints.keys()):
            res += gameid

print(res)


