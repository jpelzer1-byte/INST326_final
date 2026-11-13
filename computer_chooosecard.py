
def computer_chooosecard(hand):
    """Choose which card the computer should pass."""

    if len(hand) != 4:
        raise ValueError("The hand must have 4 cards.")

    counts = {}

    for card in hand:
        rank = card["rank"]

        if rank in counts:
            counts[rank] += 1
        else:
            counts[rank] = 1

    best_rank = None
    most_cards = 0

    for rank in counts:
        if counts[rank] > most_cards:
            most_cards = counts[rank]
            best_rank = rank

    if most_cards == 4:
        return None

    for i in range(len(hand)):
        if hand[i]["rank"] != best_rank:
            return i


if __name__ == "__main__":
    hand = [
        {"rank": "7", "suit": "Hearts"},
        {"rank": "7", "suit": "Spades"},
        {"rank": "K", "suit": "Clubs"},
        {"rank": "Q", "suit": "Diamonds"}
    ]

    print(computer_chooosecard(hand))

