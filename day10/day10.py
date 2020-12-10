
from collections import defaultdict
filename = "./input/input.txt"

def process_input(filename):
    with open(filename) as fp:
        return [int(line.strip()) for line in fp]

jolts = process_input(filename)

def count_jolt_difference(jolts):
    jolts.sort()
    jolts = [0] + jolts
    adapter_jolts = jolts[-1] + 3
    jolts.append(adapter_jolts)

    one_diff = 0
    three_diff = 0

    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i-1]
        if diff == 1:
            one_diff += 1
        elif diff == 3:
            three_diff += 1
    return one_diff * three_diff


'''
This is a dumb one and only works with test input
'''
count = 0
def count_distinct_ways_addapters(jolts):
    global count 
    def backtrack(comb, jolts, end):
        global count
        if comb[-1] == end:
            count +=1
            return

        for i in range(len(jolts)):
            diff = jolts[i] - comb[-1]
            if diff >= 1 and diff <= 3:
                temp = comb[:]
                temp.append(jolts[i])
                backtrack(temp, jolts[i+1:], end)
            else:
                break

    end = jolts[-1]
    for i in range(len(jolts)):
        if jolts[i] >= 1 and jolts[i] <= 3:
            backtrack([jolts[i]], jolts[i+1:], end)
        else:
            break

print(count_jolt_difference(jolts))
#count_distinct_ways_addapters(jolts)
#print(count)

'''
Used ideas from reddit (https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/) to find the solution
DP is for rescue. Still need to get a better grip of DP 
'''
def count_ways(jolts):
    ways = defaultdict(lambda: 0)
    ways[0] = 1
    for jolt in jolts:
        ways[jolt] = ways[jolt - 3] + ways[jolt - 2] + ways[jolt - 1]
    return ways[jolt]

print(count_ways(jolts))