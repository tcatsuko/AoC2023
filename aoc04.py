raw_input = []
f = open('aoc04.txt','rt')
for line in f:
    raw_input += [line[:-1]]
f.close()
card_scores = []
total_cards = []
card_dict = {}
for card in raw_input:
    card_number = int(card.split(':')[0][5:])
    if card_number not in card_dict:
        card_dict[card_number] = 1
    else:
        card_dict[card_number] += 1
    numbers = card.split(': ')[1]
    print('processing card: ' + str(card_number))
    winning_numbers = numbers.split(' | ')[0].split(' ')
    card_numbers = numbers.split(' | ')[1].split(' ')
    

    matches = 0
    for number in card_numbers:
        if number == '':
            continue
        if number in winning_numbers:
            matches += 1
    if matches > 0:
        if (card_number, 2**(matches - 1)) not in card_scores:
            card_scores += [(card_number,2**(matches - 1))]
        for x in range(matches):
            next_copy = card_number + 1 + x
            if next_copy not in card_dict:
                card_dict[next_copy] = (1 * card_dict[card_number])
            else:
                card_dict[next_copy] += (1 * card_dict[card_number])
    else:
        if (card_number, 0) not in card_scores:
            card_scores += [(card_number, 0)]
        

total_score = 0
for score in card_scores:
    total_score += score[1]
print('Part 1: total score is ' + str(total_score))
total_cards = 0
for card in card_dict:
    total_cards += card_dict[card]
print('Part 2: total cards is ' + str(total_cards))
