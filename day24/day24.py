filename = "./input/input.txt"
import copy

def get_tile_position(line):
    
    pos = [0, 0]

    i = 0
    cur_dir = "" 
    while i < len(line):
        ch = line[i]
        if (ch == 'e' or ch == 'w') and cur_dir == '':
            cur_dir = ch
        elif cur_dir == '' and (ch == 's' or ch == 'n'):
            cur_dir = ch
            i += 1
            continue
        elif cur_dir != '':
            cur_dir += ch
        
        # https://www.redblobgames.com/grids/hexagons/#neighbors

        if cur_dir == 'e':
            pos[0] +=1 
        elif cur_dir == 'w':
            pos[0] -= 1
        elif cur_dir == 'se':
            pos[1] += 1
        elif cur_dir == 'sw':
            pos[0] -= 1
            pos[1] += 1
        elif cur_dir == 'nw':
            pos[1] -= 1
        elif cur_dir == 'ne':
            pos[0] += 1
            pos[1] -= 1

        cur_dir = ''
        i += 1
    
    return tuple(pos)

def populate_grid_map(filename):

    grid_colors = {}
    # 0 - white
    # 1 - black
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            tile_pos = get_tile_position(line)
            if tile_pos in grid_colors:
                grid_colors[tile_pos] ^= 1
            else:
                grid_colors[tile_pos] = 1
    
    return grid_colors

grid_map = populate_grid_map(filename)

def get_neighbours_colors(tile_pos, grid):
    blacks = 0

    neighbours = [(tile_pos[0] + n[0], tile_pos[1] + n[1]) for n in [[1, -1], [1, 0], [0, 1], [-1, 1], [-1, 0], [0, -1]]]

    for n in neighbours:
        if n in grid and grid[n] == 1:
            blacks += 1
        
    
    return blacks

def solution_part1(grid_map):
    return sum(grid_map.values())

def solution_part2(grid_map):

    for pos in list(grid_map.keys()):
            neighbours = [(pos[0] + n[0], pos[1] + n[1]) for n in [[1, -1], [1, 0], [0, 1], [-1, 1], [-1, 0], [0, -1]]]
            for n in neighbours:
                if n not in grid_map:
                    grid_map[n] = 0

    for _ in range(1, 101):
        pos_to_flip = []
        new_neighbours = []

        for tile_pos, color in grid_map.items():
            blacks = 0
            neighbours = [(tile_pos[0] + n[0], tile_pos[1] + n[1]) for n in [[1, -1], [1, 0], [0, 1], [-1, 1], [-1, 0], [0, -1]]]
            
            for n in neighbours:
                if n in grid_map:
                    if grid_map[n] == 1:
                        blacks += 1
                else:
                    new_neighbours.append(n)

            if color == 0 and blacks == 2:
                pos_to_flip.append(tile_pos)
            elif color == 1 and (blacks == 0 or blacks > 2):
                pos_to_flip.append(tile_pos)
            
        for pos in pos_to_flip:
            grid_map[pos] ^= 1
        
        for nn in new_neighbours:
            grid_map[nn] = 0


    return sum(grid_map.values())

print(solution_part1(grid_map))
print(solution_part2(grid_map))
