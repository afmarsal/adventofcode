def do_it(lst, times):
    cups = [None] * 1000000
    val_to_pos = [0] * 1000001
    for i, v in enumerate(lst):
        cups[i] = [v, i + 1]
        val_to_pos[v] = i
    for i in range(len(s), 1000000):
        cups[i] = [i, i]
        val_to_pos[i] = i

    curr = cups[0]
    pickup = [None] * 3
    for i in range(times):
        # if i % 100000 == 0:
        #     print(f'-- Move {i + 1} --')
        # print(f'-- Move {i + 1} --')
        # print(f'curr = {curr}, cups: {cups}')

        # Choose pickup
        n = cups[curr[1]]
        for j in range(3):
            pickup[j] = n
            n = cups[n[1]]
        curr[1] = pickup[2][1]
        # print(f'pick up: {pickup}')

        # Choose destination
        val = (curr[0] - 1, len(cups))[curr[0] - 1 == 0]
        while val in pickup:
            val = (val - 1, len(cups))[val - 1 == 0]
        dest = cups[val_to_pos[val]]

        # print(f'dest: {dest}')
        # Insert pickup
        after_pu_pos = dest[1]
        dest[1] = val_to_pos[pickup[0][0]]
        pickup[0][1] = val_to_pos[pickup[1][0]]
        pickup[1][1] = val_to_pos[pickup[2][0]]
        pickup[2][1] = after_pu_pos

        curr = cups[curr[1]]

    one = cups[val_to_pos[1]]
    first_star = cups[one[1]]
    second_star = cups[first_star[1]]
    print(f'Result: {first_star[0]}, {second_star[0]}')
    return first_star[0] * second_star[0]


if __name__ == '__main__':
    # s = list(map(int, '389125467'))
    s = list(map(int, '792845136'))
    output = do_it(s, 10000000)
    print(f'Part 2: {output}')

# Part 1:
# too high: 987423651
