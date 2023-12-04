import argparse

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

with open(args.INPUT) as f:
    res = 0
    for line in f.readlines():
        card, line = line.split(':')
        #cardid = int(card[5:])

        wins, nbs = line.split("|")
        wins = [int(w) for w in wins.split()]
        nbs = [int(n) for n in nbs.split()]
        nbs = [n for n in nbs if n in wins]
        if len(nbs) > 0:
            res += 2**(len(nbs)-1)

print(res)


