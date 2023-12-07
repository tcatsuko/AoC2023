from operator import itemgetter
raw_input = []
all_hands = []
bets = {}

f = open('aoc07.txt','rt')

for line in f:
    card, bet = line[:-1].split(' ')
    bet = int(bet)
    current_hand = {}
    current_hand['cards'] = card
    current_hand['bet'] = bet
    bets[card] = bet
    all_hands += [current_hand]
    raw_input += [line[:-1]]
f.close()

def get_type(hand,part):
    card_count = {}
    for card in hand:
        if card not in card_count:
            card_count[card] = 1
        else:
            card_count[card] += 1
    hand_type = 7 # default to high card
    joker_count = hand.count('J')
    cards_seen = []
    for card in card_count:
        cards_seen += [card_count[card]]

    # 1 = 5 of a kind - OK
    # 2 = 4 of a kind - OK
    # 3 = full house - OK
    # 4 = 3 of a kind - OK
    # 5 = two pair - OK
    # 6 = one pair 
    # 7 = high card
    cards_seen.sort()
    cards_seen.reverse()
    # Now start to parse out what it is
    #5 of a kind:
    if len(cards_seen) == 1:
        hand_type = 1

    # 4 of a kind or full house
    elif len(cards_seen) == 2:
        if cards_seen[0] == 4:
            hand_type = 2 # 4 of a kind
            if part == 2:
                if (joker_count == 1) or (joker_count == 4):
                    hand_type = 1 # Upgraded to 5 of a kind
        else:
            hand_type = 3 # full house
            if part == 2:
                if joker_count > 0:
                    hand_type = 1 # At least one of the groups is joker, so now 5 of a kind
    elif len(cards_seen) == 3:
        
        if cards_seen[0] == 2 and cards_seen[1] == 2:
            # two pair
            hand_type = 5 # two pair
            if part == 2:
                if joker_count == 2: # AAJJB
                    # now four of a kind
                    hand_type = 2
                elif joker_count == 1: # AABBJ
                    # now a full house
                    hand_type = 3
        else:
            # 3 of a kind
            hand_type = 4
            if part == 2:
                if (joker_count == 3) or (joker_count == 1): # AAAJB or JJJAB
                    # Now 4 of a kind
                    hand_type = 2
    elif len(cards_seen) == 4: # AABCD
        hand_type = 6
        if part == 2:
            if (joker_count == 2) or (joker_count == 1): #JJABC or AABCJ
                # now 3 of a kind
                hand_type = 4
            
    else:
        if part == 2:
            if joker_count == 1:
                hand_type = 6 # one pair

    
    return hand_type
scores_1 = []
scores_2 = []
scores_3 = []
scores_4 = []
scores_5 = []
scores_6 = []
scores_7 = []
hand_scores = [scores_1, scores_2, scores_3, scores_4, scores_5, scores_6, scores_7]
def sort_hands(hands, part):
    exploded_cards = []
    if hands == []:
        return []
    for hand in hands:
        hand = hand.replace('A','P')
        hand = hand.replace('K','O')
        hand = hand.replace('Q','N')
        if part == 1:
            hand = hand.replace('J','M')
        else:
            hand = hand.replace('J','1')
        hand = hand.replace('T','L')
        exploded_cards += [[*hand]]
    sorted_exploded_cards = sorted(exploded_cards, key = itemgetter(0,1,2,3,4))
    sorted_exploded_cards.reverse()
    new_hands = []
    for hand in sorted_exploded_cards:
        new_hands += [''.join(hand)]
    for idx, hand in enumerate(new_hands):
        hand = hand.replace('P','A')
        hand = hand.replace('O','K')
        hand = hand.replace('N','Q')
        hand = hand.replace('M','J')
        hand = hand.replace('L','T')
        hand = hand.replace('1','J')
        new_hands[idx] = hand
    hands = new_hands[:]
    return hands
for hand in all_hands:
    type = get_type(hand['cards'],1)
    hand_scores[type - 1] += [hand['cards']]
number_of_hands = len(raw_input)
for idx, score_group in enumerate(hand_scores):
    score_group = sort_hands(score_group, 1)
    hand_scores[idx] = score_group
# Get final ranking
hand_scores.reverse()
hands_ranked = []
for rank in hand_scores:
    if rank == []:
        continue
    rank.reverse()
    for hand in rank:
        hands_ranked += [hand]
# We have our rankings, now time to get a total winnings
total_winnings = 0
for idx, hand in enumerate(hands_ranked):
    final_rank = idx + 1
    bet = bets[hand]
    total_winnings += (bet * final_rank)
print('Part 1: total winnings is ' + str(total_winnings))
scores_1 = []
scores_2 = []
scores_3 = []
scores_4 = []
scores_5 = []
scores_6 = []
scores_7 = []
hand_scores = [scores_1, scores_2, scores_3, scores_4, scores_5, scores_6, scores_7]
for hand in all_hands:
    type = get_type(hand['cards'],2)
    hand_scores[type - 1] += [hand['cards']]
for idx, score_group in enumerate(hand_scores):
    score_group = sort_hands(score_group, 2)
    hand_scores[idx] = score_group
# Get final ranking
hand_scores.reverse()
hands_ranked = []
for rank in hand_scores:
    if rank == []:
        continue
    rank.reverse()
    for hand in rank:
        hands_ranked += [hand]
# We have our rankings, now time to get a total winnings
total_winnings = 0
for idx, hand in enumerate(hands_ranked):
    final_rank = idx + 1
    bet = bets[hand]
    total_winnings += (bet * final_rank)
print('Part 2: total winnings is ' + str(total_winnings))
