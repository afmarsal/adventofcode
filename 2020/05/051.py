with open('input51.txt') as f:
    # Use str.maketrans to bulk replace 'F', 'L', 'B' and 'R` to 0's and 1's, and the convert
    # to int using base=2
    line_to_int = lambda s: int(s.strip().translate(str.maketrans('FLBR', '0011')), base=2)
    ids = list(map(line_to_int, f))
    print(f'Part 1: {max(ids)}')
    # Front and back missing means highest and lowest ids missing. Create a range from min to ma
    # and remove the existing ones to get he missing one
    print(f'Part 1: {set(range(min(ids), max(ids))) - set(ids)}')

# Part 1: 991
# Part 1: {534}
