def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

scan = get_lines("input.txt")

time = int(scan[0].split(':')[1].replace(" ", ""))
distance = int(scan[1].split(':')[1].replace(" ", ""))

ways = 0
for m in range(time):
    cur_dist = m * (time - m)
    ways += 1 if cur_dist > distance else 0

print(ways)