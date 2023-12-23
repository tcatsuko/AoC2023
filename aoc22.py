raw_input = []
f = open('aoc22.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
bricks = []
brick_info = {}

# Parse out the bricks
for line in raw_input:
    start, end = line.split('~')
    brick = [[int(x) for x in start.split(',')], [int(y) for y in end.split(',')]]
    # Sort so lower z comes first
    brick = sorted(brick, key=lambda z: z[2])
    brick = sorted(brick, key= lambda x: x[0])
    brick = sorted(brick, key = lambda y: y[1])
    bricks += [brick]
# Get the maximnum dimensions
bricks = sorted(bricks, key = lambda x: x[0][2])
max_x = 0
max_y = 0
max_z = bricks[-1][1][2]
for brick in bricks:
    if max(brick[0][0], brick[1][0]) > max_x:
        max_x = max(brick[0][0], brick[1][0])
    if max(brick[0][1], brick[1][1]) > max_y:
        max_y = max(brick[0][1], brick[1][1])
    if max(brick[0][2], brick[1][2]) > max_z:
        max_z = max(brick[0][2], brick[1][2])

# Come up with a ground plane
# ground_plane = []
# brick_bottoms = []
# brick_tops = []
# for z in range(max_z + 1):
#     brick_bottoms += [[]]
#     brick_tops += [[]]



# for y in range(max_y + 1):
#     current_line = [0] * (max_x + 1)
#     ground_plane += [current_line]

def brick_fall(max_x, max_y, bricks, part2 = False, ignored_brick = -1):
    ground_plane = []
    brick_bottoms = []
    brick_tops = []
    for z in range(max_z + 1):
        brick_bottoms += [[]]
        brick_tops += [[]]



    for y in range(max_y + 1):
        current_line = [0] * (max_x + 1)
        ground_plane += [current_line]

# Now, loop through each brick
    for brick_id, brick in enumerate(bricks):
        # Get orientation
        if part2 == True and brick_id == ignored_brick:
            continue
        brick_floor = 0
        brick_x = [brick[0][0], brick[1][0]]
        brick_y = [brick[0][1], brick[1][1]]
        brick_z = [brick[0][2], brick[1][2]]
        current_ground_plane = 0
        for y in range(brick_y[0], brick_y[1] + 1):
            for x in range(brick_x[0], brick_x[1] + 1):
                if ground_plane[y][x] > current_ground_plane:
                    current_ground_plane = ground_plane[y][x]
        # lowest a brick can go is current_ground_plane
        difference = brick[0][2] - current_ground_plane
        brick[0][2] -= difference
        brick[1][2] -= difference
        brick_bottoms[brick[0][2]] += [brick_id]
        brick_tops[brick[1][2] + 1] += [brick_id]
        # update the ground plane
        for y in range(brick_y[0], brick_y[1] + 1):
            for x in range(brick_x[0], brick_x[1] + 1):
                ground_plane[y][x] = brick[1][2] + 1
    # Now loop through the bricks to map out what is immediately above and below each
                
    # Attempt to 
    for idx, brick in enumerate(bricks):
        if idx not in brick_info:
            brick_info[idx] = {'on':set(), 'under':set()}
        low_z = brick[0][2]
        high_z = brick[1][2] + 1
        # First find bricks that support this one
        for supporting_brick_id in brick_tops[low_z]:
            if supporting_brick_id not in brick_info:
                brick_info[supporting_brick_id] = {'on':set(), 'under':set()}
            brick_x = (brick[0][0], brick[1][0])
            brick_y = (brick[0][1], brick[1][1])
            brick_z = (brick[0][2], brick[1][2])
            sb = bricks[supporting_brick_id]
            for y in range(brick_y[0], brick_y[1] + 1):
                for x in range(brick_x[0], brick_x[1] + 1):
                    if x >=  sb[0][0] and x <= sb[1][0] and y >= sb[0][1] and y <= sb[1][1]:
                        # The supporting brick does in fact support this brick
                        brick_info[idx]['on'].add(supporting_brick_id)
                        brick_info[supporting_brick_id]['under'].add(idx)
    return (ground_plane, brick_bottoms, brick_tops, brick_info)

ground_plane, brick_bottoms, brick_tops, brick_info = brick_fall(max_x, max_y, bricks)

bricks_to_remove = 0
for brick_idx in brick_info:
    brick_data = brick_info[brick_idx]
    under_bricks = list(brick_data['under'])
    can_remove = True
    for top_brick in under_bricks:
        if len(brick_info[top_brick]['on']) == 1:
            can_remove = False
    if can_remove == True:
        bricks_to_remove += 1
print('Part 1: can remove ' + str(bricks_to_remove) + ' bricks.')    

num_of_bricks = len(raw_input)
total_sum = 0

for i in range(num_of_bricks):
    blocks_fallen = set()
    _,new_brick_bottoms, new_brick_tops, _ = brick_fall(max_x, max_y, bricks, True, i)
    for z in range(max_z + 1):
        old_bottom =  set(brick_bottoms[z])
        new_bottom = set(new_brick_bottoms[z])
        differences = new_bottom - old_bottom
        for difference in differences:
            blocks_fallen.add(difference)
    total_sum += len(blocks_fallen)
print('Part 2: total sum is ' + str(total_sum))