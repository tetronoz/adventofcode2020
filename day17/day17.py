filename = "./input/input.txt"
import sys

input_grid = set()

def parse_input(filename, part=None):
    grid = set()
    y = -1
    z = 0
    if part == 'part2':
        w = 0
    with open(filename) as fp:
        for line in fp:
            y += 1
            line = line.strip()
            for x, v in enumerate(line):
                if v == '#':
                    if part != 'part2':
                        grid.add((x, y, z))
                    else:
                        grid.add((x, y, z, w))

    return grid

input_grid = parse_input(filename)

def solution_part1(input_grid):
    grid = input_grid
    temp_grid = set()

    start_x = float("inf")
    end_x = float("-inf")
    start_y = float("inf")
    end_y = float("-inf")

    for cube in grid:
        start_x = min(cube[0], start_x)
        end_x = max(cube[0], end_x)
        start_y = min(cube[1], start_y)
        end_y = max(cube[1], end_y)
        
    start_x -= 1
    end_x += 1
    start_y -= 1
    end_y +=1

    for cycle in range(1, 7):
        if cycle > 1:
            start_x = new_start_x - 1
            end_x = new_end_x + 1
            start_y = new_start_y - 1
            end_y = new_end_x + 1

        new_start_x = float("inf")
        new_end_x = float("-inf")
        new_start_y = float("inf")
        new_end_y = float("-inf")
        
        for z in range(-cycle, cycle + 1):
            for y in range(start_y, end_y + 1):
                for x in range(start_x , end_x + 1):
                    neighbors_count = sum(1 for i in range(x-1, x+2) for j in range(y-1, y+2) for k in range(z-1, z+2) if (i, j, k) in grid)
                    
                    if (x, y, z) in grid and 3<= neighbors_count <= 4:
                        temp_grid.add((x, y, z))
                        new_start_x = min(new_start_x, x)
                        new_end_x = max(new_end_x, x)
                        new_start_y = min(new_start_y, y)
                        new_end_y = max(new_end_y, y)
                    if (x, y, z) not in grid and neighbors_count == 3:
                        temp_grid.add((x, y, z))
                        new_start_x = min(new_start_x, x)
                        new_end_x = max(new_end_x, x)
                        new_start_y = min(new_start_y, y)
                        new_end_y = max(new_end_y, y)
        
        grid = temp_grid
        temp_grid = set()
    
    print(len(grid))


def solution_part2(input_grid):
    grid = input_grid
    temp_grid = set()

    start_x = float("inf")
    end_x = float("-inf")
    start_y = float("inf")
    end_y = float("-inf")

    for cube in grid:
        start_x = min(cube[0], start_x)
        end_x = max(cube[0], end_x)
        start_y = min(cube[1], start_y)
        end_y = max(cube[1], end_y)
        
    start_x -= 1
    end_x += 1
    start_y -= 1
    end_y +=1

    for cycle in range(1, 7):
        if cycle > 1:
            start_x = new_start_x - 1
            end_x = new_end_x + 1
            start_y = new_start_y - 1
            end_y = new_end_x + 1

        new_start_x = float("inf")
        new_end_x = float("-inf")
        new_start_y = float("inf")
        new_end_y = float("-inf")

        for w in range(-cycle, cycle + 1):    
            for z in range(-cycle, cycle + 1):
                for y in range(start_y, end_y + 1):
                    for x in range(start_x , end_x + 1):
                        #neighbors_count = 0
                        neighbors_count = sum(1 for i in range(x-1, x+2) for j in range(y-1, y+2) for k in range(z-1, z+2) for l in range(w-1, w+2) if (i, j, k, l) in grid)
                        #for k in range(z-1, z+2):
                        #    for j in range(y-1, y+2):
                        #        for i in range(x-1, x+2):
                        #            if (i, j, k) != (x, y, z) and (i, j, k) in grid:
                        #                neighbors_count += 1
                        if (x, y, z, w) in grid and 3<= neighbors_count <= 4:
                            new_start_x = min(new_start_x, x)
                            new_end_x = max(new_end_x, x)
                            new_start_y = min(new_start_y, y)
                            new_end_y = max(new_end_y, y)
                            temp_grid.add((x, y, z, w))
                        if (x, y, z, w) not in grid and neighbors_count == 3:
                            new_start_x = min(new_start_x, x)
                            new_end_x = max(new_end_x, x)
                            new_start_y = min(new_start_y, y)
                            new_end_y = max(new_end_y, y)
                            temp_grid.add((x, y, z, w))
        
        grid = temp_grid
        temp_grid = set()
    
    print(len(grid))

solution_part1(input_grid)
input_grid = parse_input(filename, 'part2')
solution_part2(input_grid)