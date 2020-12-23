def do_it(lst):
    idx = 0
    size = len(lst)
    for i in range(100):
        print(f'-- Move {i + 1} --')
        curr = int(lst[idx])
        print(f'curr = {curr}, cups: {lst}')
        sel = []
        for j in range(3):
            sel.append(lst[(idx + j + 1) % len(lst)])
        lst = [l for l in lst if l not in sel]
        print(f'pick up: {sel}')

        # Choose destination
        dest = (curr - 1) % size
        dest = (dest, size)[dest == 0]
        while dest not in lst:
            dest = (dest - 1) % size
            dest = (dest, size)[dest == 0]
        print(f'dest: {dest}')

        ins_idx = lst.index(dest) + 1
        if ins_idx == len(lst):
            lst.extend(sel)
        else:
            lst[ins_idx:ins_idx] = sel

        idx = (lst.index(curr) + 1) % len(lst)

    print('-- final --')
    curr = int(lst[idx])
    print(f'curr = {curr}, cups: {lst}')
    one_idx = lst.index(1)
    result = []
    if one_idx == len(lst) - 1:
        result = lst[:len(lst)-1]
    else:
        result = lst[one_idx+1:] + lst[0:one_idx]
    print(result)
    return ''.join([str(n) for n in result])


if __name__ == '__main__':
    # s = list(map(int, '389125467'))
    s = list(map(int, '792845136'))
    output = do_it(s)
    print(f'Part 1: {output}')

# Part 1:
# too high: 987423651