import argparse
import numpy as np

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

notsymbols = ".0123456789"

def check_part(a, i, j):
    loi = i-1 if i > 0 else 0
    hii = i+1 if i < a.shape[0]-1 else i
    loj = j-1 if j > 0 else 0
    hij = j+1 if j < a.shape[0]-1 else j

    return any(c for c in a[loi:hii+1, loj:hij+1].flatten()
                 if c not in notsymbols)


with open(args.INPUT) as f:
    res = 0
    engine = np.array([[c for c in line.strip()] for line in f.readlines()])
    for i in range(engine.shape[0]):
        number = None
        is_part = False
        for j in range(engine.shape[1]):
            c = engine[i][j]
            if c in "0123456789":
                if number is None:
                    number = 0
                number *= 10
                number += int(c)
                is_part |= check_part(engine, i, j)
            else:
                if is_part:
                    res += number
                number = None
                is_part = False

        if is_part:
            res += number

print(res)

