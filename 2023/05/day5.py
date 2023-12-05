import itertools
import unittest
import operator
import re
import functools
import operator as op
from collections import defaultdict
from pprint import pprint

def get_lines(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def part1(filename):
    scan = get_lines(filename)
    seeds = [int(n.strip()) for n in scan[0].split(':')[1].split()]
    chunks = defaultdict(list)
    scan = scan[2:]
    start = True
    for i in range(len(scan)):
        if scan[i].strip() == '':
            start = True
            continue
        if start:
            nl = re.match(r'([^-]+)-to-([^ ]+)', scan[i])
            if not nl:
                raise Exception(f'{scan[i]} not matched')
            c1, c2 = nl[1], nl[2]
            start = False
            continue
        numbers = [int(n.strip()) for n in scan[i].split()]
        chunks[c1].append((c2, numbers))

    locations = seeds[:]
    for i, seed in enumerate(seeds):
        log(f'Seed {seed}')
        next_map = 'seed'
        while next_map != 'location':
            curr_map = next_map
            for rng in chunks[curr_map]:
                next_map, (dst, src, l) = rng
                # log(f'Processing {seed} in {curr_map} -> {dst}, {src}, {l}')
                offset = locations[i] - src
                if 0 <= offset < l:
                    locations[i] = dst + offset
                    log(f'Found location {i}: {seed}, nxt map:{next_map}, new location:{locations[i]}')
                    break
            else:
                log(f'Not Found location {i}: {seed}, nxt map:{next_map}, keep location:{locations[i]}')
    print(locations)
    return min(locations)


def generate_new_ranges(loc_start, loc_length, src, l):
    res = {'change': set(), 'no_change': set()}
    if loc_start + loc_length < src or src + l < loc_start:
        # Disjoint
        res['no_change'].add((loc_start, loc_length))
        return res
    if loc_start >= src and loc_start + loc_length <= src + l:
        # Included
        res['change'].add((loc_start, loc_length))
        return res
    # Need to split
    if loc_start < src:
        new_l = src - loc_start
        res['no_change'].add((loc_start, new_l))
    if loc_start <= src + l:
        new_l = (src + l) - loc_start + 1
        res['change'].add((loc_start, new_l))
    if loc_start + loc_length > src + l:
        new_l = loc_start + loc_length - (src + l)
        res['no_change'].add((loc_start, new_l))
    return res


def part2(filename):
    scan = get_lines(filename)
    seeds = [int(n.strip()) for n in scan[0].split(':')[1].split()]
    seeds = [tuple(seeds[i:i+2]) for i in range(0, len(seeds), 2)] # pairs of [[(seed, length)],...]
    mappings = defaultdict(list)
    scan = scan[2:]
    start = True
    for i in range(len(scan)):
        if scan[i].strip() == '':
            start = True
            continue
        if start:
            nl = re.match(r'([^-]+)-to-([^ ]+)', scan[i])
            if not nl:
                raise Exception(f'{scan[i]} not matched')
            c1, c2 = nl[1], nl[2]
            start = False
            continue
        numbers = [int(n.strip()) for n in scan[i].split()]
        mappings[c1].append((c2, numbers))
    new_mappings = dict()
    # Sort mappings for easier handling
    for curr_map, mps in mappings.items():
        new_mps = sorted(mps, key=lambda m: m[1][1])
        new_mappings[curr_map] = (mps[0][0], [m[1] for m in new_mps])
        first_mapping_start = new_mappings[curr_map][1][0][1]
        # Insert fake mapping at the beginning
        if first_mapping_start > 0:
            new_mappings[curr_map][1].insert(0, [0, 0, first_mapping_start])
        # Insert fake mapping at the end
        last_mapping_start = new_mappings[curr_map][1][-1][1]
        last_mapping_length = new_mappings[curr_map][1][-1][2]
        last_mapping_end = last_mapping_start + last_mapping_length
        new_mappings[curr_map][1].append([last_mapping_end, last_mapping_end, 99999999999999999])
    # pprint(seeds)
    # pprint(new_mappings)
    # log('')

    # Each seed will generate new ranges
    locations = [[s] for s in seeds]
    min_pos = 99999999999999999
    for i in range(len(locations)):
        curr_map = 'seed'
        log(f'* Current location {locations[i]}')
        curr_locations = locations[i]
        next_locations = []
        while curr_map != 'location':
            log(f'** Current map: "{curr_map}", original seed {locations[i]}')
            # process each seed location
            for loc_start, loc_length in curr_locations:
                loc_end = loc_start + loc_length - 1
                log(f'*** Current location: "{loc_start}, {loc_end}, {loc_length}"')
                # process each range
                nxt_start = loc_start
                for map_dst_start, map_start, map_length in new_mappings[curr_map][1]:
                    # For each range of each location
                    map_end = map_start + map_length - 1
                    log(f'Processing {loc_start}-{loc_end}, {loc_length} in "{curr_map}" mapping -> {map_dst_start}, {map_start}, {map_length}')
                    if nxt_start <= map_end:
                        offset = map_start - map_dst_start
                        nxt_start_with_offset = nxt_start - offset
                        log(f'Adding {(nxt_start_with_offset, min(map_end, loc_end) - nxt_start + 1)}. nxt_locations: {next_locations}')
                        next_locations.append((nxt_start_with_offset, min(map_end, loc_end) - nxt_start + 1))
                        nxt_start = map_end + 1
                        if loc_end <= map_end:
                            break

            curr_locations = next_locations[:]
            next_locations = []
            curr_map = new_mappings[curr_map][0]
            log(f'## next map: {curr_map}, next locations: {curr_locations}\n')
        curr_min = min(p1 for p1, p2 in curr_locations)
        log(f'** Next ranges for "{curr_map}" -> "{curr_min}"')
        log('')
        min_pos = min(curr_min, min_pos)

    log(f'Min pos: {min_pos}')
    return min_pos

class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(35, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(579439039, part1('input.txt'))

class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(46, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))

# 248892167 too high