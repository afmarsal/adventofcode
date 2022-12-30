import copy
import dataclasses
import re
import sys
import unittest
from collections import defaultdict
from functools import reduce

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
MAX = 4

ROBOT_TYPES = {ORE, CLAY, OBSIDIAN, GEODE}

ROBOT_STR = ['ore', 'clay', 'obs', 'geode']

BUFF_SIZE = 10000000

def robot_types():
    return copy.copy(ROBOT_TYPES)

def read(filename):
    with open(filename) as f:
        blueprints = {}

        for line in f.read().splitlines():
            blueprint, *prices = list(map(int, re.findall(r'\d+', line)))
            blueprints[blueprint] = {ORE: {ORE: prices[0]},
                                     CLAY: {ORE: prices[1]},
                                     OBSIDIAN: {ORE: prices[2], CLAY: prices[3]},
                                     GEODE: {ORE: prices[4], OBSIDIAN: prices[5]},
                                     # No need to have more than these amount of robots
                                     MAX: [prices[0] + prices[1] + prices[2] + prices[4],
                                           prices[3],
                                           prices[5],
                                           sys.maxsize]}
    return blueprints

@dataclasses.dataclass
class PathInfo:

    def __init__(self) -> None:
        # start with 1 of ORE
        self.robots = [1, 0, 0, 0]
        # and 0 for balance
        self.balances = [0] * 4
        self.allowed = copy.copy(ROBOT_TYPES)

    # ORE: 3, CLAY: 2
    robots: list
    # { ORE: 3, CLAY: 2, OBSIDIAN: 5 }
    balances: list
    # What robots are allowed to buy
    allowed: set

    def increase_balances(self):
        # Increase robot balances
        for robot, count in enumerate(self.robots):
            self.balances[robot] += count

    def decrease_balances(self, costs):
        for resource, price in costs.items():
            self.balances[resource] -= price

@dataclasses.dataclass
class BlueprintInfo:
    def __init__(self, pi) -> None:
        self.paths = [None] * BUFF_SIZE
        self.paths[0] = pi
        self.size = 1
        self.max_geodes = 0
        self.max_obsidian = 0

    paths: list
    size: int
    max_geodes: int
    max_obsidian: int

def log(param='', end='\n'):
    # print(param, end=end)
    pass


def log_nolf(param):
    log(param, end='')


def can_buy(robot, prices, path):
    if path.robots[robot] >= prices[MAX][robot]:
        return False
    return all(path.balances[resource] >= price for resource, price in prices[robot].items())

def should_keep_path(prices, path):
    ore_balance = path.balances[ORE]
    clay_balance = path.balances[CLAY]
    obs_balance = path.balances[OBSIDIAN]
    match len(path.robots):
        case 1:  # Only ore generator robot
            if ore_balance >= max(prices[ORE][ORE], prices[CLAY][ORE]):
                log(f'Useless path for ore {path}')
                return False
        case 2:  # ore & clay
            if ore_balance >= max(prices[ORE][ORE], prices[CLAY][ORE])\
                    and clay_balance >= prices[OBSIDIAN][CLAY]:
                log(f'Useless path for clay {path}')
                return False
        case 3:  # ore & clay & obsidian
            if ore_balance >= max(prices[ORE][ORE], prices[CLAY][ORE])\
                    and clay_balance >= prices[OBSIDIAN][CLAY]\
                    and obs_balance >= prices[GEODE][OBSIDIAN]:
                log(f'Useless path for obsidian {path}')
                return False
    return True


def for_cache(path):
    return tuple(path.robots), tuple(path.balances)


