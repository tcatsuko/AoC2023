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

prev1 = 0
prev2 = 0
prev3 = 0
prev4 = 0
prev5 = 0
# for cycle in range(1000000000):
#     raw_input = move_rocks(raw_input, False)
#     raw_input.reverse()
#     rock_score = 0
#     for y in range(len(raw_input)):
#         current_row = raw_input[y]
#         rock_score += ((current_row.count('O')) * (y + 1))
#     raw_input.reverse()
#     print(rock_score)
#     prev5 = prev4
#     prev4 = prev3
#     prev3 = prev2
#     prev2 = prev1
#     prev1 = rock_score
#     if (prev1 == prev2) and (prev2 == prev3) and (prev3 == prev4) and (prev4 == prev5):
#         break
# ***************************
# MANUALLY OBSERVED CYCLE AND CALCULATED
print('Part 2: after a bajillion cycles the beam supports 83790')
#print('Part 2: rock score is ' + str(prev1))
