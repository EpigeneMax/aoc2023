import argparse
import re

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

with open(args.INPUT) as f:
    for line in f.readlines():
        if line.startswith("Time:"):
            times = [int(t) for t in line[5:].split()]
        if line.startswith("Distance:"):
            dists = [int(d) for d in line[9:].split()]

    res = 1
    for (t, d) in zip(times, dists):
        # holding the button for x seconds => x*(t-x)
        # question is: for how many values of x does x*(t-x) > d hold?
        res *= len([x for x in range(t+1) if x*(t-x) > d])


print(res)

