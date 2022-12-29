import copy
import dataclasses
import re
import unittest

ROBOT_TYPES = {'ore', 'clay', 'obs', 'geode'}

def robot_types():
    return copy.copy(ROBOT_TYPES)

def read(filename):
    with open(filename) as f:
        blueprints = {}

        for line in f.read().splitlines():
            blueprint, *prices = list(map(int, re.findall(r'\d+', line)))
            blueprints[blueprint] = {'ore': {'ore': prices[0]},
                                     'clay': {'ore': prices[1]},
                                     'obs': {'ore': prices[2], 'clay': prices[3]},
                                     'geode': {'ore': prices[4], 'obs': prices[5]}}
    return blueprints

@dataclasses.dataclass
class PathInfo:
    # { 'ore': 3, 'clay': 2
    robots: dict
    # { 'ore': 3, 'clay': 2, 'obs': 5 }
    balances: dict
    # What robots are allowed to buy
    allowed: set  = dataclasses.field(default_factory=robot_types)

    def increase_balances(self):
        # Increase robot balances
        for robot, count in self.robots.items():
            self.balances[robot] = self.balances.get(robot, 0) + count

    def decrease_balances(self, costs):
        for resource, price in costs.items():
            self.balances[resource] -= price

@dataclasses.dataclass
class BlueprintInfo:
    paths: list

def log(param='', end='\n'):
    # print(param, end=end)
    pass


def log_nolf(param):
    log(param, end='')


def can_buy(robot_costs, balances):
    for resource, price in robot_costs.items():
        balance = balances.get(resource, 0)
        if balance < price:
            return False
    return True


def should_keep_path(prices, path):
    ore_balance = path.balances.get('ore', 0)
    clay_balance = path.balances.get('clay', 0)
    obs_balance = path.balances.get('obs', 0)
    match len(path.robots):
        case 1:  # Only ore generator robot
            if ore_balance >= max(prices['ore']['ore'], prices['clay']['ore']):
                log(f'Useless path for ore {path}')
                return False
        case 2:  # ore & clay
            if ore_balance >= max(prices['ore']['ore'], prices['clay']['ore'])\
                    and clay_balance >= prices['obs']['clay']:
                log(f'Useless path for clay {path}')
                return False
        case 3:  # ore & clay & obsidian
            if ore_balance >= max(prices['ore']['ore'], prices['clay']['ore'])\
                    and clay_balance >= prices['obs']['clay']\
                    and obs_balance >= prices['geode']['obs']:
                log(f'Useless path for obsidian {path}')
                return False
    return True


def is_worse(new_path, paths):
    for path in paths:
        # same or less robots
        worse_robots = all(path.robots.get(new_robot, 0) >= new_amount for new_robot, new_amount in new_path.robots.items())
        if worse_robots:
            log(f'Found better robots for {new_path} in paths:{paths}')
        else:
            return False
        worse_balances = all(path.balances.get(new_resource, 0) >= new_amount for new_resource, new_amount in new_path.balances.items())
        if worse_balances:
            log(f'Found better resrouces for {new_path} in paths:{paths}')
        else:
            return False
    return True


def part1(filename):
    blueprint_prices = read(filename)
    log(blueprint_prices)
    minutes = 24
    paths_by_blueprint = {b: BlueprintInfo([PathInfo({'ore': 1}, {})]) for b in blueprint_prices.keys()}
    # paths_by_blueprint = {1: BlueprintInfo([PathInfo({'ore': 1}, {})])}
    for minute in range(1, minutes+1):
        log(f'\n**** Minute: {minute}')
        for blueprint, blueprint_info in paths_by_blueprint.items():
            log(f'** Blueprint: {blueprint}')
            next_paths = []
            next_paths_filtered = []
            max_obs = max(path.balances.get('obs', 0) for path in blueprint_info.paths)
            max_geodes = max(path.balances.get('geode', 0) for path in blueprint_info.paths)
            for path_idx, path in enumerate(blueprint_info.paths):
                log(f'BP: {blueprint}, path {path_idx}: {path}')
                if path.balances.get('geode', 0) < max_geodes - 2:
                    log(f'Discard path (less than {max_geodes} geodes): {path}')
                    continue
                if 'geode' not in path.robots and path.balances.get('obs', 0) < max_obs - 2:
                    log(f'Discard path (less than {max_obs} obs): {path}')
                    continue

                # Try to buy
                for robot in ROBOT_TYPES:
                    if robot not in path.allowed:
                        # log(f'Can\'t buy: {robot}')
                        continue
                    robot_costs = blueprint_prices[blueprint][robot]
                    if can_buy(robot_costs, path.balances):
                        # buy
                        new_path = copy.deepcopy(path)
                        new_path.decrease_balances(robot_costs)
                        new_path.allowed = robot_types()
                        new_path.increase_balances()
                        new_path.robots[robot] = new_path.robots.get(robot, 0) + 1
                        next_paths.append(new_path)
                        path.allowed.remove(robot)
                        log(f'Bought {robot}. Adding path: {len(next_paths) - 1} -> {next_paths[-1]}')
                    # else:
                    #     log(f'Cant buy {robot} for {path}')

                # Discard after buying if more balances than required
                if not should_keep_path(blueprint_prices[blueprint], path):
                    log(f'Discard path 1: {path}')
                    continue
                path.increase_balances()
                next_paths.append(path)
                log(f'Keep path: {path_idx} -> {path}')

            paths_by_blueprint[blueprint].paths = next_paths_filtered if len(next_paths_filtered) > 0 else next_paths

            log(f'\nPaths for blueprint {blueprint}')
            for path_idx, p in enumerate(paths_by_blueprint[blueprint].paths):
                log(f'{path_idx}: {p}')

        # if minute == 10:
        #     break

    max_per_blueprint = {}
    for blueprint, blueprint_info in paths_by_blueprint.items():
        max_per_blueprint[blueprint] = max(path.balances.get('geode', 0) for path in blueprint_info.paths)
    print(max_per_blueprint)
    return sum(b * v for b, v in max_per_blueprint.items())


def part2(filename):
    return -1


class TestPart1(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(33, part1('sample.txt'))

    def test_input(self):
        self.assertEqual(1466, part1('input.txt'))


class TestPart2(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(-2, part2('sample.txt'))

    def test_input(self):
        self.assertEqual(-2, part2('input.txt'))
