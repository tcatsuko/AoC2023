raw_input = []
f = open('aoc11.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
galaxies = []
empty_columns = []
empty_rows = []
expansions = 2 # Making the empty column / row twice as large

# Populate the range of empty columns, we will remove indices from here as we find galaxies
for x in range(len(raw_input[0])):
    empty_columns += [x]
    
# Loop through the input, get a list of galaxies and empty rows / columns
for y in range(len(raw_input)):
    empty_row = True
    for x in range(len(raw_input[0])):
        if raw_input[y][x] == '#':
            galaxies += [(x,y)]
            empty_row = False
            if x in empty_columns:
                empty_columns.remove(x)
    if empty_row == True:
        empty_rows += [y]

def get_col_expansion(galaxy1, galaxy2, empty_columns):
    col_expansion = 0
    x1 = galaxy1[0]
    x2 = galaxy2[0]
    if x2 > x1:
        for x in range(x1, x2 + 1):
            if x in empty_columns:
                col_expansion += 1
    elif x1 > x2:
        for x in range(x2, x1 + 1):
            if x in empty_columns:
                col_expansion += 1
    return col_expansion

def get_row_expansion(galaxy1, galaxy2, empty_rows):
    row_expansion = 0
    y1 = galaxy1[1]
    y2 = galaxy2[1]
    if y2 > y1:
        for y in range(y1, y2 + 1):
            if y in empty_rows:
                row_expansion += 1
    elif y1 > y2:
        for y in range(y2, y1 + 1):
            if y in empty_rows:
                row_expansion += 1
    return row_expansion

def get_manhattan(galaxy1, galaxy2):
    x1 = galaxy1[0]
    x2 = galaxy2[0]
    y1 = galaxy1[1]
    y2 = galaxy2[1]
    
    if (x2 > x1):
        x_dist = x2 - x1
    elif (x1 > x2):
        x_dist = x1 - x2
    else:
        x_dist = 0

    if (y2 > y1):
        y_dist = y2 - y1
    elif (y1 > y2):
        y_dist = y1 - y2
    else:
        y_dist = 0
    return (x_dist + y_dist)

part1_galaxies = galaxies[:]
galaxy_distances = []
while len(part1_galaxies) > 0:
    galaxy1 = part1_galaxies.pop()
    for galaxy2 in part1_galaxies:
        col_expansion = get_col_expansion(galaxy1, galaxy2, empty_columns)
        row_expansion = get_row_expansion(galaxy1, galaxy2, empty_rows)
        raw_manhattan = get_manhattan(galaxy1, galaxy2)
        raw_manhattan += (col_expansion * (expansions - 1)) # Make sure to subtract the original column
        raw_manhattan += (row_expansion * (expansions - 1)) # Make sure to subtract the original row
        galaxy_distances += [raw_manhattan]
print('Part 1: sum of all distances is ' + str(sum(galaxy_distances)))

#part2
expansions = 1000000 # Making empty columns/rows  1,000,000 times larger
part2_galaxies = galaxies[:]
galaxy_distances = []
while len(part2_galaxies) > 0:
    galaxy1 = part2_galaxies.pop()
    for galaxy2 in part2_galaxies:
        col_expansion = get_col_expansion(galaxy1, galaxy2, empty_columns)
        row_expansion = get_row_expansion(galaxy1, galaxy2, empty_rows)
        raw_manhattan = get_manhattan(galaxy1, galaxy2)

        raw_manhattan += (col_expansion * (expansions - 1)) # Make sure to subtract the original column
        raw_manhattan += (row_expansion * (expansions - 1)) # Make sure to subtract the original row
        galaxy_distances += [raw_manhattan]
print('Part 2: sum of all distances is ' + str(sum(galaxy_distances)))