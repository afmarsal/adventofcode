from continuouswood import ContinuousWood


def do_it(filename):
    wood = ContinuousWood.parse(filename)
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    # steps = [(1, 2)]
    result = 1
    for step in steps:
        wood.step = step
        partial = sum(tile == '#' for tile in wood)
        print(f'Partial for {step}: {partial}')
        result *= partial
    return result


if __name__ == '__main__':
    output = do_it('input031.txt')
    print(f'Result: {output}')

# Result: 3492520200
