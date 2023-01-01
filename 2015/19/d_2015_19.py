import re
import unittest
from collections import defaultdict

MOLECULE = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArAr" \
           "CaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnF" \
           "ArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMg" \
           "ArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCa" \
           "SiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMg" \
           "ArCaF"

def log(param='', end='\n'):
    print(param, end=end)
    pass

def log_nolf(param):
    log(param, end='')

def read(filename):
    with open(filename) as f:
        transforms = defaultdict(list)
        for line in f.read().splitlines():
            k, v = line.split(' => ')
            transforms[k].append(v)
    return transforms

def calc(transforms, molecule, target_molecule=None):
    results = set()
    idx = 0
    while idx < len(molecule):
        for k, v in transforms.items():
            if molecule[idx:idx+len(k)] == k:
                for tr in v:
                    prefix = molecule[0:idx] if idx > 0 else ""
                    suffix = molecule[idx+len(k):]
                    result = prefix + tr + suffix
                    if len(result) > len(target_molecule):
                        continue
                    results.add(result)
                    if result == target_molecule:
                        return results
        idx += len(k)
    return results

def next_results(transforms, results, molecule):
    next_results = set()
    for r in results:
        next_results.update(calc(transforms, r, molecule))
    return next_results

def part1(filename, molecule):
    transforms = read(filename)
    return len(calc(transforms, molecule))

def part2(filename, init_molecule):
    # Reverse the process: from the target molecule try to apply
    # transformations in reverse order
    # Taking advantage of no "substrings" between input transformations, so no "smart"
    # transforms, just find and replace until reducing to 'e'
    transforms0 = read(filename)
    transforms = {}
    for k, v in transforms0.items():
        for t in v:
            transforms[t] = k
    log(f'{transforms}')
    steps = 0
    new_s = init_molecule
    while new_s != 'e':
        for frm, to in transforms.items():
            new_s, n = re.subn(frm, to, new_s)
            steps += n
    return steps

    # For sample input, need something smarter (and slower)

    # (molecule, idx, steps)
    # queue = []
    # for i in range(len(init_molecule)):
    #     queue.append((init_molecule, i, 0))
    # max_transform_size = max(len(k) for k, v in transforms.items())
    # while True:
    #     molecule, idx, steps = queue.pop()
    #     # log(f'mol: {molecule} at {idx} with steps: {steps}')
    #     # log(f'{molecule}[{idx}]')
    #     for frm, to in transforms.items():
    #         # log(f'transform: {frm}:{to}')
    #         if to == target and frm == molecule:
    #             return steps + 1
    #         if idx + len(frm) > len(molecule):
    #             # log(f'Discarding transform: {frm}:{to} because exceeding size')
    #             continue
    #         if molecule[idx:idx+len(frm)] == frm:
    #             if to == target:
    #                 # log(f'Found invalid transform: {frm}:{to} at idx {molecule}[{idx}]')
    #                 continue
    #             # Queue up a transformation
    #             new_molecule = (molecule[0:idx] if idx > 0 else "") + to + molecule[idx + len(frm):]
    #             # log(f'Found match {molecule}[{idx}:{idx+len(frm)}] -> {to}. Queueing: {new_molecule}')
    #             max_idx = max(idx - max_transform_size + 1, 0)
    #             log(f'Found match [{idx}:{idx+len(frm)}] -> {to}. Queueing at {max_idx}, len: {len(new_molecule)}')
    #             queue.append((new_molecule, max_idx, steps + 1))
    #     queue.insert(0, (molecule, idx+1, steps))




class TestPart1(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(4, part1('sample1.txt', 'HOH'))

    def test_sample2(self):
        self.assertEqual(7, part1('sample1.txt', 'HOHOHO'))

    def test_input1(self):
        self.assertEqual(535, part1('input.txt', MOLECULE))

class TestPart2(unittest.TestCase):
    def test_sample1(self):
        self.assertEqual(3, part2('sample2.txt', 'HOH'))

    def test_sample2(self):
        self.assertEqual(6, part2('sample2.txt', 'HOHOHO'))

    def test_input(self):
        self.assertEqual(212, part2('input.txt', MOLECULE))
