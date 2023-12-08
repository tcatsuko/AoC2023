import itertools, math
raw_input = []
f = open('aoc08.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
instructions = raw_input[0]
instructions = instructions.replace('L','0')
instructions = instructions.replace('R','1')
node_map = {}
for line in raw_input[2:]:
    node, directions = line.split(' = ')
    left = directions.split(', ')[0][1:]
    right = directions.split(', ')[1][:-1]
    node_map[node] = (left, right)
steps = 0
target_node = 'ZZZ'
current_node = 'AAA'
for instruction in itertools.cycle(instructions):
    if current_node == target_node:
        break
    current_node = node_map[current_node][int(instruction)]
    steps += 1
print('Part 1: steps needed: ' + str(steps))
# Now find all nodes, will use lcm to get final answer
step_counts = []
start_nodes = []
for node in node_map:
    if node[-1] == 'A':
        start_nodes += [node]
for node in start_nodes:
    current_node = node
    
    steps = 0
    for instruction in itertools.cycle(instructions):
        #if current_node == target_node:
        if current_node[2] == 'Z': # note that a valid ending is ANY node with Z at the end
            break
        current_node = node_map[current_node][int(instruction)]
        steps += 1
    step_counts += [steps]
lcm_steps = math.lcm(*step_counts)
print('Part 2: steps needed: ' + str(lcm_steps))