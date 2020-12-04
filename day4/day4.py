filename = "./input/input.txt"

def is_key_valid(k, v):
    valid = True

    if k == 'byr' and (int(v) < 1920 or int(v) > 2002):
        return False
    
    elif k == 'iyr' and (int(v) < 2010 or int(v) > 2020):
        return False
    
    elif k == 'eyr' and (int(v) < 2020 or int(v) > 2030):
        return False
    
    elif k == 'hgt':
        unit = v[-2:]
        if unit != 'cm' and unit != 'in':
            return False
        height = int(v[:-2])
        if unit == 'cm' and (height < 150 or height > 193):
            return False
        elif unit == 'in' and (height < 59 or height > 76):
            return False
    
    elif k == 'hcl':
        if v[0] != '#' or len(v) != 7:
            return False
        for i in range(1, len(v)):
            if not v[i].isdigit() and (v[i].isascii() and v[i] > 'f'):
                return False
    
    elif k == 'ecl':
        colors = {'amb': True, 'blu': True, 'brn': True, 'gry': True, 'grn': True, 'hzl': True, 'oth': True}
        if v not in colors:
            return False
    
    elif k == 'pid':
        if len(v) != 9 or not v.isdigit():
            return False

    return valid

def is_all_keys_present(passport_keys, required_fields):
    valid = True
    
    for k in required_fields:
        if k not in passport_keys:
            return False
    
    return valid

def are_keys_valid(passport_data):
    valid = True
    
    for key, value in passport_data.items():
        if not is_key_valid(key, value):
            return False
    return valid

def is_passport_valid(passport_data, required_fields):
    all_keys_valid = False
    data_splitted = " ".join(passport_data).split()
    fields_and_values = {}
    for data in data_splitted:
        key, value = data.split(':')
        fields_and_values[key] = value

    have_all_keys = is_all_keys_present(fields_and_values.keys(), required_fields)
    if have_all_keys:
        all_keys_valid = are_keys_valid(fields_and_values)

    return have_all_keys, all_keys_valid
    
def count_valid_passports(filename):
    passport_data = []
    valid_passports_part1 = 0
    valid_passports_part2 = 0
    required_fields = {'byr': True, 'iyr': True, 'eyr': True, 'hgt': True, 'hcl': True, 'ecl': True, 'pid': True}

    with open(filename) as fp:
        for line in fp:
            if line != "\n":
                passport_data.append(line.strip())
                continue
            
            result = is_passport_valid(passport_data, required_fields)
            if result[0]:
                valid_passports_part1 += 1
            if result[0] and result[1]:
                valid_passports_part2 += 1
            passport_data = []

        if passport_data:
            result = is_passport_valid(passport_data, required_fields)
            if result[0]:
                valid_passports_part1 += 1
            if result[0] and result[1]:
                valid_passports_part2 += 1

    return valid_passports_part1, valid_passports_part2

part1, part2 = count_valid_passports(filename)

print(part1)
print(part2)