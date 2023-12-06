import argparse
import re

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

with open(args.INPUT) as f:
    for line in f.readlines():
        if line.startswith("Time:"):
            line = re.sub(" ", "", line[5:].strip())
            t = int(line)
        if line.startswith("Distance:"):
            line = re.sub(" ", "", line[9:].strip())
            d = int(line)

    # holding the button for x seconds => x*(t-x)
    # question is: for how many values of x does x*(t-x) > d hold?
    res = len([x for x in range(t+1) if x*(t-x) > d])


print(res)

