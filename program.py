import random

class Pig: 
    """
    
        Attributes:
        
        Side Effects: 
        
    """

    def __init__(self, player): 
        self.player = player
        self.hand = []

        self.deck = [(suit, rank) 
        for suit in ('Spades', 'Hearts', 'Clubs', 'Diamonds')
        for rank in range(1,14)]

        self.bot = []

    def dealer(self):
        random.shuffle(self.deck)
        self.hand =[self.deck.pop() for cards in range(4)]
        self.bot = [self.deck.pop() for cards in range(4)]
        return self.hand, self.bot

    def pass_hands(self): 
        b_suits = {suits for suits, rank in self.bot} 
        
        while len(b_suits) != 4: 
            player_pass = self.hand.pop(0)
            bot_pass = self.bot.pop(0)
            self.hand.append(bot_pass)
            self.bot.append(player_pass)
            print(f'Player Hand: {self.hand}\nBot Hand: {self.bot} \n')
            input("Press any key to continue:")
        
        print('*touches nose*')
        
        


               
b1 = Pig('john')
b1.dealer()
print(b1.pass_hands())