import util


def do_it(filename):
    seen_ints = set()
    accums = {}
    input_ints = util.read_ints_from_file(filename)
    for n in input_ints:
        if 2020 - n in accums:
            factors = accums[2020 - n]
            return n * factors[0] * factors[1]
        for j in seen_ints:
            current_accum = n + j
            accums[current_accum] = [n, j]
        seen_ints.add(n)


if __name__ == '__main__':
    result = do_it('input01.txt')
    print(f'Result: {result}')

# Result: 193598720
