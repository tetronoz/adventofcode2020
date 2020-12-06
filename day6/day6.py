filename = "./input/input.txt"
from collections import Counter

def count_any_yes_in_group(group_answers):
    return len(set(group_answers))

def count_all_yes_in_group(group_answers, size):
    yes_answers = 0
    c = Counter(group_answers)
    for v in c.values():
        if v == size:
            yes_answers += 1
    return yes_answers
    
def count_yes_answers(filename):
    count_any_yes = 0
    count_all_yes = 0
    group_answers = []
    group_size = 0
    with open(filename) as fp:
        for line in fp:
            if line == '\n':
                count_any_yes += count_any_yes_in_group(group_answers)
                count_all_yes += count_all_yes_in_group(group_answers, group_size)
                group_answers = []
                group_size = 0
            else:
                group_size += 1
                group_answers.extend(list(line.strip()))
    
    count_any_yes += count_any_yes_in_group(group_answers)
    count_all_yes += count_all_yes_in_group(group_answers, group_size)
    return count_any_yes, count_all_yes

any_yes, all_yes = count_yes_answers(filename)
print(any_yes)
print(all_yes)