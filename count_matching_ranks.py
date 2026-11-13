def count_matching_ranks(hand, target_rank):
    """Analyzes a player's hand to count how many cards match a specific target rank, 
    helping figure out how close the player is to getting a complete 'book'

    Args: 
        hand (list of dict): A list of four card dictionaries, where each dictionary 
            contains 'rank' (str) and 'suit' (str) keys.
        target_rank (str): The specific card rank being searched for (e.g., 'Queen').

    Returns:
        int: The total count of cards in the hand that match the target rank.
    """
    matching_count = 0
    
    for card in hand:
        if card["rank"] == target_rank:
            matching_count += 1
            
    return matching_count

if __name__ == "__main__":
    test_hand = [
        {"rank": "Jack", "suit": "Hearts"},
        {"rank": "Jack", "suit": "Spades"},
        {"rank": "Queen", "suit": "Clubs"},
        {"rank": "King", "suit": "Diamonds"}
    ]
    
    result = count_matching_ranks(test_hand, "Jack")
    print(f"Testing count_matching_ranks for 'Jack': Expected 2, Got {result}")