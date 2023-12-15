raw_input = []
f = open ('aoc15.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
instructions = raw_input[0].split(',')
hash_values = []
def calculate_hash(instruction):
    hash_value = 0
    characters = [x for x in instruction]
    for character in characters:
        hash_value += ord(character)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value
for instruction in instructions:
    hash_value = calculate_hash(instruction)
    hash_values += [hash_value]
print('Part 1: sum of hash values is ' + str(sum(hash_values)))

# Get boxes ready
light_boxes = []
for x in range(256):
    light_boxes += [[]]
# Start to go through each light
for idx, lens in enumerate(instructions):
    
    
    if '-' in lens:
        name, power = lens.split('-')
        found_lens = False
        hash = calculate_hash(name)
        for x, item in enumerate(light_boxes[hash]):
            if name in item:
                found_lens = True
                lens_index = x
                break
        if found_lens == True:
            del light_boxes[hash][lens_index]
    else:
        # its an =
        name, power = lens.split('=')
        found_lens = False
        hash = calculate_hash(name)
        for idx, item in enumerate(light_boxes[hash]):
            if name in item:
                found_lens = True
                found_idx = idx
        if found_lens == True:
            light_boxes[hash][found_idx] = [name, power]
        else:
            light_boxes[hash] += [[name, power]]
# Calculate total power
total_power = 0
for raw_box_index, box in enumerate(light_boxes):
    box_index = raw_box_index + 1
    for raw_slot, contents in enumerate(box):
        slot = raw_slot + 1
        focal_length = int(contents[1])
        lens_power = box_index * slot * focal_length
        total_power += lens_power
print('Part 2: Total power is ' + str(total_power))