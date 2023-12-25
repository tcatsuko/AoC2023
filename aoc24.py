raw_input = []
f = open('aoc24.txt','rt')
from z3 import *
for line in f:
    raw_input += [line[:-1]]
f.close()
hailstones = {}
for line in raw_input:
    position_txt, velocity_txt = line.split(' @ ')
    position = tuple([int(x) for x in position_txt.split(', ')])
    velocity = [int(x) for x in velocity_txt.split(', ')]
    hailstones[position] = velocity
print()

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x1 == x2 and y1 == y2) or (x3==x4 and y3 == y4):
        return False
    denom = ((y4 - y3)* (x2 - x1) - (x4 - x3) * (y2 - y1))

    if denom == 0:
        # lines are parallel
        return False
    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

    # if (ua < 0 or ua > 1 or ub < 0 or ub > 1):
    #     return False
    
    x = x1 + ua * (x2 - x1)
    y = y1 + ua * (y2 - y1)

    return (x, y)
hailstone_list = list(hailstones.keys())
num_intersections = 0
low_range = 200000000000000
high_range = 400000000000000

for idx, p1 in enumerate(hailstone_list):
    for idx2 in range(idx + 1, len(hailstone_list)):
        x1, y1, z1 = p1
        p1_v = hailstones[p1]
        x2 = x1 + p1_v[0]
        y2 = y1 + p1_v[1]
        p2 = hailstone_list[idx2]
        x3, y3, z3 = hailstone_list[idx2]
        p2_v = hailstones[(x3, y3, z3)]
        x4 = x3 + p2_v[0]
        y4 = y3 + p2_v[1]
        intersection = intersect(x1, y1, x2, y2, x3, y3, x4, y4)

        if intersection != False:
            # get time
            int_x = int(intersection[0])
            int_y = int(intersection[1])
            x1_time = (int_x - x1) / p1_v[0]
            y1_time = (int_y - y1) / p1_v[1]
            x2_time = (int_x - x3) / p2_v[0]
            y2_time = (int_y - y3) / p2_v[1]
            
            if int(intersection[0]) in range(low_range, high_range + 1) and int(intersection[1]) in range(low_range, high_range + 1):
                if (x1_time > 0 and y1_time > 0 and x2_time > 0 and y2_time > 0):
                    num_intersections += 1

print('Part 1: ' + str(num_intersections))
rock_x, rock_y, rock_z = Ints('rock_x, rock_y, rock_z')
rock_vx, rock_vy, rock_vz = Ints('rock_vx, rock_vy, rock_vz')
t1, t2, t3 = Ints('t1, t2, t3')
part2 = Int('part2')
h1_x, h1_y, h1_z = hailstone_list[0]
h1_vx, h1_vy, h1_vz = hailstones[hailstone_list[0]]
h2_x, h2_y, h2_z = hailstone_list[1]
h2_vx, h2_vy, h2_vz = hailstones[hailstone_list[1]]
h3_x, h3_y, h3_z = hailstone_list[2]
h3_vx, h3_vy, h3_vz = hailstones[hailstone_list[2]]

solve(
    rock_x + t1 * rock_vx == h1_x + t1 * h1_vx,
    rock_y + t1 * rock_vy == h1_y + t1 * h1_vy,
    rock_z + t1 * rock_vz == h1_z + t1 * h1_vz,
    rock_x + t2 * rock_vx == h2_x + t2 * h2_vx,
    rock_y + t2 * rock_vy == h2_y + t2 * h2_vy,
    rock_z + t2 * rock_vz == h2_z + t2 * h2_vz,
    rock_x + t3 * rock_vx == h3_x + t3 * h3_vx,
    rock_y + t3 * rock_vy == h3_y + t3 * h3_vy,
    rock_z + t3 * rock_vz == h3_z + t3 * h3_vz,
    part2 == rock_x + rock_y + rock_z,

)
