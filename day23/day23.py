import sys
puzzle = "364297581"
#puzzle = "389125467"


def solution_part1(p):
    digits = [int(x) for x in list(p)]

    mod = len(digits)
    
    min_label = min(digits)
    max_label = max(digits)

    move = 0
    c_idx = 0

    while move < 100:
        move += 1
        
        current_cup = digits[c_idx]
        
        if c_idx + 4 <= len(digits):
            three_cups = digits[c_idx + 1: c_idx + 4]
            digits = digits[:c_idx + 1] + digits[c_idx + 4:]
        elif c_idx + 1 == len(digits):
            three_cups = digits[(c_idx + 1) % mod:(c_idx + 4) % mod]
            digits = digits[(c_idx + 4) % mod:]
        else:
            three_cups = digits[(c_idx + 1) % mod:] + digits[:(c_idx + 4) % mod]
            digits = digits[(c_idx + 4) % mod: c_idx + 1]
        
        destination_cup = current_cup - 1
        
        while True:
            if destination_cup < min_label:
                destination_cup = max_label

            if destination_cup not in three_cups:
                break
            else:
                destination_cup -= 1
        
        d_idx = digits.index(destination_cup)

        digits = digits[:d_idx + 1] + three_cups + digits[d_idx+1:]
        c_idx = digits.index(current_cup)
        
        if c_idx + 1 < len(digits):
            c_idx += 1
        else:
            c_idx = 0
    
    one_idx = digits.index(1)
    
    answer = [str(x) for x in digits[one_idx+1:] + digits[:one_idx]]
    print("".join(answer))

def solution_part2(p):
    cups = [int(x) for x in list(puzzle)]

    for i in range(len(cups)+1, 1000001):
        cups.append(i)

    max_label = len(cups)
    min_label = 1

    nexts = [0] * (len(cups) + 1)
    nexts[0] = cups[0]

    lastidx = cups[-1]

    for idx in range(1, len(cups)):
        nexts[cups[idx-1]] = cups[idx]

    head = nexts[0]
    print_move = 0

    move = 0

    while move < 10000000:
        move += 1
        one, two, three = nexts[head], nexts[nexts[head]], nexts[nexts[nexts[head]]]

        dest_cup = head - 1

        while True:
            if dest_cup < min_label:
                dest_cup = max_label
            if dest_cup != one and dest_cup != two and dest_cup != three:
                break
            else:
                dest_cup -= 1

        nexts[head] = nexts[three]
        dest_next_save = nexts[dest_cup]
        nexts[dest_cup] = one
        nexts[three] = dest_next_save

        if nexts[three] == 0:
            lastidx = three
        nexts[lastidx] = head

        new_head = nexts[head]
        nexts[head] = 0
        lastidx = head
        nexts[0] = new_head
        head = nexts[0]

    m = nexts[1]
    n = nexts[m]
    print(m*n)
                
solution_part1(puzzle)
solution_part2(puzzle)