filename = "./input/input.txt"

from collections import defaultdict

bags_map = defaultdict(list)

def build_bags_map(line):
    line = line.strip(".").replace(",", "").split()
    parent = None
    digit_idx = None

    for idx, word in enumerate(line):
        if word == 'bags' and parent is None:
            parent = " ".join(line[:idx])
        elif word.isdigit():
            digit_idx = idx
        elif (word == 'bags' or word == 'bag') and parent is not None and digit_idx is not None:
            bags_map[parent].append((int(line[digit_idx]), " ".join(line[digit_idx + 1: idx])))

def dfs(parent, bag_type):
    count = 0
    for bag in bags_map[parent]:
        if bag[1] == bag_type:
            count = 1
        if bag[1] in bags_map:
            count = max(dfs(bag[1], bag_type), count)
    return count

def count_inner_bags(bags):
    inner_sum = 0
    for bag_nums, bag_type in bags:
        if bag_type in bags_map:
            inner_sum += bag_nums + bag_nums * (count_inner_bags(bags_map[bag_type]))
        else:
            inner_sum += bag_nums
    return inner_sum

def count_bags(filename, bag_type):
    count = 0
    with open(filename) as fp:
        for line in fp:
            build_bags_map(line.strip())
    
    for bag in bags_map:
        count += dfs(bag, bag_type)

    inner_sum = count_inner_bags(bags_map[bag_type])

    return count, inner_sum

count, inner_sum  = count_bags(filename, "shiny gold")
print(count)
print(inner_sum)
