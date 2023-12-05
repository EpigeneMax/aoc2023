import argparse
import re

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

with open(args.INPUT) as f:
    seeds = []
    for line in f.readlines():
        if line.startswith("seeds: "):
            line = line[7:]
            mapped = [int(c) for c in line.split()]

        elif re.match("[a-z]+-to-[a-z]+ map", line):
            seeds = seeds + mapped
            mapped = []

        elif re.match("[0-9]+ [0-9]+ [0-9]+", line):
            [des_start, src_start, length] = [int(c) for c in line.split()]
            mapped = mapped + [s+des_start-src_start
                               for s in seeds
                               if src_start <= s and s < src_start + length]
            seeds = [s
                     for s in seeds
                     if not(src_start <= s and s < src_start + length)]


seeds = seeds + mapped
print(min(seeds))


