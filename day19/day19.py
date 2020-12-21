filename = "./input/input.txt"

import sys
import re

def parse_input_value(raw_value):
    raw_value = raw_value.strip()
    if raw_value[0] == '"':
        raw_value = raw_value.replace('"', '')
        return raw_value
    else:
        raw_value = raw_value.split("|")
        rules = []
        for rv in raw_value:
            r = []
            for rn in rv.strip().split():
                r.append(int(rn))
            rules.append(r)
        
        return rules if len(rules) > 1 else rules[0]

def read_input(filename):
    raw_rules = {}
    with open(filename) as fp:
        for line in fp:
            if line != '\n':
                key, raw_value = line.strip().split(":", 1)
                key = int(key)
                value = parse_input_value(raw_value)
                raw_rules[int(key)] = value
            else:
                return raw_rules

def build_rules():
    raw_rules = read_input(filename)
    
    return raw_rules

def compile_rules(raw_rules):
    for rule in raw_rules:
        if isinstance(raw_rules[rule], list) and len(raw_rules[rule]) == 2 and isinstance(raw_rules[rule][0], list):
            raw_rules[rule].insert(0, ['('])
            raw_rules[rule].insert(2, ['|'])
            raw_rules[rule].insert(4, [')'])

    def compile_rule(rule_numbers):

        if isinstance(rule_numbers, str):
            return rule_numbers
        
        s = ""
        for rn in rule_numbers:
            if isinstance(rn, int):
                s += compile_rule(raw_rules[rn])
            elif isinstance(rn, list):
                s += compile_rule(rn)
            elif isinstance(rn, str):
                s += rn
         
        return s
            
    return compile_rule(raw_rules[0])
    

raw_rules = build_rules()
pattern = compile_rules(raw_rules)
def count_matches(filename, pattern):
    read_line = False
    count = 0
    pat = re.compile(pattern)
    with open(filename) as fp:
        for line in fp:
            if read_line:
                line = line.strip()
                match = re.fullmatch(pat, line)
                if match:
                    count += 1
                
            if line != '\n':
                continue
            else:
                read_line = True
    print(count)

count_matches(filename, pattern)