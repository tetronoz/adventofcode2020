input_data = "6,13,1,15,2,0"

numbers = [int(x) for x in input_data.split(",")]

def get_number_spoken(target, numbers):
    
    spoken_numbers = {}

    turn = 1
    for number in numbers[:-1]:
        spoken_numbers[number] = turn
        turn += 1
    
    turn += 1
    last_num_spoken = numbers[-1]

    while turn <= target:
        if last_num_spoken not in spoken_numbers:
            spoken_numbers[last_num_spoken] = turn - 1
            last_num_spoken = 0
        else:
            diff = turn - 1 - spoken_numbers[last_num_spoken]  
            spoken_numbers[last_num_spoken] = turn - 1
            last_num_spoken = diff
        turn += 1
             
    return last_num_spoken

print(get_number_spoken(2020, numbers))
print(get_number_spoken(30000000, numbers))