import util
from itertools import chain


class Node:
    nodes = {}

    @staticmethod
    def get_node(color):
        return Node.nodes[color] if color in Node.nodes else Node(color)
        # if color in Node.nodes:
        #     return Node.nodes[color]
        # else:
        #     return Node(color)

    def __init__(self, color) -> None:
        self.color = color
        self.children = []
        self.parents = []
        self.nodes[color] = self
        print(f'New node: {color}')

    def add(self, child_name, qty):
        self.children.append((child_name, qty))
        if child_name in Node.nodes:
            print(f'Adding {self.color} parent to existing node {child_name}: {qty}')
            child = Node.nodes[child_name]
        else:
            print(f'Adding {self.color} parent to new node {child_name}: {qty}')
            child = Node(child_name)
        child.parents.append((self.color, qty))

    def distinct_parents(self):
        i = len(self.parents)
        print(f'Recursing {self.color}: {i}')
        return {p[0] for p in self.parents}.union(*(Node.nodes[p[0]].distinct_parents() for p in self.parents))


def do_it(filename):
    for line in util.lines(filename):
        split = line.split()
        n = Node.get_node(split[0] + split[1])
        for inner in range(4, len(split), 4):
            if split[inner] != "no":
                n.add(split[inner + 1] + split[inner + 2], int(split[inner]))

    return len(Node.nodes['shinygold'].distinct_parents())


if __name__ == '__main__':
    output = do_it('input71.txt')
    print(f'Result: {output}')

# Result: 337
