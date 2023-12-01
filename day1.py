import argparse

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

with open(args.INPUT) as f:
    res = 0
    for line in f.readlines():
        digits = [int(c) for c in line if c.isdigit()]
        res += 10*digits[0] + digits[-1]

print(res)


