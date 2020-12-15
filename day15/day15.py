input_data = "6,13,1,15,2,0"

numbers = [int(x) for x in input_data.split(",")]

def update_spoken_numbers(number, game_data, turn):
    if number in game_data:
        count, _ , turn_last = game_data[number]
        game_data[number] = [count+1, turn_last, turn]
    else:
        game_data[number] = [1, None, turn]
    
    return game_data


def get_number_spoken(target, numbers):
    
    # number : [count, turn_prev, turn_last]
    spoken_numbers = {}

    for i, v in enumerate(numbers):
        spoken_numbers[v] = [1, None, i+1]
    
    turn = len(numbers)
    last_num_spoken = numbers[-1]
    while turn != target:
        turn += 1
        if last_num_spoken in spoken_numbers and spoken_numbers[last_num_spoken][0] == 1:
            last_num_spoken = 0
            spoken_numbers = update_spoken_numbers(last_num_spoken, spoken_numbers, turn)
            
        elif last_num_spoken in spoken_numbers and spoken_numbers[last_num_spoken][0] > 1:
            _, turn_prev, turn_last = spoken_numbers[last_num_spoken]
            last_num_spoken = turn_last - turn_prev
            spoken_numbers = update_spoken_numbers(last_num_spoken, spoken_numbers, turn)
            
    
    return last_num_spoken

print(get_number_spoken(2020, numbers))
print(get_number_spoken(30000000, numbers))