def calc(blueprint_prices, minutes):
    paths_by_blueprint = {b: BlueprintInfo(PathInfo()) for b in blueprint_prices.keys()}
    # paths_by_blueprint = {1: BlueprintInfo([PathInfo()])}
    blueprint_cache = defaultdict(set)
    buff, idx = [None] * 10000000, 0
    idx = 0
    for minute in range(1, minutes+1):
        log(f'\n\n**** Minute: {minute}')
        for blueprint, blueprint_info in paths_by_blueprint.items():
            log(f'\n** Blueprint: {blueprint}')
            max_obs, max_geodes = 0, 0
            for path_idx in range(paths_by_blueprint[blueprint].size):
                path = paths_by_blueprint[blueprint].paths[path_idx]
                max_obs = max(max_obs, path.balances[OBSIDIAN])
                max_geodes = max(max_geodes, path.balances[GEODE])
            for path_idx in range(paths_by_blueprint[blueprint].size):
                path = paths_by_blueprint[blueprint].paths[path_idx]
                if for_cache(path) in blueprint_cache.get(blueprint, set()):
                    log(f'Path {path} cached. Continuing...')
                    continue
                blueprint_cache[blueprint].add(for_cache(path))
                log(f'BP: {blueprint}, path {path_idx}: {path}')
                if path.balances[GEODE] < max_geodes - 2:
                    log(f'Discard path (less than {max_geodes} geodes): {path}')
                    continue
                # if path.robots[GEODE] == 0 and path.balances[OBSIDIAN] < max_obs - 3:
                #     log(f'Discard path (less than {max_obs} obs): {path}')
                #     continue

                # Try to buy
                if minute < minutes:
                    for robot in ROBOT_TYPES:
                        if minute == minutes - 1 and robot != GEODE:
                            continue
                        if robot not in path.allowed:
                            # log(f'Can\'t buy: {robot}')
                            continue
                        robot_costs = blueprint_prices[blueprint][robot]
                        if can_buy(robot, blueprint_prices[blueprint], path):
                            # buy
                            new_path = copy.deepcopy(path)
                            new_path.decrease_balances(robot_costs)
                            new_path.allowed = robot_types()
                            new_path.increase_balances()
                            new_path.robots[robot] += 1
                            buff[idx] = new_path
                            idx += 1
                            new_path.max_geodes = max(max_geodes, path.balances[GEODE])
                            path.allowed.remove(robot)
                            log(f'Bought {ROBOT_STR[robot]}. Adding path: {idx - 1} -> {buff[idx - 1]}')
                        # else:
                        #     log(f'Cant buy {robot} for {path}')

                # Discard after buying if more balances than required
                if not should_keep_path(blueprint_prices[blueprint], path):
                    log(f'Discard path 1: {path}')
                    continue
                path.increase_balances()
                buff[idx] = path
                idx += 1
                path.max_geodes = max(max_geodes, path.balances[GEODE])
                log(f'Keep path: {path_idx} -> {path}')

            paths_by_blueprint[blueprint].paths, buff = buff, paths_by_blueprint[blueprint].paths
            paths_by_blueprint[blueprint].size, idx = idx, 0

            log(f'Paths for blueprint {blueprint} (size: {paths_by_blueprint[blueprint].size})')
            for path_idx in range(paths_by_blueprint[blueprint].size):
                log(f'{path_idx}: {paths_by_blueprint[blueprint].paths[path_idx]}')

        print(f'Minute {minute}')

    max_per_blueprint = {}
    for blueprint, blueprint_info in paths_by_blueprint.items():
        max_per_blueprint[blueprint] = max(blueprint_info.paths[i].balances[GEODE] for i in range(blueprint_info.size))
    return max_per_blueprint

def part1(filename):
    blueprint_prices = read(filename)
    minutes = 24
    max_per_blueprint = calc(blueprint_prices, minutes)
    return sum(b * v for b, v in max_per_blueprint.items())


def part2(filename):
    blueprint_prices = read(filename)
    new_blueprint_prices = {k: v for k, v in blueprint_prices.items() if k <= 3}
    minutes = 32
    log(f'{new_blueprint_prices}')
    max_per_blueprint = calc(new_blueprint_prices, minutes)
    print(f'{max_per_blueprint}')
    return reduce(lambda x, y: x * y, max_per_blueprint.values())


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(33, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1466, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(3472, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(8250, part2('input.txt'))
