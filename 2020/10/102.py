
class Graph:

    def __init__(self, ints) -> None:
        super().__init__()
        self.total_paths = 0
        self.ints = ints
        self.precalc = {}

    def next_nodes(self, idx):
        next_idx = []
        for i in range(idx + 1, min(idx + 4, len(self.ints))):
            if self.ints[i] - self.ints[idx] <= 3:
                next_idx.append(i)
        return next_idx

    def count_paths(self, idx0):
        if idx0 == len(self.ints) - 1:
            self.total_paths += 1

        for n in self.next_nodes(idx0):
            # print(f'Child node ints[{n}]={self.ints[n]}')
            self.count_paths(n)


def do_it(filename):
    with open(filename) as f:
        ints = sorted(list(map(int, f)))
        ints.insert(0, 0)
        ints.append(max(ints) + 3)
    print(ints)
    graph = Graph(ints)
    graph.count_paths(0)
    return graph.total_paths


if __name__ == '__main__':
    output = do_it('input1.txt')
    print(f'Result: {output}')

# Result: 1904
