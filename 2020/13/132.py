from itertools import count


def do_it(filename):
    with open(filename) as f:
        v0 = int(f.readline().strip())
        bus_ids = [int(c) for c in f.readline().strip().replace('x', '0').split(',')]

    freqs = [[bus_id, bus_id - i] for i, bus_id in enumerate(bus_ids) if bus_id > 0]
    freqs.sort(key=lambda p: p[1], reverse=True)
    print(freqs)

    while True:
        freqs[0][1] += freqs[0][0]
        next_val = freqs[0][1]
        found = False
        for freq in freqs[1:]:
            while freq[1] < next_val:
                freq[1] += freq[0]
            found = freq[1] == next_val
            if not found:
                break
        if found:
            break

    return next_val


if __name__ == '__main__':
    output = do_it('input0.txt')
    print(f'Result: {output}')

# Result: 2305