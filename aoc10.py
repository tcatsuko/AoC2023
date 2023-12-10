raw_input = []
f = open('aoc10.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
# appears to be a graph of some sort, pad it with empty space
new_input = []
current_length = len(raw_input[0])
end_length = ['.' * (current_length + 2)]
new_input += end_length
for line in raw_input:
    new_input += ['.' + line + '.']
new_input += end_length
# find the start point
for row, line in enumerate(new_input):
    for column, value in enumerate(line):
        if value == 'S':
            start_point = (column, row)
current_point = start_point
next_point = (-1,-1)
size = 0
# assume you need to check all directions since you don't know what S is
directions_to_check = []

# Find a start direction
# right
valid_directions = ['-','J','7']
if new_input[start_point[1]][start_point[0] + 1] in valid_directions:
    directions_to_check += [(1, 0)]
# down
valid_directions = ['|','L','J']
next_point_coords = (start_point[0], start_point[1] + 1)
if new_input[next_point_coords[1]][next_point_coords[0]] in valid_directions:
    directions_to_check += [(0, 1)]
# left
valid_directions = ['-','L','F']
if new_input[start_point[1] ][start_point[0] - 1] in valid_directions:
    directions_to_check += [(-1, 0)]
# up:
valid_directions = ['|','7','F']

if new_input[start_point[1] - 1][start_point[0]] in valid_directions:
    directions_to_check += [(0, -1)]
all_loop_sizes = []
all_loop_nodes = []
for direction in directions_to_check:
    current_direction = direction

    current_point = start_point
    next_point = (-1,-1)
    size = 0
    loop_nodes = set()
    while current_point not in loop_nodes:
        size += 1
        loop_nodes.add(current_point)
        next_point_location = (current_point[0] + current_direction[0], current_point[1] + current_direction[1])
        next_point_value = new_input[next_point_location[1]][next_point_location[0]]
        # check the next point value
        
        # check for invalid / broken loops
        if current_direction == (0,1): # down
            invalid_pipes = ['-','7','F','.']
        elif current_direction == (1,0): # right
            invalid_pipes = ['|','L','F','.']
        elif current_direction == (0,-1): # up
            invalid_pipes = ['-','L','J','.']
        else:   # left
            invalid_pipes = ['|','J','7','.']
        if next_point_value in invalid_pipes:
            size = -1
            break
        # for the straight lines, keep on doing what we are doing
        # only need logic for the bends in the pipe
        if next_point_value == '7':
            if current_direction == (1,0):
                current_direction = (0,1)
            elif current_direction == (0,-1):
                current_direction = (-1,0)
        elif next_point_value == 'F':
            if current_direction == (0,-1):
                current_direction = (1,0)
            elif current_direction == (-1,0):
                current_direction = (0,1)
        elif next_point_value == 'J':
            if current_direction == (0,1):
                current_direction = (-1,0)
            elif current_direction == (1,0):
                current_direction = (0,-1)
        elif next_point_value == 'L':
            if current_direction == (0,1):
                current_direction = (1,0)
            elif current_direction == (-1,0):
                current_direction = (0,-1)
        current_point = next_point_location
    all_loop_sizes += [size]
    all_loop_nodes += [loop_nodes]
# Get max loop size
max_loop_size = max(all_loop_sizes)
max_loop_index = all_loop_sizes.index(max_loop_size)

print('Part 1: Maximum loop size is ' + str(max_loop_size // 2))

# Determine what S is.  Should only be two directions
dir1 = directions_to_check[0]
dir2 = directions_to_check[1]

if dir1 == (-1,0):
    if dir2 == (1,0):
        s_acts_as = '-'
    elif dir2 == (0,-1):
        s_acts_as = 'J'
    elif dir2 == (0,1):
        s_acts_as = '7'
elif dir1 == (0,-1):
    if dir2 == (0,1):
        s_acts_as = '|'
    elif dir2 == (-1,0):
        s_acts_as = 'J'
    elif dir2 == (1,0):
        s_acts_as = 'L'
elif dir1 == (1,0):
    if dir2 == (-1,0):
        s_acts_as = '-'
    elif dir2 == (0,1):
        s_acts_as = 'F'
    elif dir2 == (0,-1):
        s_acts_as = 'L'
else:
    if dir2 == (0,-1):
        s_acts_as = '|'
    elif dir2 == (-1,0):
        s_acts_as = '7'
    elif dir2 == (1,0):
        s_acts_as = 'F'
# Use shoestring theorem to get area inside of loop
max_loop = all_loop_nodes[max_loop_index]
points_inside = 0
for y, line in enumerate(new_input):
    # Start outside by default since we padded the input
    inside = False
    prev_corner = ''

    for x, point in enumerate(line):
        # Check to see if this is part of the loop
        if (x, y) in max_loop:
            # It's a point on the loop
            # Check for a corner
            point_value = new_input[y][x]
            if point_value == 'S':
                point_value = s_acts_as
            if point_value == 'F':
                if prev_corner == '':
                    prev_corner = 'F'
                else:
                    print()
            elif point_value == 'L':
                if prev_corner == '':
                    prev_corner = 'L'
                else:
                    print()
            elif point_value == '7':
                if prev_corner == 'F':
                    prev_corner = ''
                elif prev_corner == 'L':
                    prev_corner = ''
                    inside = not inside
                else:
                    print()
            elif point_value == 'J':
                if prev_corner == 'L':
                    prev_corner = ''
                elif prev_corner == 'F':
                    prev_corner = ''
                    inside = not inside
                else:
                    print()
            elif point_value == '|':
                inside = not inside
        else: # Not part of the loop
            if inside == True:
                points_inside += 1
print('Part 2: there are ' + str(points_inside) + ' points inside the loop.')