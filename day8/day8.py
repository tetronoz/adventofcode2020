filename = "./input/input.txt"



def process_input(filename):
    with open(filename) as fp:
        instructions = [line.strip() for line in fp]
    return instructions

def parse_instruction(instr_line):
    instr, offset = instr_line.split()
    operation = offset[0]
    offset = offset[1:]

    return instr, operation, offset

def execute_instruction(instr, operation, offset, acc, inst_idx):
    if instr == 'nop':
        inst_idx += 1
    elif instr == 'acc':
        if operation == '+':
            acc += offset
        elif operation == '-':
            acc -= offset
        inst_idx += 1
    elif instr == 'jmp':
        if operation == '+':
            inst_idx += offset
        elif operation == '-':
            inst_idx -= offset
    return inst_idx, acc

def find_loop(instructions):
    acc = 0
    inst_idx = 0
    visited = set()

    while True:
        if inst_idx in visited:
            break
        else:
            visited.add(inst_idx)
            instr, operation, offset = parse_instruction(instructions[inst_idx])
            offset = int(offset)

            inst_idx, acc = execute_instruction(instr, operation, offset, acc, inst_idx)

    return acc

def fix_loop(instructions):
    acc = 0
    inst_idx = 0
    visited = set()

    while inst_idx < len(instructions):
        if inst_idx in visited:
            return None
        else:
            visited.add(inst_idx)
            instr, operation, offset = parse_instruction(instructions[inst_idx])
            offset = int(offset)
            inst_idx, acc = execute_instruction(instr, operation, offset, acc, inst_idx)

    print(acc)
    return True

data = process_input(filename)
print(find_loop(data))

#replace nop
for idx, line in enumerate(data):
    if line.startswith("nop"):
        data_copy = data[:]
        data_copy[idx] = data_copy[idx].replace('nop', 'jmp')
        if fix_loop(data_copy):
            break

#replace jmp
for idx, line in enumerate(data):
    if line.startswith("jmp"):
        data_copy = data[:]
        data_copy[idx] = data_copy[idx].replace('jmp', 'nop')
        if fix_loop(data_copy):
            break