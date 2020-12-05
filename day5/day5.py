filename = "./input/input.txt"

def bsp(letters, lower, upper):
    middle = (upper + lower) // 2
    lower_chars = {'F': True, 'L': True}
    upper_chars = {'B': True, 'R': True}
    if len(letters) == 1:
        return lower if letters in lower_chars else upper
    else:
        if letters[0] in lower_chars:
            res = bsp(letters[1:], lower, middle)
        elif letters[0] in upper_chars:
            res = bsp(letters[1:], middle+1, upper)
    return res


def get_seat_row(characters):
    return bsp(characters, 0, 127)

def get_seat_column(characters):
    return bsp(characters, 0, 7)

def get_seat_position(boarding_pass):
    row = get_seat_row(boarding_pass[:7])
    col = get_seat_column(boarding_pass[7:])
    return row, col

def get_out_seat_id(seat_ids):
    
    # go through all possible seat ids excluding the very front (0) and back (127) rows
    for row in range(1, 127):
        for col in range(9):
            t_id = row * 8 + col
            if t_id not in seat_ids and (t_id - 1 in seat_ids and t_id + 1 in seat_ids):
                return t_id
    return None

def process_boarding_passes(filename):
    highest_seat_id = float("-inf")
    all_seat_ids = set()
    with open(filename) as fp:
        for line in fp:
            boarding_pass = line.strip()
            row, col = get_seat_position(boarding_pass)
            current_seat_id = row * 8 + col
            all_seat_ids.add(current_seat_id)
            highest_seat_id = max(highest_seat_id, current_seat_id)
    our_seat_id = get_out_seat_id(all_seat_ids)
    return highest_seat_id, our_seat_id

higest_seat_id, our_seat_id = process_boarding_passes(filename)
print(higest_seat_id)
print(our_seat_id)