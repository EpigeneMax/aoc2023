import argparse
import numpy as np

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

def is_adjacent(pos, st, len):
    (a, b) = pos
    (i,j) = st
    loi = i-1 if i > 0 else 0
    hii = i+1
    loj = j-1 if j > 0 else 0
    hij = j+len
    return loi <= a and a <= hii and loj <= b and b <= hij

with open(args.INPUT) as f:
    res = 0
    engine = np.array([[c for c in line.strip()] for line in f.readlines()])
    numbers = []
    for i in range(engine.shape[0]):
        nb_start = None
        nb_len = 0
        for j in range(engine.shape[1]):
            c = engine[i][j]
            if c in "0123456789":
                if nb_start is None:
                    nb_start = (i,j)
                    nb_len = 1
                else:
                    nb_len += 1
            else:
                if nb_start is not None:
                    numbers.append((nb_start, nb_len))
                nb_start = None
                nb_len = 0

        if nb_start is not None:
            numbers.append((nb_start, nb_len))

    for i in range(engine.shape[0]):
        for j in range(engine.shape[1]):
            c = engine[i][j]
            if c != '*':
                continue

            adj = [nb for nb in numbers if is_adjacent((i,j), nb[0], nb[1])]
            if len(adj) == 2:
                tmp = 1
                for ((a,b),l) in adj:
                    tmp *= int("".join(engine[a,b:b+l]))
                res += tmp

print(res)

