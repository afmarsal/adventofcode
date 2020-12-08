import re

with open("input021.txt") as f:
    # Map lines in file to list of Match objects matching pattern
    ml = list(map(lambda l: re.match(r'^(\d+)-(\d+) (\w+): (\w+)$', l), f))
    # Method str.count returns the number of occurrences of a substring in a string. Then check
    # if that count is between the allowed range. True evaluates to 1, so summing all gives the
    # desired result
    print("A: ", sum(int(m[1]) <= m[4].count(m[3]) <= int(m[2]) for m in ml))
    # Sum the times it's True that ONLY 1 position match the condition (XOR)
    print("B: ", sum((m[4][int(m[1]) - 1] == m[3]) != (m[4][int(m[2]) - 1] == m[3]) for m in ml))
