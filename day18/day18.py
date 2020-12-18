import operator

filename = "./input/input.txt"

def process_line(line):
    ops = {
        "+": operator.add,
        "*": operator.mul,
    }

    stack = []
    parentheses = 0
    accumulated_result = 0
    op = None

    i = -1

    while i < len(line) - 1:
        i += 1
        ch = line[i]
        if ch == ' ':
            continue

        if ch.isdigit() and accumulated_result == 0:
            accumulated_result = int(ch)
            continue
        elif ch.isdigit() and accumulated_result != 0:
            assert op
            op_func =  ops[op]
            accumulated_result = op_func(accumulated_result, int(ch))
            op = None
            continue

        if ch == '*' or ch == '+':
            op = ch
            continue

        if ch == '(':
            parentheses += 1
            if accumulated_result > 0:
                stack.append(accumulated_result)
                stack.append(op)
            else:
                stack.append('noop')

            accumulated_result = 0
            op = None
            continue

        if ch == ')':
            parentheses -= 1
            if parentheses == 0:
                while stack:
                    element = stack.pop()
                    if element == '+' or element == '*':
                        op_func = ops[element]
                    elif isinstance(element, int):
                        accumulated_result = op_func(accumulated_result, element)
            elif parentheses > 0 and stack:
                op = stack.pop()
                if op != 'noop':
                    op_func = ops[op]
                    operand = stack.pop()
                    accumulated_result = op_func(accumulated_result, operand)
            
            continue
    
    return accumulated_result


def process_line_part2(line):
    line = line.replace(" ", "")
    i = 0

    accumulated_result = 0
    stack = []

    while i < len(line):
        ch = line[i]

        if ch.isdigit() and accumulated_result == 0:
            accumulated_result = int(ch)
            i += 1
            continue
        
        if ch == '*':
            stack.append(accumulated_result)
            accumulated_result = 0
            i += 1
            continue
        elif ch == '+':
            if line[i+1].isdigit():
                accumulated_result += int(line[i+1])
                i += 2
                continue
            else:
                i += 1
                continue

        if ch == '(':
            j = i + 1
            parentheses = 1
            while parentheses != 0:
                if line[j] == "(":
                    parentheses += 1
                if line[j] == ")":
                    parentheses -= 1
                j += 1
            
            accumulated_result += process_line_part2(line[i+1: j-1])
            i = j

    while stack:
        accumulated_result *= stack.pop()
    return accumulated_result

def solution_part1(filename):
    result_part1 = result_part2 = 0

    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            result_part1 += process_line(line)
            result_part2 += process_line_part2(line)
    return result_part1, result_part2


part1, part2 = solution_part1(filename)
print(part1)
print(part2)