raw_input = []
f = open('aoc02.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
# Parse the input
games = {}
good_games = []
bad_games = set()
powers = []
total_red = 12
total_blue = 14
total_green = 13
for line in raw_input:
    game_number = int(line.split(':')[0].split(' ')[1])
    current_game = {'red':0, 'blue':0, 'green':0}
    game_info = line.split(': ')[1]
    cube_sets = game_info.split('; ')
    cube_minimums = {'red':0, 'blue':0, 'green':0}
    for cube_set in cube_sets:
        cubes = cube_set.split(', ')
        current_pull = {'red':0, 'blue':0, 'green':0}
        for cube in cubes:
            [num, color] = cube.split(' ')
            current_pull[color] = int(num)
        for color in current_pull:
            if current_pull[color] > cube_minimums[color]:
                cube_minimums[color] = current_pull[color]
        if current_pull['red'] > total_red or current_pull['green'] > total_green or current_pull['blue'] > total_blue:
            bad_games.add(game_number)
    power = cube_minimums['red'] * cube_minimums['blue'] * cube_minimums['green']
    powers += [power]
    if game_number not in bad_games:
        good_games += [game_number]
print('Part 1: sum of good game IDs is ' + str(sum(good_games)))
print('Part 2: sum of powers is ' + str(sum(powers)))

