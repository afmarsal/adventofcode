import unittest


def get_nums(filename):
    chunks = []
    with open(filename) as f:
        chunk = []
        for line in f.read().splitlines():
            if not line:
                chunks.append(chunk)
                chunk = []
            else:
                chunk.append(int(line))
        chunks.append(chunk)
    return chunks





def day1(chunks):
    return max([sum(chunk) for chunk in chunks])


def day2(chunks):
    return sum(sorted([sum(chunk) for chunk in chunks])[-3:])


if __name__ == '__main__':
    # chunks = get_nums('sample.txt')
    chunks = get_nums('input.txt')
    day1(chunks)
    day2(chunks)


class TestPart1(unittest.TestCase):
    def test0(self):
        nums = get_nums('sample.txt')
        self.assertEqual(day1(nums), 24000)

    def test1(self):
        nums = get_nums('input.txt')
        self.assertEqual(day1(nums), 69281)
