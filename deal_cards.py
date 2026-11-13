import random

def deal_cards(deck, num_of_players):
    random.shuffle(deck)
    
    cards_needed = num_of_players * 4
    if len(deck)< cards_needed:
        raise ValueError("Not enough cards in the deck")
    
    hands = [] # starts each player with an empty hand
    for i in range(num_of_players):
        hands.append([])
        
    for round in range(4):
        for player in range(num_of_players):
            card = deck.pop(0)
            hands[player].append(card)
            
    return hands