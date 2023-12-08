import argparse
import functools

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

    res = 0
    curnode = "AAA"
    while curnode != "ZZZ":
        for i in instr:
            res += 1
            if i == "L":
                curnode = nodes[curnode][0]
            elif i == "R":
                curnode = nodes[curnode][1]
            else:
                raise ValueError(f"invalid instruction {i}")

            if curnode == "ZZZ":
                break

print(res)

