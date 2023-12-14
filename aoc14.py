raw_input = []
f = open('aoc14.txt','rt')
for line in f:
    raw_input += [[x for x in line[:-1]]]
f.close()
def move_rocks(rock_map, part1 = True):
    
    # North
    # perform a first pass
    moves = 0
    for y in range(1, len(rock_map)):
        current_row = rock_map[y]
        previous_row = rock_map[y - 1]
        for x, item in enumerate(current_row):
            if item == 'O':
                # Check above
                if previous_row[x] == '.':
                    rock_map[y-1][x] = 'O'
                    rock_map[y][x] = '.'
                    moves += 1
    while moves != 0:
        moves = 0
        for y in range(1, len(rock_map)):
            current_row = rock_map[y]
            previous_row = rock_map[y - 1]
            for x, item in enumerate(current_row):
                if item == 'O':
                    # Check above
                    if previous_row[x] == '.':
                        rock_map[y-1][x] = 'O'
                        rock_map[y][x] = '.'
                        moves += 1
    if part1 == True:
        return rock_map
    # Move west
    for y in range(len(rock_map)):
        current_row = rock_map[y]
        moves = 0
        for x in range(1, len(rock_map)):
            if current_row[x] == 'O':
                if current_row[x - 1] == '.':
                    moves += 1
                    current_row[x - 1] = 'O'
                    current_row[x] = '.'
        while moves != 0:
            moves = 0
            for x in range(1, len(rock_map)):
                if current_row[x] == 'O':
                    if current_row[x - 1] == '.':
                        moves += 1
                        current_row[x - 1] = 'O'
                        current_row[x] = '.'
    # Move south
    rock_map.reverse()
    moves = 0
    for y in range(1, len(rock_map)):
        current_row = rock_map[y]
        previous_row = rock_map[y - 1]
        for x, item in enumerate(current_row):
            if item == 'O':
                # Check above
                if previous_row[x] == '.':
                    rock_map[y-1][x] = 'O'
                    rock_map[y][x] = '.'
                    moves += 1
    while moves != 0:
        moves = 0
        for y in range(1, len(rock_map)):
            current_row = rock_map[y]
            previous_row = rock_map[y - 1]
            for x, item in enumerate(current_row):
                if item == 'O':
                    # Check above
                    if previous_row[x] == '.':
                        rock_map[y-1][x] = 'O'
                        rock_map[y][x] = '.'
                        moves += 1
    rock_map.reverse()
    # East
    for y in range(len(rock_map)):
        current_row = rock_map[y]
        moves = 0
        current_row.reverse()
        for x in range(1, len(rock_map)):
            if current_row[x] == 'O':
                if current_row[x - 1] == '.':
                    moves += 1
                    current_row[x - 1] = 'O'
                    current_row[x] = '.'
        while moves != 0:
            moves = 0
            for x in range(1, len(rock_map)):
                if current_row[x] == 'O':
                    if current_row[x - 1] == '.':
                        moves += 1
                        current_row[x - 1] = 'O'
                        current_row[x] = '.'
        current_row.reverse()
    return rock_map


new_rock_map = move_rocks(raw_input)
new_rock_map.reverse()
rock_score = 0
for y in range(len(new_rock_map)):
    current_row = new_rock_map[y]
    rock_score += ((current_row.count('O')) * (y + 1))
print('Part 1: Rock score is ' + str(rock_score))

# Now for part 2
raw_input = []
f = open('aoc14.txt','rt')
for line in f:
    raw_input += [[x for x in line[:-1]]]
f.close()

def map_to_string(rock_map):
    output_string = ''
    for line in rock_map:
        output_string += ''.join(line)
    return output_string

rock_maps = []
rock_scores = []
for cycle in range(1000000000):
    raw_input = move_rocks(raw_input, False)
    raw_input.reverse()
    rock_score = 0
    for y in range(len(raw_input)):
        current_row = raw_input[y]
        rock_score += ((current_row.count('O')) * (y + 1))
    raw_input.reverse()
    map_string = map_to_string(raw_input)
    if map_string in rock_maps:
        current_cycle = cycle
        start_cycle = rock_maps.index(map_string)
        break
    rock_maps += [map_string]
    rock_scores += [rock_score]
cycle_length = current_cycle - start_cycle
leftover = 1000000000 - start_cycle
final_index = start_cycle + (leftover % cycle_length) - 1
final_score = rock_scores[final_index]

print('Part 2: Rock score is ' + str(final_score))

