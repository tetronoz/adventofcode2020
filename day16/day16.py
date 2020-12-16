filename = "./input/input.txt"

import re
import sys
from collections import defaultdict

pattern = "^(.*)\:\s(\d+)-(\d+)\sor\s(\d+)-(\d+)$"
compiled_pattern = re.compile(pattern)
rules = {}
range_nums = set()
valid_tickets = []

my_ticket = None

def parse_line(line):
    re_object = re.search(compiled_pattern, line)
    if re_object:
        rule_name = re_object.group(1)
        start1 = int(re_object.group(2))
        end1 = int(re_object.group(3))
        start2 = int(re_object.group(4))
        end2 = int(re_object.group(5))

        rules[rule_name] = [[start1, end1], [start2, end2]]
    else:
        print("FAILED")
        sys.exit(-1)

def build_rules(filename):
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if line == 'your ticket:':
                break
            if len(line) > 0:
                parse_line(line)

def build_range(rules):
    for values in rules.values():
        for el in values:
            for n in range(el[0], el[1] + 1):
                range_nums.add(n)

build_rules(filename)
build_range(rules)

def get_scanning_rate(filename):
    is_nearby_tickets = False
    is_my_ticket = False
    rate = 0
    my_ticket = None
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            if is_my_ticket:
                my_ticket = [int(x) for x in line.split(',')]
                is_my_ticket = False
            if is_nearby_tickets:
                nums = [int(x) for x in line.split(',')]
                is_valid_ticket = True
                for num in nums:
                    if num not in range_nums:
                        rate += num
                        is_valid_ticket = False
                if is_valid_ticket:
                    valid_tickets.append(nums)
            if line == "your ticket:":
                is_my_ticket = True
            if line == "nearby tickets:":
                is_nearby_tickets = True
    
    return rate, my_ticket

def get_product_of_six_positions(valid_tickets):
    
    rule_pos_map = {}

    rules_flatten = defaultdict(set)
    for rule, ranges in rules.items():
        start1 = ranges[0][0]
        end1 = ranges[0][1]
        start2 = ranges[1][0]
        end2 = ranges[1][1]
        for i in range(start1, end1+1):
            rules_flatten[rule].add(i)
        
        for i in range(start2, end2+1):
            rules_flatten[rule].add(i)
    
    rules_position = defaultdict(set)
    for rule in rules:
        rules_position[rule] = [idx for idx in range(len(valid_tickets[0]))]
    
    while rules_position:
        for ticket in valid_tickets:
            for idx, value in enumerate(ticket):
                for rule in rules_position:
                    if idx in rules_position[rule] and value not in rules_flatten[rule]:
                            rules_position[rule].remove(idx)
            
        rule, idxs = sorted(rules_position.items(), key = lambda x: len(x[1]))[0]
        rule_pos_map[rule] = idxs[0]
        del rules_position[rule]
        for rule in rules_position:
            rules_position[rule].remove(idxs[0])
    
    product_of_six_departures = 1
    for rule, pos in rule_pos_map.items():
        if rule.startswith("departure"):
            product_of_six_departures *= my_ticket[pos]
   
    return product_of_six_departures

rate, my_ticket = get_scanning_rate(filename)
print(rate)
print(get_product_of_six_positions(valid_tickets))