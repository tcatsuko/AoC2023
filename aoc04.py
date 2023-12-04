raw_input = []
f = open('test_aoc04.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
card_scores = []
total_cards = []

for card in raw_input:
    card_number = int(card.split(':')[0][5:])
    numbers = card.split(': ')[1]
    total_cards += [card_number]
    winning_numbers = numbers.split(' | ')[0].split(' ')
    card_numbers = numbers.split(' | ')[1].split(' ')
    matches = 0
    for number in card_numbers:
        if number == '':
            continue
        if number in winning_numbers:
            matches += 1
    if matches > 0:
        card_scores += [2**(matches - 1)]
        for x in range(matches):
            total_cards += [x + card_number]
    else:
        card_scores += [0]
print('Part 1: total score is ' + str(sum(card_scores)))
print('Part 2: total cards is ' + str(len(total_cards)))
