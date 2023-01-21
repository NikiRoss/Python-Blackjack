from dealer import Dealer

player_live = True
dealer_live = True
dealer = Dealer()

player_hand = []
dealer_hand = []


for _ in range(2):
    dealer.deal_card(player_hand)
    dealer.deal_card(dealer_hand)
    
play_again = 'y'
while play_again == 'y':
    
    while player_live or dealer_live:
        
        print(f"Dealer has {dealer_hand} for a total of {dealer.calculate_score(dealer_hand)}")
        print(f"You have {player_hand} for a total of {dealer.calculate_score(player_hand)}")
        stay_or_hit = input("1: Stay\n2: Hit\n")
        
        if stay_or_hit == '1':
            player_live = False  
        else:
            dealer.deal_card(player_hand)
            
        if dealer.calculate_score(dealer_hand) >= 16:
            dealer_live = False
        else:
            dealer.deal_card(dealer_hand)
        
        if dealer.check_winner(player_hand, dealer_hand):
            break
    play_again = input("Would you like to play again? (y/n)\n")
    

