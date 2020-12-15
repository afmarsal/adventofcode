SAMPLE_0 = '0,3,6'
SAMPLE_1 = '1,3,2'
SAMPLE_2 = '2,1,3'
SAMPLE_3 = '1,2,3'
SAMPLE_4 = '2,3,1'
INPUT_0 = '5,2,8,16,18,0,1'


def do_it(input, times):
    num_list = list(map(int, input.split(',')))
    # { number: last_turn]
    numbers = {v: i + 1 for i, v in enumerate(num_list)}

    spoken = num_list[len(num_list) - 1]
    initial_turn = len(numbers) + 1

    for turn in range(initial_turn, times + 1):
        prev_spoken = spoken
        if spoken in numbers:
            spoken = (turn - 1) - numbers[spoken]
            numbers[prev_spoken] = (turn - 1)
        else:
            spoken = 0
        numbers[prev_spoken] = turn - 1

    return spoken


if __name__ == '__main__':
    output = do_it(INPUT_0, 2020)
    print(f'Part 1: {output}')
    output = do_it(INPUT_0, 30000000)
    print(f'Part 2: {output}')

# Part 1: 517
# Part 2: 1047739
