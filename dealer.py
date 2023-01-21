import random

class Dealer:
    def __init__(self):
        self.deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A'] * 4
    
    def deal_card(self, turn):
        card = random.choice(self.deck)
        turn.append(card)
        self.deck.remove(card)
    
    def calculate_score(self, turn):
        total = 0
        face = ['J', 'Q', 'K']
        for card in turn:
            if card in range(1, 11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total
    
    def check_winner(self, player_hand, dealer_hand):
        if self.calculate_score(player_hand) > 21:
            print(f"You are bust with a total of {self.calculate_score(player_hand),} dealer wins")
            return True
        elif self.calculate_score(dealer_hand) > 21:
            print(f"You win! Dealer bust with a total of {self.calculate_score(dealer_hand)}")
            return True
        elif self.calculate_score(player_hand) == 21:
            print(f"\nYou win!!! You have {player_hand} for a total of 21 and the dealer has {dealer_hand} with a total of {self.calculate_score(dealer_hand)}")
            return True
        elif self.calculate_score(dealer_hand) == 21:
            print(f"\ndealer has {dealer_hand} with a total of {self.calculate_score(dealer_hand)}. Dealer wins")
            return True
        elif self.calculate_score(player_hand) and self.calculate_score(dealer_hand) == 21:
            print(f"Game is a draw, dealer and player both have 21")
            return True
        else:
            return False
    
    
        