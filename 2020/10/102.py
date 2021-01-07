from functools import lru_cache


class Graph:

    def __init__(self, ints) -> None:
        super().__init__()
        self.ints = ints
        self.precalc = {}

    def next_nodes(self, idx):
        return [i for i in range(idx + 1, min(idx + 4, len(self.ints))) if self.ints[i] - self.ints[idx] <= 3]

    def count_paths(self, idx, curr_paths):
        if idx == len(self.ints) - 1:
            return curr_paths + 1

        if idx in self.precalc:
            return self.precalc[idx]
        for next_node in self.next_nodes(idx):
            self.precalc[next_node] = self.count_paths(next_node, curr_paths)
            curr_paths += self.precalc[next_node]
        return curr_paths


@lru_cache(None)
def arrangements(jolts, prev) -> int:
    """The number of arrangements that go from prev to the end of `jolts`."""
    first, rest = jolts[0], jolts[1:]
    if first - prev > 3:
        return 0
    elif not rest:
        return 1
    else:
        return (arrangements(rest, first) +  # Use first
                arrangements(rest, prev))    # Skip first


def do_it(filename):
    with open(filename) as f:
        ints = sorted(list(map(int, f)))
        # ints = [0] + ints + [max(ints) + 3]
    return arrangements(tuple(ints), 0)


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 10578455953408
