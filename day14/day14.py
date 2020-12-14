import re
import sys

from collections import defaultdict
filename = "./input/input.txt"

pattern = re.compile(r"^mem\[(\d+)\]\s=\s(\d+)$")

def get_value_address(line):
    match = re.search(pattern, line)
    value = 0
    address = 0
    if match:
        address = int(match.group(1))
        value = int(match.group(2))
    else:
        print("FAILED")
        sys.exit(-1)
    
    return value, address

def apply_bitmask(value, mask):
    mask_off = int(mask.replace('X', '0'), 2)
    mask_on = int(mask.replace('X', '1'), 2)

    return (value | mask_off) & mask_on

def get_addresses(address, mask):
    zeros = 36 - len(address)
    full_address = ['0'] * zeros
    for v in address:
        full_address.append(v)
    
    X = []

    assert len(full_address) == 36
    assert len(mask) == 36

    for i in range(len(mask)):
        if mask[i] == '0':
            continue
        if mask[i] == 'X':
            X.append(i)
        full_address[i] = mask[i]
    
    if len(X) == 0:
        yield "".join(full_address)
    else:
        for v in range(2**len(X)):
            b = list(bin(v)[2:])
            candidate = ['0'] * (len(X) - len(b)) + b
            for i in range(len(X)):
                x_pos = X[i]
                full_address[x_pos] = candidate[i]
            yield "".join(full_address)


def sum_values_in_memory(filename):
    mask = None
    mem = {}
    mem2 = {}

    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if line.startswith("mask"):
                mask = line.split("=")[1].lstrip()
            else:
                value, address = get_value_address(line)
                mem[address] = apply_bitmask(value, mask)
                for addr in get_addresses(list(bin(address)[2:]), mask):
                    mem2[addr] = value
    
    return sum(mem.values()), sum(mem2.values())

print(sum_values_in_memory(filename))