from itertools import count


def do_it(filename):
    with open(filename) as f:
        v0 = int(f.readline().strip())
        bus_ids = [int(c) for c in f.readline().strip().replace('x', '0').split(',')]

    freqs = {}
    for bus_id in bus_ids:
        if bus_id != 0:
            for i in count(0, bus_id):
                if i >= v0:
                    freqs[bus_id] = i - v0
                    break

    result = min(freqs, key=freqs.get)
    return result * freqs[result]


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 2305