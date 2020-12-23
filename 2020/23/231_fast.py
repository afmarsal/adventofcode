def do_it(lst):
    size = len(lst)
    next_lst = lst.copy()
    pickup = [0] * 3
    for i in range(100):
        curr_idx = 0
        curr = lst[curr_idx]
        print(f'-- Move {i + 1} --')
        print(f'curr = {curr}, cups: {lst}')
        for j in range(3):
            pickup[j] = lst[(curr_idx + j + 1) % len(lst)]
        print(f'pick up: {pickup}')

        # Choose destination
        dest = (curr - 1) % size
        dest = (dest, size)[dest == 0]
        while dest in pickup:
            dest = (dest - 1) % size
            dest = (dest, size)[dest == 0]
        print(f'dest: {dest}')

        ins_idx = lst.index(dest) + 1 % size
        # copy the list to another in 3 "regions":
        # 1: after pickup until insert point
        # 2: pickup
        # 3: the rest
        # any of them may hit end of buffer
        # 1st
        write_idx = 0
        start_pickup = curr_idx + 1 % size
        end_pickup = curr_idx + 4 % size
        if end_pickup < ins_idx:
            chunk_size = ins_idx - end_pickup
            next_lst[write_idx:chunk_size] = lst[end_pickup:ins_idx]
            write_idx = chunk_size
        else:
            chunk_size = lst(lst) - end_pickup
            next_lst[0:chunk_size] = lst[end_pickup:]
            write_idx = chunk_size + 1
            chunk_size = ins_idx
            next_lst[write_idx:write_idx + chunk_size] = lst[:ins_idx]
            write_idx += chunk_size
        # 2nd
        if start_pickup > end_pickup:
            raise Exception("Not handled")
        else:
            next_lst[write_idx:write_idx + len(pickup)] = pickup
            write_idx += len(pickup)
        # 3rd
        if ins_idx < start_pickup:
            chunk_size = curr_idx - ins_idx + 1
            next_lst[write_idx:write_idx + chunk_size] = lst[ins_idx:curr_idx]
        else:
            chunk_size = len(lst) - ins_idx
            next_lst[write_idx:write_idx + chunk_size] = lst[ins_idx:len(lst)]
            write_idx += chunk_size
            next_lst[write_idx:] = lst[:curr_idx+1]

        lst, next_lst = next_lst, lst

    print('-- final --')
    curr = int(lst[0])
    print(f'curr = {curr}, cups: {lst}')
    one_idx = lst.index(1)
    if one_idx == len(lst) - 1:
        result = lst[:len(lst) - 1]
    else:
        result = lst[one_idx + 1:] + lst[0:one_idx]
    print(result)
    return ''.join([str(n) for n in result])


if __name__ == '__main__':
    # s = list(map(int, '389125467'))
    s = list(map(int, '792845136'))
    output = do_it(s)
    print(f'Part 1: {output}')

# Part 1: 98742365
