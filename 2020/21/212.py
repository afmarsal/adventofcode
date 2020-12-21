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

    sorted_data = [(list(i)[0], a) for a, i in results.items() if len(i) == 1]
    unique = {s[0] for s in sorted_data}
    while len(unique) < len(all_allergens):
        for a, i in results.items():
            i.difference_update(unique)
            if len(i) == 1:
                unique_ing = list(i)[0]
                unique.add(unique_ing)
                sorted_data.append((unique_ing, a))

    sorted_data.sort(key=lambda x: x[1])
    return ','.join([s[0] for s in sorted_data])


if __name__ == '__main__':
    with open('input1.txt') as f:
        lines = list(map(str.strip, f))

    output = do_it(lines)
    print(f'Part 2: {output}')

# Part 1: xxscc,mjmqst,gzxnc,vvqj,trnnvn,gbcjqbm,dllbjr,nckqzsg
