import re


def do_it(filename):
    with open(filename) as f:
        lines = list(map(str.strip, f.readlines()))

    memory = {}
    regex = re.compile(r'mem\[(\d+)] = (\d+)')
    for line in lines:
        if line.startswith('mask'):
            mask_str = line.split('=')[1].strip()
            mask0 = int(mask_str.replace('X', '1'), 2)
            mask1 = int(mask_str.replace('X', '0'), 2)
        else:
            m = regex.fullmatch(line)
            memory[int(m[1])] = (int(m[2]) & mask0) | mask1
    return sum(memory.values())


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 4297467072083
