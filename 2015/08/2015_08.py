def do_str(s1):
    result = len(s1) - len(eval(s1))
    print(f'{s1} - {eval(s1)} = {len(s1)} - {len(eval(s1))} = {result}')
    return result


def do(lines):
    return sum(len(line) - len(eval(line)) for line in lines)
    # return sum(do_str(line) for line in lines)


sample = r'''""
"abc"
"aaa\"aaa"
"\x27"
'''

assert do(sample.splitlines()) == 23 - 11

lines = open('input.txt').read().splitlines()
part1 = do(lines)
print(f'# Part 1: {part1}')

# Part 1: 1633 -- too high
