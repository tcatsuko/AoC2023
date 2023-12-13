raw_input = []
f = open('aoc13.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()

# Now organize into patterns
patterns = []
current_pattern = []
for line in raw_input:
    if line == '':
        patterns += [current_pattern]
        current_pattern = []
        continue
    line = line.replace('.','0')
    line = line.replace('#','1')
    current_pattern += [line]
patterns += [current_pattern]

def transpose(pattern):
    # First convert strings to list of characters
    new_pattern = []
    for line in pattern:
        new_pattern += [[x for x in line]]
    # Next, transpose the list of lists
    transposed_pattern = list(map(lambda *x: list(x), *new_pattern))
    temp_pattern = []
    # It's mirrored across y axis, fix that
    for idx, line in enumerate(transposed_pattern):
        line.reverse()
        temp_pattern += [''.join(line)]
    transposed_pattern = temp_pattern[:]
    return transposed_pattern

def convert_binary(pattern):
    binary_pattern = []
    for line in pattern:
        bin_value = int(line, base=2)
        binary_pattern += [bin_value]
    return binary_pattern

def find_mirror(pattern, part2=False, original=0):
    original -= 1 # Remember, we add 1 to found_index before returning
    for idx, line in enumerate(pattern):
        if idx == len(pattern) - 1:
            return -1
        current_line = line
        current_idx = idx
        next_line = pattern[idx + 1]
        next_idx = idx + 1
        if current_line == next_line:
            pattern_match = True
            found_idx = idx
            while (current_idx >= 0) and (next_idx < len(pattern)):
                current_line = pattern[current_idx]
                next_line = pattern[next_idx]
                if current_line == next_line:
                    current_idx -= 1
                    next_idx += 1
                else:
                    pattern_match = False
                    break
            if pattern_match == True:
                if part2 == False:
                    return found_idx + 1
                else:
                    if found_idx != original:
                        return found_idx + 1
    return -1

def fix_smudges(pattern, original_reflection):
    new_patterns = []
    for idx1 in range(len(pattern) - 1):
        current_line = pattern[idx1]
        for idx2 in range(idx1, len(pattern)):
            next_line = pattern[idx2]
            xor_mask = current_line ^ next_line
            if xor_mask.bit_count() == 1:
                new_pattern = pattern[:]
                new_current_line = current_line ^ xor_mask
                new_pattern[idx1] = new_current_line
                reflection = find_mirror(new_pattern, True, original_reflection)
                if reflection > -1:
                    return reflection
                break
    return -1

row_mirrors = []
column_mirrors = []
pattern_mirror_indices = []
for idx, pattern in enumerate(patterns):
    pattern_info = {}
    transposed_pattern = transpose(pattern) # To get vertical mirrors
    binary_pattern = convert_binary(pattern)
    binary_transposed = convert_binary(transposed_pattern)
    row_mirror = find_mirror(binary_pattern)
    if row_mirror > -1:
        row_mirrors += [row_mirror * 100]
    
    column_mirror = find_mirror(binary_transposed)
    if column_mirror > -1:
        column_mirrors += [column_mirror]
        
    pattern_info['row'] = row_mirror
    pattern_info['column'] = column_mirror
    pattern_mirror_indices += [pattern_info]

print('Part 1: notes summarized is ' + str(sum(row_mirrors) + sum(column_mirrors)))


row_mirrors = []
column_mirrors = []
for idx, pattern in enumerate(patterns):
    transposed_pattern = transpose(pattern)
    binary_pattern = convert_binary(pattern)
    binary_transposed = convert_binary(transposed_pattern)     
    # Check rows
    original_mirror = pattern_mirror_indices[idx]
    original_row = original_mirror['row']
    original_column = original_mirror['column']
    row_result = fix_smudges(binary_pattern, original_row)
    if row_result > -1:
        row_mirrors += [row_result * 100]
    col_result = fix_smudges(binary_transposed, original_column)
    if col_result > -1:
        column_mirrors += [col_result]

print('Part 2: notes summarized is ' + str(sum(row_mirrors) + sum(column_mirrors)))




    