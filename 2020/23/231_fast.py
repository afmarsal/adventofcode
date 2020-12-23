class Cup:

    def __init__(self, val, nxt) -> None:
        self.val = val
        self.nxt_pos = nxt

    def __repr__(self) -> str:
        return str(self.val)


class Cups:

    def __init__(self, lst) -> None:
        self.cups = [Cup(v, (i + 1) % len(lst)) for i, v in enumerate(lst)]
        self.val_to_pos = [0] * (len(lst) + 1)
        for i in range(len(lst)):
            self.val_to_pos[lst[i]] = i

    def at_pos(self, pos):
        return self.cups[pos]

    def next(self, cup):
        return self.cups[cup.nxt_pos]

    def of_val(self, val):
        return self.cups[self.val_to_pos[val]]

    def dest(self, cup, pickup):
        val = (cup.val - 1, len(self.cups))[cup.val - 1 == 0]
        while val in pickup:
            val = (val - 1, len(self.cups))[val - 1 == 0]
        return self.cups[self.val_to_pos[val]]

    def insert_at(self, dest, pickup):
        after_pu_pos = dest.nxt_pos
        dest.nxt_pos = self.val_to_pos[pickup[0].val]
        pickup[0].nxt_pos = self.val_to_pos[pickup[1].val]
        pickup[1].nxt_pos = self.val_to_pos[pickup[2].val]
        pickup[2].nxt_pos = after_pu_pos

    def __repr__(self) -> str:
        start = self.cups[0]
        nxt = self.next(start)
        result = [str(start.val)]
        while nxt != start:
            result.append(str(nxt.val))
            nxt = self.next(nxt)
        return ' '.join(result)


def do_it(lst, times):
    cups = Cups(lst)
    curr = cups.at_pos(0)
    pickup = [None] * 3
    for i in range(times):
        print(f'-- Move {i + 1} --')
        print(f'curr = {curr}, cups: {cups}')

        # Choose pickup
        n = cups.next(curr)
        for j in range(3):
            pickup[j] = n
            n = cups.next(n)
        curr.nxt_pos = pickup[2].nxt_pos
        print(f'pick up: {pickup}')

        # Choose destination
        dest = cups.dest(curr, {v.val for v in pickup})
        print(f'dest: {dest}')
        # Insert pickup
        cups.insert_at(dest, pickup)

        curr = cups.next(curr)

    print('-- final --')
    print(f'curr = {curr}, cups: {lst}')
    start = cups.of_val(1)
    nxt = cups.next(start)
    result = []
    while nxt != start:
        result.append(str(nxt.val))
        nxt = cups.next(nxt)
    return ''.join(result)


if __name__ == '__main__':
    # s = list(map(int, '389125467'))
    s = list(map(int, '792845136'))
    output = do_it(s, 100)
    print(f'Part 1: {output}')

# Part 1: 98742365
