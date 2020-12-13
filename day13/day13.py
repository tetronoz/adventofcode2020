from collections import defaultdict

filename = "./input/input.txt"

def parse_input(filename):
    data = [line.strip() for line in open(filename)]

    return int(data[0]),[x for x in data[1].split(',')]

ts, all_bus_lines = parse_input(filename)

def get_earliest_id(ts, all_bus_lines):
    bus_lines = [int(x) for x in all_bus_lines if x != 'x']
    min_wait_time = float("inf")
    earliest_bus_id = None

    for bus_line in bus_lines:
        wait_time = bus_line - (ts % bus_line)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            earliest_bus_id = bus_line
    
    return earliest_bus_id * min_wait_time


print(get_earliest_id(ts, all_bus_lines))

'''
This one won't be possible without:
- a hint from Reddit that directed me to 'Chinese Remainder Theorem'
- a clear explanation of the theorem with an example at https://www.youtube.com/watch?v=zIFehsBHB8o 
'''

def get_earliest_ts(all_bus_lines):
    offsets = []
    bus_ids = []
    bus_ids_product = 1
    N = []

    answer = 0

    for i,v in enumerate(all_bus_lines):
        if v != 'x':
            v = int(v)
            offsets.append(v - i)
            bus_ids.append(v)
            bus_ids_product *= v

    for i, _ in enumerate(bus_ids):
        N.append(bus_ids_product // bus_ids[i])
    
    for i, mod in enumerate(bus_ids):
        n = N[i]
        x = pow(n, -1, mod)
        offset = offsets[i]
        answer += x*offset*n
    
    return answer % bus_ids_product

print(get_earliest_ts(all_bus_lines))