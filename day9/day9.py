filename = "./input/input.txt"

def process_file(filename):
    with open(filename) as fp:
        return [int(num.strip()) for num in fp]


data = process_file(filename)

def find_two_sum(nums, target):
    two_sum_map = {}

    for num in nums:
        candidate = target - num
        if candidate in two_sum_map:
            return True
        else:
            two_sum_map[num] = True
    return False

def get_wrong_number(wsize):
    window = wsize

    target_idx = len(data) - 1
    p2 = target_idx
    p1 = p2 - window
    
    while p1 > 0:
        target = data[target_idx]
        nums = data[p1:p2]
        if not find_two_sum(nums, target):
            return target
        target_idx -= 1
        p2 -= 1
        p1 -= 1
    return

def find_min_max(p1, p2):
    min_num = float("inf")
    max_num = float("-inf")

    while p1 < p2:
        min_num = min(min_num, data[p1])
        max_num = max(max_num, data[p1])
        p1 += 1
    
    return min_num, max_num

def get_encryption_weakness(target):
    p1 = 0
    p2 = 1
    cur_sum = data[p1] + data[p2]

    while cur_sum != target:
        if cur_sum < target:
            p2 += 1
            cur_sum += data[p2]
        elif cur_sum > target:
            cur_sum -= data[p1]
            p1 += 1
        elif cur_sum == target:
            break

    min_num, max_num = find_min_max(p1, p2)
    
    return min_num + max_num


wrong_number = get_wrong_number(25)
print(wrong_number)
encryption_weakness = get_encryption_weakness(wrong_number)
print(encryption_weakness)