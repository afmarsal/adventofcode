import re


def generate_address(mask_str, start_idx, addresses, mask1):
    idx = mask_str.find('X', start_idx)
    if idx < 0:
        return addresses
    result = []
    for address in addresses:
        m1 = 1 << (len(mask_str) - idx - 1)
        result.append(address | m1 | mask1)
        m0 = ~m1
        result.append((address & m0) | mask1)
    # res_str = [format(m, '#010b') for m in result]
    # print("After masking: \n" + "\n".join(res_str))
    return generate_address(mask_str, idx + 1, result, mask1)


def do_it(filename):
    with open(filename) as f:
        lines = list(map(str.strip, f.readlines()))

    memory = {}
    regex = re.compile(r'mem\[(\d+)] = (\d+)')
    for line in lines:
        if line.startswith('mask'):
            mask_str = line.split('=')[1].strip()
            mask1 = int(mask_str.replace('X', '0'), 2)
        else:
            m = regex.fullmatch(line)
            for mem_add in generate_address(mask_str, 0, [int(m[1])], mask1):
                memory[mem_add] = int(m[2])
    print(memory)
    return sum(memory.values())


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 5030603328768
