import argparse
from math import lcm

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()


with open(args.INPUT) as f:
    lines = f.readlines()
    instr = lines[0].strip()
    lines = lines[2:]

    nodes = {}
    for line in lines:
        line = line.split('=')
        node = line[0].strip()
        line = line[1].split(',')
        lhs = line[0].strip()[1:]
        rhs = line[1].strip()[:-1]
        nodes[node] = (lhs, rhs)

    curnode = [x for x in nodes.keys() if x[-1] == "A"]
    res = []
    for c in curnode:
        k = 0
        while c[-1] != "Z":
            for i in instr:
                k += 1
                if i == "L":
                    c = nodes[c][0]
                elif i == "R":
                    c = nodes[c][1]
                else:
                    raise ValueError(f"invalid instruction {i}")

                if c[-1] == "Z":
                    res.append(k)
                    break

print(lcm(*res))

