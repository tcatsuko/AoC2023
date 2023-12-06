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

lowest_location = float('inf')

# Build up the structure for part 2
game_ranges = []
# seed-to-soil
rule_range = []
current_rule = []
for seed in seed_soil:
    
    this_range = seed_soil[seed]['range']
    seed_range = [seed, seed + this_range - 1]
    soil_start = seed_soil[seed]['soil']
    current_rule += [(seed_range, soil_start)]
rule_range += [current_rule]
current_rule = []
for soil in soil_fert:
    this_range = soil_fert[soil]['range']
    soil_range = [soil, soil + this_range - 1]
    fert_start = soil_fert[soil]['fert']
    current_rule += [(soil_range, fert_start)]
rule_range += [current_rule]
current_rule = []
for fert in fert_water:
    this_range = fert_water[fert]['range']
    fert_range = [fert, fert + this_range - 1]
    water_start = fert_water[fert]['water']
    current_rule += [(fert_range, water_start)]
rule_range += [current_rule]
current_rule = []
for water in water_light:
    this_range = water_light[water]['range']
    water_range = [water, water + this_range - 1]
    light_start = water_light[water]['light']
    current_rule += [(water_range, light_start)]
rule_range += [current_rule]
current_rule = []
for light in light_temp:
    this_range = light_temp[light]['range']
    light_range = [light, light + this_range - 1]
    temp_start = light_temp[light]['temp']
    current_rule += [(light_range, temp_start)]
rule_range += [current_rule]
current_rule = []
for temp in temp_humid:
    this_range = temp_humid[temp]['range']
    temp_range = [temp, temp + this_range - 1]
    humid_start = temp_humid[temp]['humid']
    current_rule += [(temp_range, humid_start)]
rule_range += [current_rule]
current_rule = []
for humid in humid_location:
    this_range = humid_location[humid]['range']
    humid_range = [humid, humid + this_range - 1]
    location_start = humid_location[humid]['location']
    current_rule += [(humid_range, location_start)]
rule_range += [current_rule]

new_seed_ranges = seed_ranges[0]

def split_ranges(source_range, rule_range, translate_start):
    # will always return the source range by default, assumes no overlap
    translated = False
    x1 = source_range[0]
    x2 = source_range[1]
    y1 = rule_range[0]
    y2 = rule_range[1]
    # Check if source range is completely within compared range
    # y1~x1---x2~y2
    before_range = []
    overlapped_range = source_range
    after_range = []
    if (x1 >= y1) and (x2 <= y2):
        overlapped_range = [translate_start + x1 - y1, translate_start + x2 - y1]
        translated = True
    # check if rule range is completely within source range
    # x1~y1---y2~x2
    elif (y1 >= x1) and (y2 <= x2):
        if x1 != y1:
            before_range = [x1, y1 - 1]
        overlapped_range = [translate_start, translate_start + y2 - y1]
        translated = True
        if x2 != y2:
            after_range = [y2 + 1, x2]
    # check if rule range overlaps on left side
    # y1---x1----y2---x2
    elif (y1 <= x1) and (x2 >= y2) and (y2 >= x1):
        
        overlapped_range = [translate_start + (x1-y1), translate_start + y2 - x1]
        translated = True
        if x2 != y2:
            after_range = [y2 + 1, x2]
    # check if rule range overlaps on right side
    # x1---y1---x2---y2
    elif (x1 <= y1) and (x2 < y2) and (x2 >= y1):
        if x1 != y1:
            before_range = [x1, y1 - 1]
        overlapped_range = [translate_start, translate_start + x2 - y1]
        translated = True
        
    return (before_range, overlapped_range, after_range, translated)


def translate_points(in_range, next_ranges):
    global lowest_location
    if len(next_ranges) == 7:
        print('Processing seed-to-soil')
    elif len(next_ranges) == 6:
        print('Processing soil-to-fertilizer')
    elif len(next_ranges) == 5:
        print('Processing fertilizer-to-water')
    elif len(next_ranges) == 4:
        print('Processing water-to-light')
    elif len(next_ranges) == 3:
        print('Processing light-to-temp')
    elif len(next_ranges) == 2:
        print('Processing temp-to-humidity')
    elif len(next_ranges) == 1:
        print('Processing humidity-to-location')
    else:
        print('Determining if lowest location')
    if next_ranges == []:
        if in_range[0] < lowest_location:
            lowest_location = in_range[0]
            print("found lowest location: " + str(lowest_location))
        return
    current_rule = next_ranges[0]
    if len(next_ranges) > 1:
        next_rule = next_ranges[1:]
    else:
        next_rule = []
    ranges_to_check = [in_range]
    success_translated_ranges = []
    for rule in current_rule:
        for range_to_check in ranges_to_check:
            new_ranges_to_check = []
            translated_ranges = split_ranges(range_to_check, rule[0], rule[1])
            if translated_ranges[3] == True:
                success_translated_ranges += [translated_ranges[1]]
                if translated_ranges[0] != []:
                    new_ranges_to_check += [translated_ranges[0]]
                if translated_ranges[2] != []:
                    new_ranges_to_check += [translated_ranges[2]]
            else:
                new_ranges_to_check += [range_to_check]
        ranges_to_check = new_ranges_to_check[:]
    for range_to_check in ranges_to_check:
        success_translated_ranges += [range_to_check]
    for next_range in success_translated_ranges:
        translate_points(next_range, next_rule)  
           


for seed_range in seed_ranges:
   translate_points(seed_range, rule_range)
# translate_points(seed_ranges[1], rule_range)
print()




print('Part 1: lowest location is ' + str(part_1_lowest))
print('Part 2: Lowest location is ' + str(lowest_location))
# 100644325 too high
# 37806486 apparently the correct answer
