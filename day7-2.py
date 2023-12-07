import argparse
import functools

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def hand_type(hand):
    assert len(hand) == 5
    counts = { c: len([x for x in hand if x == c]) for c in hand }
    if card_values["J"] in hand:
        jc = counts[card_values["J"]]
        del counts[card_values["J"]]
    else:
        jc = 0

    if jc == 5:
        return 6

    maxc = [x for x,v in counts.items() if v == max(counts.values())][0]
    counts[maxc] += jc

    if 5 in counts.values():
        return 6
    elif 4 in counts.values():
        return 5
    elif 3 in counts.values() and 2 in counts.values():
        return 4
    elif 3 in counts.values():
        return 3
    elif len([x for x, v in counts.items() if v == 2]) == 2:
        return 2
    elif 2 in counts.values():
        return 1
    else:
        return 0


def order_hands(lhs, rhs):
    ltype = hand_type(lhs)
    rtype = hand_type(rhs)
    if ltype == rtype:
        for a,b in zip(lhs, rhs):
            if a == b:
                continue
            else:
                if a < b:
                    return -1
                else:
                    return 1
        return 0
    else:
        if ltype < rtype:
            return -1
        else:
            return 1


with open(args.INPUT) as f:
    hands = []
    for line in f.readlines():
        line = line.split()
        h = [card_values[c] for c in line[0]]
        bid = int(line[1])
        hands.append((h, bid))

hands = sorted(hands, key=functools.cmp_to_key(lambda x, y: order_hands(x[0], y[0])))

res = 0
for i, v in enumerate(hands):
    res += (i+1)*v[1]


print(res)

