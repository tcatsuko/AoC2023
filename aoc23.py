import networkx as nx
raw_input = []
f = open ('aoc23.txt','rt')
for  line in f:
    raw_input += [line[:-1]]
f.close()
height = len(raw_input)
width = len(raw_input[0])
start_point = (1, 0)
end_point = (width - 2, height - 1)
G = nx.DiGraph()
# Now build up the graph
for y in range(height):
    for x in range(width):
        current_tile = raw_input[y][x]
        if current_tile == '#':
            continue
        # Check if on steep slope
        if current_tile == '^':
            G.add_edge((x, y),(x,y-1))
            continue
        elif current_tile == '>':
            G.add_edge((x, y), (x+1, y))
            continue
        elif current_tile == '<':
            G.add_edge((x,y),(x-1,y))
            continue
        elif current_tile == 'v':
            G.add_edge((x, y),(x, y+1))
            continue
        elif (x, y) == end_point:
            continue
        # Now check each direction
        # up
        if y > 0:
            if raw_input[y-1][x] != '#':
                G.add_edge((x, y),(x, y-1))
        if y < (height - 1):
            if raw_input[y + 1][x] != '#':
                G.add_edge((x, y), (x, y+1))
        if x > 0:
            if raw_input[y][x - 1] != '#':
                G.add_edge((x, y),(x-1, y))
        if x < (width - 1):
            if raw_input[y][x + 1] != '#':
                G.add_edge((x, y), (x+1, y))
all_paths = nx.all_simple_paths(G, start_point, end_point)
max_path = 0
for path in all_paths:
    this_path = list(path)
    if len(this_path) > max_path:
        max_path = len(this_path)
print('Part 1: Max path length is ' + str(max_path - 1))

G = nx.Graph()
# Seems to be easiest to condense the input map into a list of intersections
node_info = {}
# First loop through and find all "intersection" nodes
intersection_nodes = []
for y in range(height):
    for x in range(width):
        if raw_input[y][x] == '#':
            continue
        directions = 0
        if y > 0:
            if raw_input[y-1][x] != '#':
                directions += 1
        if y < (height - 1):
            if raw_input[y + 1][x] != '#':
                directions += 1
        if x > 0:
            if raw_input[y][x-1] != '#':
                directions += 1
        if x < (width - 1):
            if raw_input[y][x+1] != '#':
                directions += 1
        if directions > 2:
            intersection_nodes += [(x, y)]
# walk through each intersection node
intersection_nodes = [(1, 0)] + intersection_nodes
intersection_nodes += [(width - 2, height-1)]
# walk through each intersection node
for start_node in intersection_nodes:
    # check up
    directions = []
    x = start_node[0]
    y = start_node[1]
    if y > 0:
        if raw_input[y-1][x] != '#':
            directions += [(0,-1)]
    if y < (height - 1):
        if raw_input[y + 1][x] != '#':
            directions += [(0,1)]
    if x > 0:
        if raw_input[y][x-1] != '#':
            directions += [(-1,0)]
    if x < (width - 1):
        if raw_input[y][x+1] != '#':
            directions += [(1,0)]
    while directions:
        visited_points = set()
        distance = 0
        visited_points.add(start_node)
        current_direction = directions.pop(0)
        start_direction = (current_direction[0], current_direction[1])
        current_point = (start_node[0] + start_direction[0], start_node[1] + start_direction[1])
        x = current_point[0]
        y = current_point[1]
        distance += 1
        visited_points.add(current_point)
        # check up
        dead_end = False
        if y > 0 and raw_input[y-1][x] != '#' and (x,y-1) not in visited_points:
            current_direction = (0,-1)
        if y < height - 1:
            if raw_input[y+1][x] != '#':
                if (x, y+1) not in visited_points:
                    current_direction = (0,1)
        # elif (y < height - 1) and raw_input[y+1][x] != '#' and current_direction != (0,-1):
        #     current_direction = (0,1)
        if x > 0 and raw_input[y][x-1] != '#' and (x-1,y) not in visited_points:
            current_direction = (-1,0)
        if x < width - 1 and raw_input[y][x+1] != '#' and (x+1,y) not in visited_points:
            current_direction = (1,0)
        
        if dead_end == True:
            continue
        while current_point not in intersection_nodes:
            
            visited_points.add(current_point)
            dead_end = False
            possible_directions = 0
            x = current_point[0]
            y = current_point[1]
            if y > 0 and raw_input[y-1][x] != '#' and (x,y-1) not in visited_points:
                current_direction = (0,-1)
                possible_directions += 1
            if (y < height - 1) and raw_input[y+1][x] != '#' and (x,y+1) not in visited_points:
                current_direction = (0,1)
                possible_directions += 1
            if x > 0 and raw_input[y][x-1] != '#' and (x-1,y) not in visited_points:
                current_direction = (-1,0)
                possible_directions += 1
            if x < width - 1 and raw_input[y][x+1] != '#' and (x+1,y) not in visited_points:
                current_direction = (1,0)
                possible_directions += 1
            if possible_directions == 0:
                dead_end = True
                break
           
            distance += 1
            current_point = (current_point[0] + current_direction[0], current_point[1] + current_direction[1])

        if dead_end == True:
            continue
        if start_node not in node_info:
            node_info[start_node] = {}
        node_info[start_node][current_point] = distance
# build the graph
for node in node_info:
    for next_node in node_info[node]:
        G.add_edge(node, next_node)
all_possible_paths = nx.all_simple_paths(G, (1, 0), (width - 2, height-1))
max_path = 0
for path in all_possible_paths:
    distance = 0
    for n_idx in range(len(path) - 1):
        start = path[n_idx]
        end = path[n_idx + 1]
        distance += node_info[start][end]
    if distance > max_path:
        max_path = distance
print('Part 2: Max path length is ' + str(max_path))

