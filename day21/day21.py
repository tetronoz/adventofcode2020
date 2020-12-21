filename = "./input/input.txt"
import re
import sys
from collections import defaultdict

allergens_to_ingredients = defaultdict(list)
appearence_count = defaultdict(int)
all_allergens = set()
dangerous = {}

def build_map(filename):
    pattern = ("(.*)\s\(contains\s(.*)\)")
    compiled_pattern = re.compile(pattern)

    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            match = re.search(compiled_pattern, line)
            if not match:
                print("ERROR")
                sys.exit()
            else:
                ingreds = match.group(1)
                allergens = match.group(2)
                for allergen in allergens.split(", "):
                    allergens_to_ingredients[allergen].append(set(ingreds.split()))
                for ingr in ingreds.split():
                    appearence_count[ingr] += 1
                    all_allergens.add(ingr)

build_map(filename)

while True:
    running = False
    for allergen in allergens_to_ingredients:
        if len(allergens_to_ingredients[allergen]) > 1:
            sets = allergens_to_ingredients[allergen]
            intersection = set.intersection(*sets)
            if len(intersection) == 1:
                running = True
                intersection = list(intersection)[0]
                dangerous[allergen] = intersection
                for v in allergens_to_ingredients.values():
                    for s in v:
                        if intersection in s:
                            s.remove(intersection)
                        if intersection in all_allergens:
                            all_allergens.remove(intersection)
                        if len(s) == 0:
                            del(s)
    
    for allergen in list(allergens_to_ingredients):
        if len(allergens_to_ingredients[allergen]) == 1 and len(allergens_to_ingredients[allergen][0]) == 1:
            running = True
            alregen_remove = list(allergens_to_ingredients[allergen][0])[0]
            dangerous[allergen] = alregen_remove
            del allergens_to_ingredients[allergen]

            for v in allergens_to_ingredients.values():
                    for s in v:
                        if alregen_remove in s:
                            s.remove(alregen_remove)
                        if alregen_remove in all_allergens:
                            all_allergens.remove(alregen_remove)
                        if len(s) == 0:
                            del(s)

    if not running:
        break

s = 0
for ing in all_allergens:
    s += appearence_count[ing]

print(f'Part 1: {s}')

res = [v[1] for v in sorted(dangerous.items(), key = lambda x: x[0])]
print(f'Part 2: {",".join(res)}')