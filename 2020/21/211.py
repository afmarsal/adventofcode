from functools import reduce


def do_it(lines):
    data = []
    all_ingredients = set()
    all_allergens = set()
    for line in lines:
        ingredients = set(line.split('(contains ')[0].strip().split())
        allergens = set(line.split('(contains ')[1].strip()[:-1].split(", "))
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)
        data.append((ingredients, allergens))

    results = dict()
    for allergen in all_allergens:
        results[allergen] = set()
        first = True
        for ingredients, allergens in data:
            if allergen in allergens:
                if first:
                    results[allergen] = set(ingredients)
                    first = False
                else:
                    results[allergen] &= ingredients
        print(f'{allergen} -> {results[allergen]}')

    contaminated = {a for s in results.values() for a in s}
    return sum(len(ingredients - contaminated) for ingredients, allergens in data)


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 1: {output}')

# Part 1: 1958
