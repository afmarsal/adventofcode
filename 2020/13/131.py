import math


def do_it(filename):
    with open(filename) as f:
        v0 = int(f.readline().strip())
        bus_ids = [int(c) for c in f.readline().strip().split(',') if c != 'x']

    freqs = {bus_id: (bus_id * math.ceil(v0 / bus_id)) - v0 for bus_id in bus_ids}
    result = min(freqs, key=freqs.get)
    return result * freqs[result]


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 2305
