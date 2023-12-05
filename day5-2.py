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
            line = line.split()
            mapped = []
            for i in range(len(line) // 2):
                a = int(line[2*i])
                b = int(line[2*i+1])
                mapped.append([a, a+b])

        elif re.match("[a-z]+-to-[a-z]+ map", line):
            seeds = seeds + mapped
            mapped = []

        elif re.match("[0-9]+ [0-9]+ [0-9]+", line):
            [des_start, src_start, length] = [int(c) for c in line.split()]
            nseeds = []
            for a, b in seeds:
                # a <= src_start < src_start+length <= b
                if a <= src_start and src_start+length <= b:
                    if a < src_start:
                        nseeds.append([a, src_start])
                    if src_start+length < b:
                        nseeds.append([src_start+length, b])
                    mapped.append([des_start, des_start+length])
                # src_start < a <= src_start+length <= b
                elif src_start < a and a <= src_start+length and src_start+length <= b:
                    if src_start+length < b:
                        nseeds.append([src_start+length, b])
                    if a < src_start+length:
                        mapped.append([a-src_start+des_start, des_start+length])
                # a <= src_start <= b < src_start+length
                elif a <= src_start and src_start <= b and b < src_start+length:
                    if a < src_start:
                        nseeds.append([a, src_start])
                    if src_start < b:
                        mapped.append([des_start, b-src_start+des_start])
                # src_start < a < b < src_start+length
                elif src_start < a and b < src_start+length:
                    mapped.append([a-src_start+des_start, b-src_start+des_start])
                else:
                    nseeds.append([a,b])

            seeds = nseeds


seeds = seeds + mapped
print(min([a for a,_ in seeds]))


