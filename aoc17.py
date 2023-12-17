import sys
from queue import PriorityQueue
from collections import defaultdict


heat_map = []
f = open('aoc17.txt','rt')
for line in f:
    heat_map += [[int(x) for x in line[:-1]]]
f.close()

dir_right = (1,0)
dir_left = (-1,0)
dir_up = (0,-1)
dir_down = (0,1)
turns = {dir_right:[dir_up, dir_down], dir_left:[dir_up, dir_down], dir_up: [dir_left, dir_right], dir_down: [dir_left, dir_right]}
c_heat_loss = defaultdict(lambda: defaultdict(lambda:sys.maxsize))
#put in starting node.  Starts with heat loss of 0 going in every direction
c_heat_loss[(0,0)][dir_right] = 0
c_heat_loss[(0,0)][dir_left] = 0
c_heat_loss[(0,0)][dir_up] = 0
c_heat_loss[(0,0)][dir_down] = 0
dj = PriorityQueue() # Poor man's Djikstra
dj.put((0, (0,0), dir_right)) # Start at 0,0, move right
dj.put((0, (0,0), dir_down) ) # Start at 0,0., move down

while not dj.empty():
    heat_loss, position, direction = dj.get()
    if heat_loss > c_heat_loss[position][direction]:
        # We have been here before, and now we have higher heat loss.  Stop this branch
        continue
    x_pos, y_pos = position

    # Now move
    for i in range(3):
        x_pos = x_pos + direction[0]
        y_pos = y_pos + direction[1]
        # Check if out of bounds
        if (x_pos < 0) or (x_pos >= len(heat_map[0])) or (y_pos < 0) or (y_pos >= len(heat_map)):
            break
        heat_loss += heat_map[y_pos][x_pos]

        # Turn our movement now
        for next_dir in turns[direction]:
            if heat_loss < c_heat_loss[(x_pos,y_pos)][next_dir]:
                c_heat_loss[(x_pos,y_pos)][next_dir] = heat_loss
                dj.put((heat_loss, (x_pos,y_pos),next_dir))


end_point_x = len(heat_map[0]) - 1
end_point_y = len(heat_map) - 1
endpoint_values = c_heat_loss[(end_point_x, end_point_y)].values()
print('Part 1: minimum heat loss is ' + str(min(endpoint_values)))

# Now for part 2.
c_heat_loss = defaultdict(lambda: defaultdict(lambda:sys.maxsize))
#put in starting node
c_heat_loss[(0,0)][dir_right] = 0
c_heat_loss[(0,0)][dir_left] = 0
c_heat_loss[(0,0)][dir_up] = 0
c_heat_loss[(0,0)][dir_down] = 0
dj = PriorityQueue()
dj.put((0, (0,0), dir_right)) # Start at 0,0, move right
dj.put((0, (0,0), dir_down) ) # Start at 0,0., move down
while not dj.empty():
    heat_loss, position, direction = dj.get()
    if heat_loss > c_heat_loss[position][direction]:
        # We have been here before, and now we have higher heat loss.  Stop this branch
        continue
    x_pos, y_pos = position

    # Now move
    for i in range(10):
        x_pos = x_pos + direction[0]
        y_pos = y_pos + direction[1]
        # Check if out of bounds
        if (x_pos < 0) or (x_pos >= len(heat_map[0])) or (y_pos < 0) or (y_pos >= len(heat_map)):
            break
        # Add the heat loss for this step. 
        heat_loss += heat_map[y_pos][x_pos]

        if i < 3:
            # minimum of 4 moves in a direction
            continue

        # Turn our movement now
        for next_dir in turns[direction]:
            if heat_loss < c_heat_loss[(x_pos,y_pos)][next_dir]: # If we haven't seen the next node yet then the heat los is sys.maxsize
                c_heat_loss[(x_pos,y_pos)][next_dir] = heat_loss
                dj.put((heat_loss, (x_pos,y_pos),next_dir))

endpoint_values = c_heat_loss[(end_point_x, end_point_y)].values()
print('Part 2: minimum heat loss is ' + str(min(endpoint_values)))