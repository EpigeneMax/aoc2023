import argparse
import functools

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()


with open(args.INPUT) as f:
    res = 0
    for line in f.readlines():
        seqs = []
        cur = [int(c) for c in line.split()]
        while any(c != 0 for c in cur):
            seqs.append(cur)
            cur = [cur[i+1]-cur[i] for i in range(len(cur)-1)]
        # add an extra zero
        cur.append(0)
        seqs.append(cur)
        for i in range(2,len(seqs)+1):
            seqs[-i].append(seqs[-i+1][-1] + seqs[-i][-1])

        res += seqs[0][-1]


print(res)

