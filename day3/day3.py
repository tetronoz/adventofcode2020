filename = "./input/input.txt"

def count_trees(filename, right, down):
    trees = 0
    pos = right
    num_chars = 0
    current_line_num = 0
    action_line = down

    with open(filename) as fp:
        for line_from_fp in fp:
            line = line_from_fp.strip()
            if current_line_num == 0:
                num_chars = len(line)
                current_line_num += 1
                continue
            else:
                if current_line_num == action_line:
                    if line[pos % num_chars] == '#':
                        trees += 1
                    pos += right
                    action_line += down
                current_line_num += 1
                
    return trees


def find_prod_trees(params):
    product_of_trees = 1
    for right, down in params:
        product_of_trees *= (count_trees(filename, right, down))
    return product_of_trees

print(count_trees(filename, 1, 2))
params = [[1,1], [3,1], [5, 1], [7, 1], [1, 2]]
print(find_prod_trees(params))