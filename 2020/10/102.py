
class Graph:

    def __init__(self, ints) -> None:
        super().__init__()
        self.ints = ints
        self.precalc = {}

    def next_nodes(self, idx):
        next_idx = []
        for i in range(idx + 1, min(idx + 4, len(self.ints))):
            if self.ints[i] - self.ints[idx] <= 3:
                next_idx.append(i)
        return next_idx

    def count_paths(self, idx0, curr_paths):
        if idx0 == len(self.ints) - 1:
            return curr_paths + 1

        if idx0 in self.precalc:
            return self.precalc[idx0]
        for n in self.next_nodes(idx0):
            child_paths = self.count_paths(n, curr_paths)
            self.precalc[n] = child_paths
            curr_paths += self.precalc[n]
        return curr_paths


def do_it(filename):
    with open(filename) as f:
        ints = sorted(list(map(int, f)))
        ints.insert(0, 0)
        ints.append(max(ints) + 3)
    graph = Graph(ints)
    return graph.count_paths(0, 0)


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 10578455953408
