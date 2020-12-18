import operator

OPERATORS = {'+': operator.add, '*': operator.mul}
WAITING_OPERAND_1 = 'waiting1'
WAITING_OPERATOR = 'waiting2'
WAITING_OPERAND_2 = 'waitingOp'
DIGITS = (str(c) for c in range(10))


def process_token(stack, status, token):
    print(f'Processing {token}, {status}, {stack}')
    try:
        if status == WAITING_OPERAND_1:
            if token == '(':
                stack.append('(')
                return WAITING_OPERAND_1
            else:
                stack.append(int(token))
                return WAITING_OPERATOR

        elif status == WAITING_OPERATOR:
            if token == ')':
                curr = stack.pop()
                while stack[-1] != '(':
                    action = OPERATORS[stack.pop()]
                    operand1 = stack.pop()
                    curr = action(operand1, curr)
                stack[-1] = curr
                if len(stack) > 1 and stack[-2] == '+':
                    operand2 = stack.pop()
                    action = OPERATORS[stack.pop()]
                    operand1 = stack.pop()
                    stack.append(action(operand1, operand2))
                return WAITING_OPERATOR

            else:
                stack.append(token)
                return WAITING_OPERAND_2

        elif status == WAITING_OPERAND_2:
            if token[0] == '(':
                stack.append('(')
                return WAITING_OPERAND_1
            else:
                operand2 = int(token)
                if stack[-1] == '*':
                    stack.append(operand2)
                    return WAITING_OPERATOR
                else:
                    if stack[-1] != '+':
                        raise Exception('WAT 2!!')
                action = OPERATORS[stack.pop()]
                operand1 = stack.pop()
                stack.append(action(operand1, operand2))
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
    result = 1
    for i in range(0, len(stack), 2):
        result *= stack[i]

    return result


def do_it(lines):
    return sum(calc(line) for line in lines)


if __name__ == '__main__':
    with open('input0.txt') as f:
        filelines = list(map(str.strip, f))

    output = do_it(filelines)
    print(f'Part 2: {output}')


# Part 2: 201376568795521

