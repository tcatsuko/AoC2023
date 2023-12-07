schematic = []
f = open('aoc03.txt','rt')
for line in f:
    schematic += ['.' + line[:-1] + '.']
f.close()
line_length = len(schematic[0])
schematic = ['.' * line_length] + schematic + ['.' * line_length]
print()
def check_chunk(chunk,row,colstart,colend,gears):
    is_part = False
    # Check first line
    for idx, character in enumerate(chunk[0]):
        if (not character.isdigit()) and (not (character == '.')):
            if character == '*':
                gear_location = (row - 1, colstart + idx - 1)
                if gear_location not in gears:
                    gears[gear_location] = [chunk[1][1:-1]]
                else:
                    gears[gear_location] += [chunk[1][1:-1]]
            is_part = True
    # Check first character of chunk row
    if (not chunk[1][0].isdigit()) and (not (chunk[1][0] == '.')):
        if chunk[1][0] == '*':
            gear_location = (row, colstart - 1)
            if gear_location not in gears:
                gears[gear_location] = [chunk[1][1:-1]]
            else:
                gears[gear_location] += [chunk[1][1:-1]]
        is_part = True
    # Check last character of chunk row
    if (not chunk[1][-1].isdigit()) and (not (chunk[1][-1] == '.')):
        if chunk[1][-1] == '*':
            gear_location = (row, colend + 1)
            if gear_location not in gears:
                gears[gear_location] = [chunk[1][1:-1]]
            else:
                gears[gear_location] += [chunk[1][1:-1]]
        is_part = True
    # Check last line
    for idx, character in enumerate(chunk[-1]):
        if (not character.isdigit()) and (not (character == '.')):
            if character == '*':
                gear_location = (row + 1, colstart + idx - 1)
                if gear_location not in gears:
                    gears[gear_location] = [chunk[1][1:-1]]
                else:
                    gears[gear_location] += [chunk[1][1:-1]]
                
            is_part = True
    
    return is_part
parts = []
gears = {}

for idx, x in enumerate(schematic):
    if idx == 0:
        continue
    #if idx == len(schematic) - 1:
    #    continue
    current_number = ''
    begin_index = -1
    end_index = -1
    for line_idx, item in enumerate(x):
        if item.isdigit():
            if begin_index == -1:
                begin_index = line_idx
            end_index = line_idx
            current_number += item
        elif not (item.isdigit()):
            if end_index > -1:

                chunk = [schematic[idx - 1][begin_index - 1:end_index + 2]] + [schematic[idx][begin_index - 1:end_index + 2]] + [schematic[idx + 1][begin_index - 1:end_index + 2]]
                is_part = check_chunk(chunk, idx, begin_index, end_index, gears)
                if is_part == True:
                    parts += [int(current_number)]
                
                current_number = ''
                begin_index = -1
                end_index = -1
print('Part 1: sum of part numbers is ' + str(sum(parts)))
gear_ratios = []
for location in gears:
    parts = gears[location]
    if len(parts) == 2:
        gear_ratios += [int(parts[0]) * int(parts[1])]
print('Part 2: sum of gear ratios is ' + str(sum(gear_ratios)))