filename = "./input/input.txt"

import copy

def construct_grid(filename):
    with open(filename) as fp:
        return [[char for char in list(line.strip()) ] for line in fp]

grid = construct_grid(filename)

def apply_rules_part2(grid):
    g = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            seat = grid[i][j]
            no_occupied = True
            adjacent_occupied = 0 

            # Look all way up
            row = i
            col = j
            while row > 0:
                row -= 1
                if grid[row][j] == '#':
                    no_occupied = False
                    adjacent_occupied += 1

                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break
            
            # Look up diagonally all the way left
            row = i
            col = j
            while row > 0 and col > 0:
                row -= 1
                col -= 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break

            # Look up diagonally all the way to the right
            row = i
            col = j
            while row > 0 and col < len(grid[0]) - 1:
                row -= 1
                col += 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break

            # Look all the way tp the left
            row = i
            col = j
            while col > 0:
                col -= 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break

            # Look all the way to the right
            row = i
            col = j
            while col < len(grid[0]) - 1:
                col += 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break

            # Look all the way down
            row = i
            col = j
            while row < len(grid) - 1:
                row += 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break

            # Look down diagonally all the way to the left
            row = i
            col = j
            while row < len(grid) - 1 and col > 0:
                row += 1
                col -= 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break

            # Look down diagonally all the way to the right
            row = i
            col = j
            while row < len(grid) - 1 and col < len(grid[0]) - 1:
                row += 1
                col += 1
                if grid[row][col] == '#':
                    no_occupied = False
                    adjacent_occupied += 1
                
                if grid[row][col] == '#' or grid[row][col] == 'L':
                    break
            
            if seat == 'L' and no_occupied:
                g[i][j] = '#'
            elif seat == '#' and adjacent_occupied >= 5:
                g[i][j] = 'L'
            
    return g


def apply_rules(grid):
    g = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            seat = grid[i][j]
            no_occupied = True
            adjacent_occupied = 0 

            # Look up
            if i > 0 and grid[i-1][j] == '#':
                no_occupied = False
                adjacent_occupied += 1
            
            # Look up left
            if i > 0 and j > 0 and grid[i-1][j-1] == '#':
                no_occupied = False
                adjacent_occupied += 1

            # Look up right
            if i > 0 and j < len(grid[0]) - 1 and grid[i-1][j+1] == '#':
                no_occupied = False
                adjacent_occupied += 1

            # Look left
            if j > 0 and grid[i][j-1] == '#':
                no_occupied = False
                adjacent_occupied += 1

            # Look right
            if j < len(grid[0]) - 1 and grid[i][j+1] == '#':
                no_occupied = False
                adjacent_occupied += 1

            # Look down
            if i < len(grid) - 1 and grid[i+1][j] == '#':
                no_occupied = False
                adjacent_occupied += 1

            # Look down left
            if i < len(grid) - 1 and j > 0 and grid[i+1][j-1] == '#':
                no_occupied = False
                adjacent_occupied += 1

            # Look down right
            if i < len(grid) - 1 and j < len(grid[0]) - 1 and grid[i+1][j+1] == '#':
                no_occupied = False
                adjacent_occupied += 1
            
            if seat == 'L' and no_occupied:
                g[i][j] = '#'
            elif seat == '#' and adjacent_occupied >= 4:
                g[i][j] = 'L'
            
    return g

def count_occupied_seats(seats):
    count = 0
    for seat in seats:
        if seat == '#':
            count += 1
    return count


def solution_part1(grid):
    memo = {}
    not_seen = True
    while not_seen:
        new_grid = apply_rules(grid)
        flatten = [ele for sub in new_grid for ele in sub]
        if tuple(flatten) in memo:
            not_seen = False
            print(count_occupied_seats(flatten))
        else:
            memo[tuple(flatten)] = True
        grid = new_grid

def solution_part2(grid):
    memo = {}
    not_seen = True
    while not_seen:
        new_grid = apply_rules_part2(grid)
        flatten = [ele for sub in new_grid for ele in sub]
        if tuple(flatten) in memo:
            not_seen = False
            print(count_occupied_seats(flatten))
        else:
            memo[tuple(flatten)] = True
        grid = new_grid


solution_part1(grid)
solution_part2(grid)