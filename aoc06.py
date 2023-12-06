raw_input = []
f = open('aoc06.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
times = [int(x) for x in raw_input[0].split(':')[1].split()]
distances = [int(x) for x in raw_input[1].split(':')[1].split()]
races = []
for idx, time in enumerate(times):
    races += [(times[idx], distances[idx])]
# Part 1
ways_to_win = []
for race in races:
    time = race[0]
    distance = race[1]
    race_wins = 0
    for t in range(time - 1):
        distance_traveled = (time - t) * t
        if distance_traveled > distance:
            race_wins += 1
    ways_to_win += [race_wins]
part1 = 1
for win in ways_to_win:
    part1 *= win
print('Part 1: ' + str(part1))
# part 2
time = int(''.join(raw_input[0].split(':')[1].split()))
distance = int(''.join(raw_input[1].split(':')[1].split()))
race_wins = 0
for t in range(time - 1):
    distance_traveled = (time - t) * t
    if distance_traveled > distance:
        race_wins +=1
print('Part 2: ' + str(race_wins))