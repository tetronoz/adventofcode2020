from collections import Counter

filename = "./input/input.txt"

def count_valid_passwords(filename):
    count = 0
    with open(filename) as fp:
        for line in fp:
            times, letter, password = parse_line(line.strip())
            c = Counter(password)
            if c[letter] <= times[1] and c[letter] >= times[0]:
                count += 1
    return count

def count_valid_passwords_new_policy(filename):
    count = 0
    with open(filename) as fp:
        for line in fp:
            positions, letter, password = parse_line(line.strip())
            first = positions[0] - 1
            second = positions[1] - 1
            if (letter == password[first] and letter != password[second]) or (letter != password[first] and letter == password[second]):
                count += 1
    return count


def parse_line(line):
    times_raw, letter_raw, password = line.split()
    times = [x for x in map(int, times_raw.split("-"))]
    letter = letter_raw[0]

    return times, letter, password

print(count_valid_passwords(filename))
print(count_valid_passwords_new_policy(filename))