def round_loser(player_hand, other_hands):
    """Takes the length of given set and compares in order to end 
    passing loop.
    
		Args: 
        player_hand (list of tuples): list of the “rank” and “suit” values a player has.
        other_hands (list of tuples): list of tuples containing "rank" and "suit". 

        Returns: 
	        Boolean: allows player to place finger or displays bot placing finger. 

        Raises: 
           ValueError: Raised if player hand or bot hand is empty.
    """


    if 0 < len(player_hand) < 4 or 0 < len(other_hands) < 4:
        raise ValueError('Either player or bot does not have enough cards.')

    p_suits = {suits for suits, rank in player_hand}
    o_suits = {suits for suits, rank in other_hands}

    while 1 < len(o_suits) <= 4 or 1 < len(p_suits) <= 4:
        print(f'Player hand: {player_hand}\nBot hand: {other_hands} \n')

        if len(p_suits) == 1:
            print(f'Player hand:{input('press any key to place finger: ')}')
            break 
        elif len(o_suits) == 1: 
            print(f'Player hand: {player_hand}\nBot hand: *touches nose*')
            break
        else:
            p_suits, o_suits
            input("Press any key to continue: ")

if __name__ == "__main__": 
	player = [('Clubs', 4), ('Clubs', 3), ('Clubs', 9), ('Clubs', 4)]
	bot = [('Diamonds', 4), ('Hearts', 3), ('Diamonds', 9), ('Diamonds', 4)]
	print(f'loser function test: {round_loser(player, bot)}') 



            
