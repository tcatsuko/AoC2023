raw_input = []
f = open('aoc21.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
from collections import deque
import numpy as np

# find starting point
def get_steps(in_map, steps_needed):
    # for the real input, start point is in the center


    if steps_needed > 64:
        # Increase the map 6-fold
        raw_input = []
        for n in range(5):
            for line in in_map:
                raw_input += [5 * line]
    else:
        raw_input = in_map[:]
    x = len(raw_input) // 2
    y = len(raw_input[0]) // 2
    visited_points = set()
    step_queue = deque()
    reachable_points = set()
    start_point = (x, y, 0)
    step_queue.append(start_point)
    step_queue.append((x, y, 0))
    while step_queue:
        current_point = step_queue.popleft()
        if current_point in visited_points:
            continue
        visited_points.add(current_point)
        if current_point[2] == steps_needed:
            reachable_points.add(current_point)
        else:
            x = current_point[0]
            y = current_point[1]
            current_step = current_point[2]
            # Move left
            if x > 0:
                if raw_input[y][x - 1] != '#':
                    step_queue.append((x - 1, y, current_step + 1))
            # move up
            if y > 0:
                if raw_input[y - 1][x] != '#':
                    step_queue.append((x, y - 1, current_step + 1))
            # move right
            if x < (len(raw_input[0]) - 1):
                if raw_input[y][x + 1] != '#':
                    step_queue.append((x + 1, y, current_step + 1))
            # move down
            if y < (len(raw_input) - 1):
                if raw_input[y + 1][x] != '#':
                    step_queue.append((x, y + 1, current_step + 1))
    return len(reachable_points)
    
part1 =get_steps(raw_input, 64)
print('Part 1: you can reach ' + str(part1) + ' points.')
print()
# Looked at discussion, and this one will be fun for part 2.
# Saw that the number needed is 26501365, which is 202300 * 131 + 65
# 131 is length, width of the input
# Can solve using vandermonde, since it's an increasing sum of previous answers in sequence
# Also checkerboard -- flip flops between odd and even

v1 = get_steps(raw_input,65)
print('v1: ' + str(v1))
v2 = get_steps(raw_input, 65 + 131)
print('v2: ' + str(v2))
v3 = get_steps (raw_input, 65 + 131 * 2)



print('v3: ' + str(v3))
# Vandermonde:
# [0, 0, 1][x0]   [v1]
# [1, 1, 1][x1] = [v2]
# [4, 2, 1][x2]   [v3]

n = 202300
# Final answer is a quadratic
# part2 = ax^2 + bx + c
vm = [[0,0,1],[1,1,1],[4,2,1]]
x = np.linalg.solve(vm, np.array([v1, v2, v3])).astype(np.int64)
a = x[0]
b = x[1]
c = x[2]

part2 = (a * n * n) + (b * n) + c

print('Part 2: ' + str(part2))
# 316929390042244 too low
# 1794465006404533 too high
# 3988565464179253 possible
# 636391426712747 answer

                
