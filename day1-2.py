import argparse
import regex

parser = argparse.ArgumentParser(prog=__file__)
parser.add_argument("INPUT")

args = parser.parse_args()

convert = {
#  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
#  "0": 0,
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
}

with open(args.INPUT) as f:
    res = 0
    for line in f.readlines():
        matches = regex.findall("|".join(convert.keys()), line, overlapped=True)
        res += 10*convert[matches[0]] + convert[matches[-1]]

print(res)


