filename = "./input/input.data"

def find_two_sum(filename, target):
    two_sum_map = {}

    with open(filename) as fp:
        for line in fp:
            num = int(line.strip())
            candidate = target - num
            if candidate in two_sum_map:
                return num * candidate
            else:
                two_sum_map[num] = True


def find_three_sum(filename, target):
    data = [int(line.strip()) for line in open(filename)]
    data.sort()
    
    for i in range(len(data) - 2):
        num1 = data[i]
        x = i + 1
        y = len(data) - 1
        while x < y:
            num2 = data[x]
            num3 = data[y]
            three_sum = num1 + num2 + num3
            if three_sum == target:
                return num1 * num2 * num3
            elif three_sum > target:
                y -= 1
            elif three_sum < target:
                x += 1

print(find_two_sum(filename, 2020))
print(find_three_sum(filename, 2020))