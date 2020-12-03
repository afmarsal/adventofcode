from continuouswood import ContinuousWood


def do_it(filename):
    wood = ContinuousWood.parse(filename)
    return sum(tile == '#' for tile in wood)


if __name__ == '__main__':
    output = do_it('input.txt')
    print(f'Result: {output}')

# Result: 178
