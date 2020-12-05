import util


def do_it(filename):
    input_ints = util.read_ints_from_file(filename)
    nums = set()
    for i in input_ints:
        if i in nums:
            continue
        if 2020 - i in nums:
            return i * (2020 - i)
        nums.add(i)


if __name__ == '__main__':
    result = do_it('input01.txt')
    print(f'Result: {result}')

# Result: 32064
