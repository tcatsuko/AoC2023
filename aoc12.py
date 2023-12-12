from functools import cache

raw_input = []
f = open('aoc12.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
patterns= []
conditions  = []
for line in raw_input:
    pattern, condition= line.split(' ')
    patterns += [pattern]
    conditions += [tuple(int(x) for x in condition.split(','))]

@cache
def find_matches(pattern, condition):
    # First determine if both are empty.  If so, return 1
    # Get rid of leading dots, we don't need them
    pattern = pattern.lstrip('.')
    
    if pattern == '':
        if condition == ():
            return 1
        else:
            return 0

    # If empty condition, check to see if a spring is present in the patern.  If not, it's effectively the same as an empty pattern
    if condition == ():
        if pattern.find('#') == -1:
            return 1
        else:
            return 0
    
    # Check to see if the first part of the pattern starts with a known spring
    if pattern[0] == '#':
        # is there enough space for the initial condition??
        firstCondition = condition[0]
        if (len(pattern) < firstCondition) or ('.' in pattern[:firstCondition]):
            return 0    # Not enough space to fit the first spring
        elif len(pattern) == firstCondition: # Exactly enough space for the condition
            # Is there just one condition to check?  
            if len(condition) == 1:
                return 1
            else:
                return 0 #there are two conditions to check, but only room for the first one
        elif pattern[firstCondition] == '#':
            # The next part of the pattern after the first condition to be tested is a spring, so this is invalid
            return 0
        else:
            # Remove a spring, continue onward
            return find_matches(pattern[firstCondition + 1:],condition[1:])
    # The first character is a ?.  Change it to a "#" and check.  Also just march down to the right as well

    val1 = find_matches('#' + pattern[1:], condition)
    val2 = find_matches(pattern[1:], condition)
    return val1 + val2
valid_conditions = 0
for idx, pattern in enumerate(patterns):
    valid_conditions += find_matches(pattern, conditions[idx])
print('Part 1: there are ' + str(valid_conditions) + ' valid conditions') 

valid_conditions = 0
# now for part 2
for idx, pattern in enumerate(patterns):
    new_pattern = pattern + '?'
    new_pattern = new_pattern * 5
    new_pattern = new_pattern[:-1]
    condition = list(conditions[idx])
    condition = condition * 5
    condition = tuple(condition)
    valid_conditions += find_matches(new_pattern, condition)
print('Part 2: there are ' + str(valid_conditions) + ' valid conditions') 