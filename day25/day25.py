card_pub = 8252394
door_pub = 6269621

def get_loop_size(sn, key):

    value = 1
    loop_size = 0

    while value != key:
        loop_size += 1
        value *= sn 
        value %= 20201227
    
    return loop_size

def transform(sn, loop_size):
    value = 1

    for _ in range(loop_size):
        value *= sn
        value %= 20201227
    
    return value

card_loop_size = get_loop_size(7, card_pub)
door_loop_size = get_loop_size(7, door_pub)

card_enc = transform(card_pub, door_loop_size)
door_enc = transform(door_pub, card_loop_size)

assert card_enc == door_enc
print(card_enc)