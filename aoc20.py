import math
raw_input = []
f = open('aoc20.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
BUTTON = 1
BROADCASTER = 2
FLIP = 3
CONJ = 4

modules = {}
modules['button'] = {'state': 0, 'inputs':{'_':0}, 'outputs': {'broadcaster':0}, 'out_seq': ['broadcaster'], 'type': BUTTON}
modules['broadcaster'] = {'inputs': {'button':0}}
for line in raw_input:
    in_module, out_modules = line.split(' -> ')
    if in_module[0] == '%':
        module_type = FLIP
        in_module = in_module[1:]
    elif in_module[0] == '&':
        module_type = CONJ
        in_module = in_module[1:]
    else:
        module_type = BROADCASTER
    if in_module not in modules:
        modules[in_module] = {}
    outputs = out_modules.split(', ')
    modules[in_module]['state'] = 0
    modules[in_module]['type'] = module_type
    modules[in_module]['outputs'] = {}
    modules[in_module]['out_seq'] = outputs
    for out_module in outputs:
        modules[in_module]['outputs'][out_module] = 0
        if out_module not in modules:
            modules[out_module] = {}
            modules[out_module]['inputs'] = {}
        if 'inputs' not in modules[out_module]:
            modules[out_module]['inputs'] = {}
        modules[out_module]['inputs'][in_module] = 0

low_pulses = 0
high_pulses = 0
# instruction format:
# (sender, destination, pulse)
instruction_queue = [('button','broadcaster', 0)]
for button_press in range(1000):      # Will need to loop to 1000
    # print('*** button press ' + str(button_press + 1))
    instruction_queue = [('_', 'button', 0)]
    while instruction_queue:
        source, dest, pulse_val = instruction_queue.pop(0)

        module = modules[dest]
        module['inputs'][source] = pulse_val
        # Determine the output pulse
        if 'type' not in module:
            # some sort of output.  Cotinue.
            continue
        module_type = module['type']
        if module_type == BUTTON:
            out_pulse = 0
        elif module_type == BROADCASTER:
            out_pulse = 0
        elif module_type == FLIP:
            if pulse_val == 1:
                # ignore incoming high pulses
                continue
            else:
                module['state'] = int(not(module['state']))
            if module['state'] == 0:
                out_pulse = 0
            else:
                out_pulse = 1
        else:   # Conjunction
            num_of_inputs = len(module['inputs'])
            num_high = sum(module['inputs'].values())
            if num_high == num_of_inputs:
                out_pulse = 0
            else:
                out_pulse = 1
        
        # Now start to process and send commands for each output
        for out_module in module['out_seq']:
            if out_pulse == 0:
                low_pulses += 1
            else:
                high_pulses += 1
            module['out_module'] = out_pulse
            next_instr = (dest, out_module, out_pulse)
            # print(next_instr)
            instruction_queue += [(dest, out_module, out_pulse)]
print('Part 1: ' + str(low_pulses * high_pulses))

modules = {}
modules['button'] = {'state': 0, 'inputs':{'_':0}, 'outputs': {'broadcaster':0}, 'out_seq': ['broadcaster'], 'type': BUTTON}
modules['broadcaster'] = {'inputs': {'button':0}}
for line in raw_input:
    in_module, out_modules = line.split(' -> ')
    if in_module[0] == '%':
        module_type = FLIP
        in_module = in_module[1:]
    elif in_module[0] == '&':
        module_type = CONJ
        in_module = in_module[1:]
    else:
        module_type = BROADCASTER
    if in_module not in modules:
        modules[in_module] = {}
    outputs = out_modules.split(', ')
    modules[in_module]['state'] = 0
    modules[in_module]['type'] = module_type
    modules[in_module]['outputs'] = {}
    modules[in_module]['out_seq'] = outputs
    for out_module in outputs:
        modules[in_module]['outputs'][out_module] = 0
        if out_module not in modules:
            modules[out_module] = {}
            modules[out_module]['inputs'] = {}
        if 'inputs' not in modules[out_module]:
            modules[out_module]['inputs'] = {}
        modules[out_module]['inputs'][in_module] = 0

# Had to stop and look at the graph of the wiring.
# Need to watch rd, bt, fv, pr.  They feed into vd which is a conj and will only send low if all those are high
instruction_queue = [('button','broadcaster', 0)]
all_found = False
button_press= 0
rd = (0, False)
bt = (0, False)
fv = (0, False)
pr = (0, False)

while True:   
    if (rd[0] > 0) and (bt[0] > 0) and (fv[0] > 0) and (pr[0] > 0):
        break
    button_press += 1
    # print('*** button press ' + str(button_press))
    instruction_queue = [('_', 'button', 0)]
    while instruction_queue:
        source, dest, pulse_val = instruction_queue.pop(0)

        module = modules[dest]
        module['inputs'][source] = pulse_val
        # Determine the output pulse
        if 'type' not in module:
            # some sort of output.  Cotinue.
            continue
        module_type = module['type']
        if module_type == BUTTON:
            out_pulse = 0
        elif module_type == BROADCASTER:
            out_pulse = 0
        elif module_type == FLIP:
            if pulse_val == 1:
                # ignore incoming high pulses
                continue
            else:
                module['state'] = int(not(module['state']))
            if module['state'] == 0:
                out_pulse = 0
            else:
                out_pulse = 1
        else:   # Conjunction
            num_of_inputs = len(module['inputs'])
            num_high = sum(module['inputs'].values())
            if num_high == num_of_inputs:
                out_pulse = 0
            else:
                out_pulse = 1
        
        # Now start to process and send commands for each output
        # Need to watch rd, bt, fv, pr.  They feed into vd which is a conj and will only send low if all those are high
        if dest == 'rd' and out_pulse == 1 and rd[1] == False:
            rd = (button_press, True)
        if dest == 'bt' and out_pulse == 1 and bt[1] == False:
            bt = (button_press, True)
        if dest == 'fv' and out_pulse == 1 and fv[1] == False:
            fv = (button_press, True)
        if dest == 'pr' and out_pulse == 1 and pr[1] == False:
            pr = (button_press, True)
        for out_module in module['out_seq']:
            if out_pulse == 0:
                low_pulses += 1
            else:
                high_pulses += 1
            
            module['out_module'] = out_pulse
            next_instr = (dest, out_module, out_pulse)
            # print(next_instr)
            instruction_queue += [(dest, out_module, out_pulse)]
min_presses = math.lcm(rd[0], bt[0], fv[0], pr[0])
print('Part 2: ' + str(min_presses))