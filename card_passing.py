def pass_cards(selected_cards, player_hands):

    if len(selected_cards) != len(player_hands):
        raise ValueError("Not everyone selected a card.")

    for hand in player_hands:
        if len(hand) != 4:
            raise ValueError("Each player needs 4 cards.")

    for card_number in selected_cards:
        if card_number < 0 or card_number > 3:
            raise ValueError("Invalid card number.")

    cards_to_pass = []

    for player in range(len(player_hands)):
        card = player_hands[player].pop(selected_cards[player])
        cards_to_pass.append(card)

    for player in range(len(player_hands)):
        if player == 0:
            player_hands[-1].append(cards_to_pass[player])
        else:
            player_hands[player - 1].append(cards_to_pass[player])

    return player_hands
