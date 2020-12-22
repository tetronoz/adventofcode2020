filename = "./input/input.txt"

from collections import defaultdict

def read_input_from_file(filename):
    in_title = False
    titels = defaultdict(list)

    with open(filename) as fp:
        for line in fp:
            if line == '\n':
                in_title = False
                continue
            if line.startswith("Tile"):
                line = line.strip()
                title_id = int(line.split()[1][:-1])
                in_title = True
                continue
            if in_title:
                line = line.strip()
                titels[title_id].append(line)
    
    return titels

def get_edges(data):
    edges = [data[0], data[-1]]
    
    left = []
    right = []
    
    for d in data:
        left.append(d[0])
        right.append(d[-1])
    
    edges.append("".join(left))
    edges.append("".join(right))
    
    return edges

titles = read_input_from_file(filename)

matches = defaultdict(int)
seen_edges = {}
edge_to_title = defaultdict(list)

for title_id, data in titles.items():
    edges = get_edges(data)
    for edge in edges:
        
        edge_to_title[edge].append(title_id)
        edge_to_title[edge[::-1]].append(title_id)
        
        if edge in seen_edges:
            for t_id in edge_to_title[edge]:
                matches[t_id] += 1
        elif edge[::-1] in seen_edges:
            for t_id in edge_to_title[edge[::-1]]:
                matches[t_id] += 1
        else:
            seen_edges[edge] = True
            seen_edges[edge[::-1]] = True
            
answer = 1
for tid, v in matches.items():
    if v == 2:
        answer *= tid

print(answer)