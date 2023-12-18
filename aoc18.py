raw_input = []
f = open('aoc18.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()

# Going to use Pick's Theorem and shoelace formula
def det(p1, p2):
    return (p1[0] * p2[1]) - (p1[1] * p2[0])

instructions = []
colors = []
coordinates = []
perimeter = 0
for line in raw_input:
    instruction, length, color = split_line = line.split()
    colors += [color[2:-1]]
    perimeter += int(length)
    instructions += [(instruction, int(length))]
def shoelace_area(coordinates):
    doubled_area = 0
    for x in range(len(coordinates) - 1):
        a = coordinates[x]
        b = coordinates[x + 1]
        doubled_area += det(a, b)
    doubled_area += det(coordinates[0], coordinates[-1])
    return (doubled_area / 2)

# Now, find out the coordinates
next_dir = {'U':(0,-1), 'D':(0,1), 'L':(-1,0), 'R':(1,0), '0':(1,0), '1':(0,1), '2':(-1,0), '3':(0,-1)}

current_point = (0,0)
coordinates += [current_point]
for instruction in instructions:
    direction, length = instruction
    amount_to_add = tuple(length * x for x in next_dir[direction])
    current_point = (current_point[0] + amount_to_add[0], current_point[1] + amount_to_add[1])
    coordinates += [current_point]

polygon_area = shoelace_area(coordinates)
# i + b = A + b/2 + 1
# i = points interior to polygon
# b = border points
# A = area of polygon
total_area = int(polygon_area + (perimeter / 2) + 1)
print('Part 1: total area is ' + str(total_area))
coordinates = []
perimeter = 0
current_point = (0,0)
coordinates += [current_point]
for color in colors:
    direction = color[-1]
    length = int(color[:-1], 16)
    perimeter += length
    
    amount_to_add = tuple(length * x for x in next_dir[direction])
    current_point = (current_point[0] + amount_to_add[0], current_point[1] + amount_to_add[1])
    coordinates += [current_point]
polygon_area = shoelace_area(coordinates)
# i + b = A + b/2 + 1
# i = points interior to polygon
# b = border points
# A = area of polygon
total_area = int(polygon_area + (perimeter / 2) + 1)
print('Part 2: total area is ' + str(total_area))