import operator
import copy

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
    '<' : operator.lt,
    '>' : operator.gt,
    '=' : operator.eq,
    '<=': operator.eq or operator.lt,
    '>=': operator.eq or operator.gt,
    '!=': not operator.eq
}


raw_input = []
f = open('aoc19.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
rules = {}
end_rule_index = 0
for idx, rule in enumerate(raw_input):
    if rule == '':
        end_rule_index = idx + 1
        break
    workflow, conditions = rule.split('{')
    conditions = conditions[:-1]
    conditions = conditions.split(',')
    rules[workflow] = conditions
# Get ratings
ratings = []
for line in raw_input[end_rule_index:]:
    current_rating = {}
    split_ratings = line[1:-1].split(',')
    for rating in split_ratings:
        attribute, value = rating.split('=')
        current_rating[attribute] = int(value)
    ratings += [current_rating]
accepted = []
rejected = []
for rating in ratings:
    workflow = 'in'
    while not ((workflow == 'A') or (workflow == 'R')):
        current_workflow = rules[workflow]
        for rule in current_workflow:
            if ('<' in rule) or ('>' in rule):
                attribute = rule[0]
                op = rule[1]
                value = int(rule[2:].split(':')[0])
                if ops[op](rating[attribute], value) == True:
                    workflow = rule.split(':')[1]
                    break
            else:
                workflow = rule
    if workflow == 'A':
        accepted += [rating]
    else:
        rejected += [rating]
total_sum = 0
for rating in accepted:
    for number in rating.values():
        total_sum += number
print('Part 1: total sum is ' + str(total_sum))
parameters = {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}
def traverse_rules(rules, start_rule, parameters):
    possibilities = 0
    
    if start_rule == 'R':
        return 0
    elif start_rule == 'A':
        # calculate ranges
        x = parameters['x']
        m = parameters['m']
        a = parameters['a']
        s = parameters['s']
        return (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1]-a[0] + 1) * (s[1]-s[0]+1)
    conditions = rules[start_rule]
    for condition in conditions:
        if '>' in condition:
            parameter = condition.split('>')[0]
            threshold = int(condition.split('>')[1].split(':')[0])
            next_rule = condition.split('>')[1].split(':')[1]
            if threshold > parameters[parameter][0]:
                new_parameters = copy.deepcopy(parameters)
                new_parameters[parameter] = (threshold + 1, parameters[parameter][1])
                possibilities += traverse_rules(rules, next_rule, new_parameters)
            # else:
                parameters[parameter] = (parameters[parameter][0], threshold)
            
        elif '<' in condition:
            parameter = condition.split('<')[0]
            threshold = int(condition.split('<')[1].split(':')[0])
            next_rule = condition.split('<')[1].split(':')[1]
            if threshold < parameters[parameter][1]:
                new_parameters = copy.deepcopy(parameters)
                new_parameters[parameter] = (parameters[parameter][0], threshold - 1)
                possibilities += traverse_rules(rules, next_rule, new_parameters)
            # else:
                parameters[parameter] = (threshold, parameters[parameter][1])
        else:
            possibilities += traverse_rules(rules, condition, parameters)
    return possibilities
total_possible = traverse_rules(rules, 'in', parameters)
print('Part 2: total possibilities are ' + str(total_possible))
