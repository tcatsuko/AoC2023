raw_input = []
f = open('aoc09.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()

def get_next_number(sequence):
    if all(x == 0 for x in sequence) == True:
        return 0
    # get the next line down
    next_sequence = []
    for x in range(len(sequence) - 1):
        current_number = sequence[x]
        next_number = sequence[x + 1]
        next_sequence += [next_number - current_number]
    return sequence[-1] + get_next_number(next_sequence)

# Now to process the data
next_number = 0
for line in raw_input:
    sequence = [int(x) for x in line.split()]
    next_number += get_next_number(sequence)
print('Part 1: sum of extrapolated values is ' + str(next_number))

# For part 2, should be able to just reverse the input sequences
next_number = 0
for line in raw_input:
    sequence = [int(x) for x in line.split()]
    sequence.reverse()
    next_number += get_next_number(sequence)
print('Part 2: sum of extrapolated values is ' + str(next_number))