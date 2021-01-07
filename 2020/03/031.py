with open("input031.txt") as f:
    # wood is a list of strings, where each tree can be referenced as wood[row][col]
    wood = list(map(str.strip, f))
    # Enumerate the rows using delta X (dx) as step. Then count positions equal to '#' using delta Y (dy)
    count_trees = lambda dy, dx: sum(row[(i * dy) % len(row)] == '#' for i, row in enumerate(wood[::dx]))

    print(f'Part 1: {count_trees(3, 1)}')
    print(f'Part 2: {count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(5, 1) * count_trees(1, 2)}')

# Part 1: 178
# Part 2: 3045802500
