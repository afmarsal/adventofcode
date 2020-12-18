
WAITING_OPERAND_1 = 'waiting1'
WAITING_OPERATOR = 'waiting2'
WAITING_OPERAND_2 = 'waitingOp'


def resolve_top_stack(stack):
    res = eval(f'{stack.pop()} {stack.pop()} {stack.pop()}')
    stack.append(str(res))


def process_token(stack, status, token):
    print(f'Processing {token}, {status}, {stack}')
    try:
        if status == WAITING_OPERAND_1:
            stack.append(token)
            return WAITING_OPERAND_1 if token == '(' else WAITING_OPERATOR

        elif status == WAITING_OPERATOR:
            if token == ')':
                while stack[-2] != '(':
                    resolve_top_stack(stack)
                if stack[-2] != '(':
                    raise Exception('WAT!')
                # Replace '(' with eval'ed result at the top
                stack[-1] = stack.pop()
                if len(stack) > 1 and stack[-2] == '+':
                    resolve_top_stack(stack)
                return WAITING_OPERATOR

            else:
                stack.append(token)
                return WAITING_OPERAND_2

        elif status == WAITING_OPERAND_2:
            stack.append(token)
            if token == '(':
                return WAITING_OPERAND_1
            else:
                if stack[-2] == '*':
                    return WAITING_OPERATOR
                else:
                    if stack[-2] != '+':
                        raise Exception('WAT 2!!')
                    resolve_top_stack(stack)
                    return WAITING_OPERATOR
    finally:
        print(f'Processed {token}, {status}, {stack}')
        pass


def calc(line):
    print(line)
    stack = []
    status = WAITING_OPERAND_1
    for token in [c for word in line.split() for c in word]:
        status = process_token(stack, status, token)

    # List should contain only '*' operations
    return eval(''.join(stack))


def do_it(lines):
    return sum(calc(line) for line in lines)


if __name__ == '__main__':
    with open('input1.txt') as f:
        filelines = list(map(str.strip, f))

    output = do_it(filelines)
    print(f'Part 2: {output}')


# Part 2: 201376568795521

