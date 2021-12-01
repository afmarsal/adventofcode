
def part1(nums):
    ini = nums[0]
    c = 0
    for l in nums[1:]:
        if l > ini:
            c += 1
        ini = l

    print(f'Result {c}')

def part2(nums):
    ini = sum(nums[0:3])
    c = 0
    for j, __ in enumerate(nums[1:-2]):
        i = j+1
        curr = sum(nums[i:i+3])
        # print(f'ini: {ini}, c = {c}, i = {i}, curr = {curr}')
        if curr > ini:
            c += 1
        ini = curr
    print(f'Result {c}')


nums = [int(l) for l in open('input.txt').read().splitlines()]
# part1(nums)
part2(nums)