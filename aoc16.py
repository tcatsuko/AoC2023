raw_input = []
f = open('aoc16.txt','rt')
for line in f:
    raw_input += [[x for x in line[:-1]]]
f.close()
height = len(raw_input)
width = len(raw_input[0])
# Add a border around the original raw input to make things a little easier
top_border = [x for x in ('%' * (width + 2))]
for y in range(height):
    raw_input[y].insert(0, '%')
    raw_input[y] += ['%']
raw_input.insert(0, top_border)
raw_input += [top_border]
# Top left corner is now (1,1)
light_beams = [[(0, 1),(1, 0)]]

def get_energized_tiles(start_point_dir):
    global raw_input
    light_beams = []
    light_beams += [[start_point_dir[0], start_point_dir[1]]]
    visited_loc_dir = set()
    height = len(raw_input)
    width = len(raw_input[0])
    light_map = []
    for y in range(height - 1):
        current_row = []
        for x in range(width - 1):
            current_row += '.'
        light_map += [current_row]
    while len(light_beams) > 0:
        location, direction = light_beams.pop(0)
        while True:
            # We just keep moving until we encounter '%' (wall) or a splitter
            new_location = (location[0] + direction[0], location[1] + direction[1])
            new_x = new_location[0]
            new_y = new_location[1]
            new_location_value = raw_input[new_location[1]][new_location[0]]
            loc_dir = (new_x, new_y, direction[0], direction[1])
            if loc_dir in visited_loc_dir:
                break
            visited_loc_dir.add(loc_dir)
            if new_location_value != '%':
                light_map[new_y - 1][new_x - 1] = '#'
                location = new_location
            else:
                break
            if new_location_value == '/':
                if direction == (1,0):
                    direction = (0, -1)
                elif direction == (0, 1):
                    direction = (-1, 0)
                elif direction == (0, -1):
                    direction = (1, 0)
                elif direction == (-1, 0):
                    direction = (0, 1)
            elif new_location_value == '\\':
                if direction == (1, 0):
                    direction = (0, 1)
                elif direction == (0, -1):
                    direction = (-1, 0)
                elif direction == (0, 1):
                    direction = (1, 0)
                elif direction == (-1, 0):
                    direction = (0, -1)
            elif new_location_value == '-':
                if (direction == (0, 1)) or (direction == (0, -1)):
                    light_beams += [[location, (-1, 0)]]
                    light_beams += [[location, (1, 0)]]
                    break
            elif new_location_value == '|':
                if (direction == (1, 0)) or (direction == (-1, 0)):
                    light_beams += [[location, (0, 1)]]
                    light_beams += [[location, (0, -1)]]
                    break
    # Count visited tiles
    energized_tiles = 0
    for row in light_map:
        full_row = ''.join(row)
        energized_tiles += full_row.count('#')
    return energized_tiles
part1 = get_energized_tiles([(0,1),(1,0)])
print('Part 1: there are ' + str(part1) + ' energized tiles.')
largest_energized = 0
for y in range(1, len(raw_input) - 1):
    # Check all left sides
    current_energized = get_energized_tiles([(0, y),(1,0)])
    if current_energized > largest_energized:
        largest_energized = current_energized
    current_energized = get_energized_tiles([(len(raw_input[0])-1, y),(-1,0)])
    if current_energized > largest_energized:
        largest_energized = current_energized
for x in range(1, len(raw_input[0]) - 1):
    current_energized = get_energized_tiles([(x, 0),(0,1)])
    if current_energized > largest_energized:
        largest_energized = current_energized
    current_energized = get_energized_tiles([(x, len(raw_input)-1),(0,-1)])
    if current_energized > largest_energized:
        largest_energized = current_energized
print('Part 2: largest energized has ' + str(largest_energized) + ' blocks.')
