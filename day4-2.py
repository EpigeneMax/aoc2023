import argparse

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

with open(args.INPUT) as f:
    res = 0
    lines = f.readlines()
    copies = [1 for l in lines]
    for line in lines:
        card, line = line.split(':')
        #cardid = int(card[5:])

        wins, nbs = line.split("|")
        wins = [int(w) for w in wins.split()]
        nbs = [int(n) for n in nbs.split()]
        n = len([n for n in nbs if n in wins])
        c = copies[0]
        copies = copies[1:]
        res += c
        for i in range(n):
            copies[i] += c

print(res)


