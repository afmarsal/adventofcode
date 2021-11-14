import unittest
from collections import defaultdict

MOLECULE = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArAr" \
           "CaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnF" \
           "ArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMg" \
           "ArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCa" \
           "SiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMg" \
           "ArCaF "


def part1(lines, molecule):
    transforms = defaultdict(list)
    for line in lines:
        k, v = line.split(' => ')
        transforms[k].append(v)
    results = set()
    idx = 0
    while idx < len(molecule):
        for k, v in transforms.items():
            if molecule[idx:idx+len(k)] == k:
                for tr in v:
                    prefix = molecule[0:idx] if idx > 0 else ""
                    suffix = molecule[idx+len(k):]
                    result = prefix + tr + suffix
                    results.add(result)
        idx += len(k)

    return len(results)


class TestPart1(unittest.TestCase):
    def test_sample1(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(4, part1(lines, 'HOH'))

    def test_sample2(self):
        with open('input0.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(7, part1(lines, 'HOHOHO'))

    def test_input1(self):
        with open('input_part1.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(535, part1(lines, MOLECULE))
