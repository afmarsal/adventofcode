import util


class Node:
    nodes = {}

    @staticmethod
    def get_node(color):
        return Node.nodes[color] if color in Node.nodes else Node(color)

    def __init__(self, color) -> None:
        self.color = color
        self.children = []
        self.parents = []
        self.nodes[color] = self
        # print(f'New node: {color}')

    def add(self, child_name, qty):
        self.children.append((child_name, qty))
        Node.get_node(child_name).parents.append((self.color, qty))

    def distinct_parents(self):
        return {p[0] for p in self.parents}.union(*(Node.nodes[p[0]].distinct_parents() for p in self.parents))


def do_it(filename):
    for line in util.lines(filename):
        split = line.split()
        n = Node.get_node(''.join(split[0:2]))
        for inner in range(4, len(split), 4):
            if split[inner] != "no":
                n.add(''.join(split[inner + 1:inner + 3]), int(split[inner]))

    return len(Node.nodes['shinygold'].distinct_parents())


if __name__ == '__main__':
    output = do_it('input71.txt')
    print(f'Result: {output}')

# Result: 337
