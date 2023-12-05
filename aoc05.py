raw_input = []

f = open('aoc05.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
# Start to parse
# Get seed numbers
seed_numbers_raw = raw_input[0]
seeds = [int(x) for x in seed_numbers_raw.split(': ')[1].split()]
# Get rid of that part of the input
raw_input = raw_input[3:]
# seed-to-soil
seed_soil = {}
for idx, line in enumerate(raw_input):
    if line == '':
        new_input = raw_input[idx+2:]
        break
    [soil_start, seed_start, val_range] = [int(x) for x in line.split()]
    seed_soil[seed_start] = {'soil':soil_start, 'range':val_range}
raw_input = new_input[:]
# soil-to-fertilizer
soil_fert = {}
for idx, line in enumerate(raw_input):
    if line == '':
        new_input = raw_input[idx+2:]
        break
    [fert_start, soil_start, val_range] = [int(x) for x in line.split()]
    soil_fert[soil_start] = {'fert':fert_start, 'range':val_range}
raw_input = new_input[:]
# fertilizer-to-water
fert_water = {}
for idx, line in enumerate(raw_input):
    if line == '':
        new_input = raw_input[idx+2:]
        break
    [water_start, fert_start, val_range] = [int(x) for x in line.split()]
    fert_water[fert_start] = {'water':water_start, 'range':val_range}
raw_input = new_input[:]
# water-to-light
water_light = {}
for idx, line in enumerate(raw_input):
    if line == '':
        new_input = raw_input[idx+2:]
        break
    [light_start, water_start, val_range] = [int(x) for x in line.split()]
    water_light[water_start] = {'light':light_start, 'range':val_range}
raw_input = new_input[:]
# light-to-temp
light_temp = {}
for idx, line in enumerate(raw_input):
    if line == '':
        new_input = raw_input[idx+2:]
        break
    [temp_start, light_start, val_range] = [int(x) for x in line.split()]
    light_temp[light_start] = {'temp':temp_start, 'range':val_range}
raw_input = new_input[:]
# temp-to-humidity
temp_humid = {}
for idx, line in enumerate(raw_input):
    if line == '':
        new_input = raw_input[idx+2:]
        break
    [humid_start, temp_start, val_range] = [int(x) for x in line.split()]
    temp_humid[temp_start] = {'humid':humid_start, 'range':val_range}
raw_input = new_input[:]
# humidity-to-location
humid_location = {}
for idx, line in enumerate(raw_input):
    if line == '':
        
        break
    [location_start, humid_start, val_range] = [int(x) for x in line.split()]
    humid_location[humid_start] = {'location':location_start, 'range':val_range}

#Now that input is parsed, start to look at seeds
seed_info = {}

for seed in seeds:

# First find soil
    seed_info[seed] = {}
    seed_info[seed]['soil'] = seed # By default if it's not mapped somewhere it's the same as source
    for seed_start in seed_soil:
        val_range = seed_soil[seed_start]['range']
        seed_end = seed_start + val_range - 1
        soil_start = seed_soil[seed_start]['soil']
        if (seed >= seed_start) and (seed <= seed_end):
            offset = seed - seed_start
            seed_info[seed]['soil'] = soil_start + offset

    # Next find fertilizer
    current_soil = seed_info[seed]['soil']
    seed_info[seed]['fert'] = current_soil
    for soil_start in soil_fert:
        val_range = soil_fert[soil_start]['range']
        soil_end = soil_start + val_range - 1
        fert_start = soil_fert[soil_start]['fert']
        if (current_soil >= soil_start) and (current_soil <= soil_end):
            offset = current_soil - soil_start
            seed_info[seed]['fert'] = fert_start + offset
    # Next find water
    current_fert = seed_info[seed]['fert']
    seed_info[seed]['water'] = current_fert
    for fert_start in fert_water:
        val_range = fert_water[fert_start]['range']
        fert_end = fert_start + val_range - 1
        water_start = fert_water[fert_start]['water']
        if (current_fert >= fert_start) and (current_fert <= fert_end):
            offset = current_fert - fert_start
            seed_info[seed]['water'] = water_start + offset

    # Next find water-to-light
    current_water = seed_info[seed]['water']
    seed_info[seed]['light'] = current_water
    for water_start in water_light:
        val_range = water_light[water_start]['range']
        water_end = water_start + val_range - 1
        light_start = water_light[water_start]['light']
        if (current_water >= water_start) and (current_water <= water_end):
            offset = current_water - water_start
            seed_info[seed]['light'] = light_start + offset

    # Next find light-to-temp
    current_light = seed_info[seed]['light']
    seed_info[seed]['temp'] = current_light
    for light_start in light_temp:
        val_range = light_temp[light_start]['range']
        light_end = light_start + val_range - 1
        temp_start = light_temp[light_start]['temp']
        if (current_light >= light_start) and (current_light <= light_end):
            offset = current_light - light_start
            seed_info[seed]['temp'] = temp_start + offset

    # Next find humidity
    current_temp = seed_info[seed]['temp']
    seed_info[seed]['humid'] = current_temp
    for temp_start in temp_humid:
        val_range = temp_humid[temp_start]['range']
        temp_end = temp_start + val_range - 1
        humid_start = temp_humid[temp_start]['humid']
        if (current_temp >= temp_start) and (current_temp <= temp_end):
            offset = current_temp - temp_start
            seed_info[seed]['humid'] = humid_start + offset

    # Finally, get location
    current_humid = seed_info[seed]['humid']
    seed_info[seed]['location'] = current_humid
    for humid_start in humid_location:
        val_range = humid_location[humid_start]['range']
        humid_end = humid_start + val_range - 1
        location_start = humid_location[humid_start]['location']
        if (current_humid >= humid_start) and (current_humid <= humid_end):
            offset = current_humid - humid_start
            seed_info[seed]['location'] = location_start + offset

lowest_location = float('inf')
for seed in seed_info:
    if seed_info[seed]['location'] < lowest_location:
        lowest_location = seed_info[seed]['location']
part_1_lowest = lowest_location

# Now for part 2.  It's a doozy.
lowest_location = float('inf')
# Get seed ranges
seed_ranges = []
for x in range(0, len(seeds), 2):
    seed_ranges += [(seeds[x], seeds[x] + seeds[x+1] - 1)]



seed_range = seed_ranges[0]
def check_overlap(range1, range2):
    x1 = range1[0]
    x2 = range1[1]
    y1 = range2[0]
    y2 = range2[1]
    return (x2 >= y1) and (x1 <= y2)
def split_ranges(source, dest, start_map):
    x1 = source[0]
    x2 = source[1]
    y1 = dest[0]
    y2 = dest[1]
    # x1---y1---x2---y2
    return_range = []
    if (x1 < y1) and (y1 < x2):
        return_range += [(x1, y1-1)]
        return_range += [(start_map, (x2 - y1) + start_map)]
    # x1y1---x2---y2
    elif (x1 == y1) and (x2 < y2):
        return_range += [(start_map, start_map + x2-x1)]
    # x1---y1---x2y2
    elif (x1 < y1) and (x2 == y2):
        return_range += [(x1, y1-1)]
        return_range += [(start_map, y2-y1+start_map)]
    # y1---x1---y2---x2
    elif(y1 < x1) and (x1 < y2) and (x2 > y2):
        
        return_range += [(y2 + 1, x2)]
        return_range += [(start_map + x1 - y1, start_map + y2 - y1)]
    # x1y1---y2---x2
    elif(x1 == y1) and (y2 < x2):
        
        return_range += [(y2 + 1, x2)]
        return_range += [(start_map, start_map + y2 - y1)]
    # y1---x1---x2y2
    elif(x1 > y1) and (x2 == y2):
        return_range += [(start_map + x1 - y1, start_map + y2 - y1)]
    # x1---y1---y2---x2
    elif(x1 < y1) and (x2 > y2):
        return_range += [(x1, y1-1)]
        
        return_range += [(y2 + 1, x2)]
        return_range += [(start_map, start_map + y2 - y1)]
    # y1---x1---x2---y2
    elif (x1 >= y1) and (x2 <= y2):
        return_range += [(start_map + x1 - y1, start_map + x2 - y1)]
    else:
        return_range += [(x1, x2)]
    return return_range
lowest_location = float('inf')



print('Part 1: lowest location is ' + str(part_1_lowest))
print('Part 2: Lowest location is ' + str(lowest_location))
# 100644325 too high
# 37806486 apparently the correct answer
