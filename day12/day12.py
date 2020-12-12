filename = "./input/input.txt"

import math

def read_input(filename):
    return [line.strip() for line in open(filename)]


moves = read_input(filename)

def process_moves_part1(moves):
    
    directions = ['E', 'S', 'W', 'N']
    cur_direction_idx = 0
    cur_direction = directions[cur_direction_idx]

    moves_map = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    
    for move in moves:
        direction = move[0]
        units = int(move[1:])

        if direction == 'F':
            moves_map[cur_direction] += units
        elif direction == 'L':
            shift = units // 90
            cur_direction_idx = (cur_direction_idx - shift) % 4
            cur_direction = directions[cur_direction_idx]
        elif direction == 'R':
            shift = units // 90
            cur_direction_idx = (cur_direction_idx + shift) % 4
            cur_direction = directions[cur_direction_idx]
        else:
            moves_map[direction] += units
    
    return abs(moves_map['E'] - moves_map['W']) + abs(moves_map['S'] - moves_map['N'])

print(process_moves_part1(moves))


def get_new_waypoint(current_waypoint, units, rotation):
    
    if rotation == 'R':
        units *= -1

    rads = math.radians(units)

    x = int(current_waypoint[0] * math.cos(rads)) - int(current_waypoint[1] * math.sin(rads))
    y = int(current_waypoint[0] * math.sin(rads)) + int(current_waypoint[1] * math.cos(rads))

    return [x, y]


def update_waypoint(waypoint, direction, units):
    if direction == 'S':
        waypoint[1] -= units
    elif direction == 'W':
        waypoint[0] -= units
    elif direction == 'E':
        waypoint[0] += units
    elif direction == 'N':
        waypoint[1] += units
    
    return waypoint

def process_moves_part2(moves):
    waypoint = [10, 1]
    ship = [0, 0]

    for move in moves:
        direction = move[0]
        units = int(move[1:])
        
        if direction == 'F':
            ship[0] += units * waypoint[0]
            ship[1] += units * waypoint[1]
        elif direction == 'L':
            waypoint = get_new_waypoint(waypoint, units, 'L')
        elif direction == 'R':
            waypoint = get_new_waypoint(waypoint, units, 'R')
        else:
            waypoint = update_waypoint(waypoint, direction, units)
        
    return abs(ship[0]) + abs(ship[1])

print(process_moves_part2(moves))
