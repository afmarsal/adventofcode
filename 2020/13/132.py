def do_it(filename):
    with open(filename) as f:
        v0 = int(f.readline().strip())
        bus_ids = [int(c) for c in f.readline().strip().split(',') if c != 'x']

    # [id, offset]
    freqs = [(bus_id, i) for i, bus_id in enumerate(bus_ids) if bus_id > 0]
    print(freqs)

    step, result = freqs[0]
    for bus_id, offset in freqs[1:]:
        while (result + offset) % bus_id != 0:
            result += step
        step *= bus_id
        # print(f'found! result: {result}, step: {step}')
    return result


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 552612234243498
