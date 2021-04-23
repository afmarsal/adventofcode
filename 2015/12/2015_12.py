import json


def part1(string):
    accum = 0

    def parse_int(str_int):
        nonlocal accum
        accum = accum + int(str_int)

    d = json.JSONDecoder(parse_int=parse_int)
    d.decode(string)
    return accum


assert part1('[1,2,3]') == 6
assert part1('{"a":2,"b":4}') == 6
assert part1('[[[3]]]') == 3
assert part1('{"a":{"b":4},"c":-1}') == 3

file_input = open('input.txt').read()
print(f'# Part 1: {part1(file_input)}')


