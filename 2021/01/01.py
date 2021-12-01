nums = [int(l) for l in open('input.txt').read().splitlines()]

ini = nums[0]
c = 0
for l in nums[1:]:
    if l > ini:
        c += 1
    ini = l

print(f'Result {c}')
