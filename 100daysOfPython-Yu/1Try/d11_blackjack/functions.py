import random
import global_variables

new_values = []

def player_stake(player_bank,dealer_bank):
    """promt the user to put an amount of money from playerBank into current game
        and reduce the amount of playerBank according to the choosen amount

    Args:
        player_bank (int): current amount of money in players bank
        dealer_bank (int): current amount owned by casino
        
        Return: array with updated values for [player_bank, dealer_bank]
    """
    global new_values
    valid_choice = True
    #current_balance = print(f'Your current balance is {player_bank}' + '$')
             
    while valid_choice:
        amount_choosen = int(input('What is your stake? Print: "1", "5","25", "50", "100", "500", or "999" for ALL IN\n'))
    
        match amount_choosen:
            case 1:
                amount_choosen = 1
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case 5:
                amount_choosen = 5
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case 25:
                amount_choosen = 25
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case 50:
                amount_choosen = 50
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case 100:
                amount_choosen = 100
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case 500:
                amount_choosen = 500
                print(f"You chose to put {amount_choosen}" + "$ into this round")
            case 999:
                amount_choosen = global_variables.player_bank
                print(f"You chose to put {amount_choosen}" + "$ into this round")
                
        if (global_variables.player_bank - amount_choosen) >= 0:
            global_variables.game_stake = amount_choosen
            
            print(f'Your current balance is {global_variables.player_bank - global_variables.game_stake}' + '$')
            valid_choice = False
            break
        elif (global_variables.player_bank - amount_choosen) <= 0:
            print("You're betting too high! Please choose a new bet!")
            valid_choice = True
    new_values = [global_variables.player_bank, global_variables.dealer_bank]
    return new_values


def deal_hand(shuffled_deck, number:int):
    """deals the first hand of the game in order: card to player + card to dealer + card to player + card to dealer || equals to "hit" with number = 1
    @args: shuffled deck: arr
    player_hand: 0,1
    dealer_deck: 1,3
    """
    hand_dealt = shuffled_deck[0:number]
    return hand_dealt
    
def update_deck(shuffled_deck, number : int):
    """Def deletes the cards moved to player or dealer hand from deck

    Args:
        shuffled_deck (arr): full original shuffled deck of 52 cards
        number (int) : number of cards to remove from old arr
    Returns:
        arr: returns arr of new deck minus initially dealt cards 
    """
    updated_shuffled_deck = shuffled_deck[number:]
    return updated_shuffled_deck

def count_points(player_hand, player_points):
    """func counts and updates player_points

    Args:
        player_hand (_type_): player or dealer_hand
        player_points (_type_): current player or dealer_points counter

    Returns:
        int: current visible point counter (in case of dealer_points actual points are updated, but _visible points are returned )
        
        
    Comment: Update func to -> if player_hand == dealer_hand_visible, then all adding operations on dealer_hand & dealer_points + d_h_visible & d_p_visible, but only return visible points back
    
    in blackjack.py -> if case dealer_points 21 or player looses -> show global_variable.dealer_hand & global_variable.dealer_points (full valuesl)
    """
    
    
    if (player_hand == global_variables.dealer_hand):
        global_variables.dealer_points = 0
        global_variables.dealer_points_visible = 0
        
        for cards in global_variables.dealer_hand:
            if cards in ['Jack', 'Queen', 'King']:
                global_variables.dealer_points += 10
            elif cards == 'Ace':
                if ((global_variables.dealer_points + 11) <= 21):
                    global_variables.dealer_points += 11
                else:
                    global_variables.dealer_points += 1
            else:
                global_variables.dealer_points += cards
                
        for cards in global_variables.dealer_hand_visible:
            if cards in ['Jack', 'Queen', 'King']:
                global_variables.dealer_points_visible += 10
            elif cards == 'Ace':
                if ((global_variables.dealer_points_visible + 11) <= 21):
                    global_variables.dealer_points_visible += 11
                else:
                    global_variables.dealer_points_visible += 1
            else:
                global_variables.dealer_points_visible += cards
        return global_variables.dealer_points_visible
    
    else:
        global_variables.player_points = 0
        for cards in global_variables.player_hand: # type: ignore
            if cards in ['Jack', 'Queen', 'King']:
                global_variables.player_points += 10
            elif cards == 'Ace':
                if (global_variables.player_points + 11) <= 21:
                    global_variables.player_points += 11
                else:
                    global_variables.player_points += 1
            else:
                global_variables.player_points += cards
    return global_variables.player_points
   
def remaining_points(player_points):
    
    if(player_points == global_variables.player_points):
        global_variables.player_points_remaining = global_variables.point_limit - global_variables.player_points
    elif(player_points == global_variables.dealer_points):
        global_variables.dealer_points_remaining = global_variables.point_limit - global_variables.dealer_points
    
def hit_or_stand():
    global_variables.player_turn = 1
    global_variables.dealer_turn = 0
    #hit_or_stand_bool:bool
    
    while((global_variables.player_points < global_variables.point_limit) and (
            global_variables.dealer_points < global_variables.point_limit)):
        #if dealer stand and player stand - open all cards and count player with lowest difference to 21
        if((global_variables.player_last_turn == False) and (global_variables.dealer_last_turn == False)):
            remaining_points(global_variables.player_points)
            remaining_points(global_variables.dealer_points)
            if(global_variables.player_points_remaining < global_variables.dealer_points_remaining):
                print('Win!')
                print(f'Dealer\'s cards are {global_variables.dealer_hand} and dealer\'s points are {global_variables.dealer_points}')
                clean_up_values(False)
                
            elif(global_variables.player_points_remaining > global_variables.dealer_points_remaining):
                print('Bust! Dealer wins!')
                print(f'Dealer\'s cards are {global_variables.dealer_hand} and dealer\'s points are {global_variables.dealer_points}')
                clean_up_values(False)
                
            elif(global_variables.player_points_remaining == global_variables.dealer_points_remaining):
                print('Push!')
                print(f'Dealer\'s cards are {global_variables.dealer_hand} and dealer\'s points are {global_variables.dealer_points}')
                clean_up_values(False)
                
        elif((global_variables.player_turn == 1) and (global_variables.dealer_turn == 0)):
            
            hit_or_stand_choice = input('"Hit" or "Stand"?\n')
            # if((hit_or_stand_choice != "Hit") or (hit_or_stand_choice != "hit") or (hit_or_stand_choice != "Stand") or (hit_or_stand_choice != "stand")):
            #     hit_or_stand_bool = False
                
            #     while (hit_or_stand_bool = False):
            #         print('Please provide a valid input: "Hit"/"hit" or "Stand"/"stand" ')
            #         hit_or_stand_choice = input('"Hit" or "Stand"?\n')
            #         if(hit_or_stand_choice == "Hit" or hit_or_stand_choice == "hit" or hit_or_stand_choice == "Stand" or hit_or_stand_choice == "stand" ):
            #             break
            #         else:
            #             continue
            
            if hit_or_stand_choice == 'Hit' or hit_or_stand_choice == 'hit' :
                global_variables.player_last_turn = True
                global_variables.player_hand += deal_hand(global_variables.shuffled_deck, 1)
                global_variables.shuffled_deck = update_deck(global_variables.shuffled_deck, 1)
                count_points(global_variables.player_hand, global_variables.player_points)
                global_variables.player_turn = 0
                global_variables.dealer_turn = 1
                print(f'You drew {global_variables.player_hand[-1]}.Your hand contains {global_variables.player_hand} and you have {global_variables.player_points} points')
                
            elif hit_or_stand_choice == 'Stand' or hit_or_stand_choice == 'stand':
                global_variables.player_last_turn = False
                global_variables.player_turn = 0
                global_variables.dealer_turn = 1
              
        elif((global_variables.player_turn == 0) and (global_variables.dealer_turn == 1)):
            if(global_variables.dealer_points < 17):
                global_variables.dealer_last_turn = True
                print('Dealers card value is under 17. Dealer "hits"')
                global_variables.dealer_hand += deal_hand(global_variables.shuffled_deck, 1)
                global_variables.shuffled_deck = update_deck(global_variables.shuffled_deck, 1)
                global_variables.dealer_hand_visible = global_variables.dealer_hand[1:]
                count_points(global_variables.dealer_hand, global_variables.dealer_points)
                print(f'Dealers open cards are [{global_variables.dealer_hand_visible}] and he has {global_variables.dealer_points_visible} points')
        
                global_variables.player_turn = 1
                global_variables.dealer_turn = 0
                
                if(global_variables.dealer_points >= global_variables.point_limit):
                    break
                
            else:
                print('Dealers card value over under 17. Dealer "stands"')
                global_variables.dealer_last_turn = False
                global_variables.player_turn = 1
                global_variables.dealer_turn = 0
                
        #break
def cash_out(is_player_win:bool):
    if is_player_win:
        global_variables.player_bank += global_variables.game_stake
        global_variables.dealer_bank -= global_variables.game_stake
    else:
        global_variables.player_bank -= global_variables.game_stake
        global_variables.dealer_bank += global_variables.game_stake

def clean_up_values(is_clean_values:bool):
    """func resets player and dealer points for further game loops

    Args:
        is_clean_values (bool): True: set, False: player looses
    """
    
    if is_clean_values == True:
        global_variables.player_bank = 1000
        global_variables.dealer_bank = 10000
        
        global_variables.game_stake = 0
        global_variables.originalDeck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'Jack', 'Jack', 'Jack', 'Jack', 'Queen', 'Queen', 'Queen', 'Queen', 'King', 'King', 'King', 'King', 'Ace', 'Ace', 'Ace', 'Ace', ]
        # deck of cards -> shuffle
        global_variables.shuffled_deck = random.sample(global_variables.originalDeck, len(
            global_variables.originalDeck))

        global_variables.player_hand = []
        global_variables.dealer_hand = []
        global_variables.dealer_hand_visible = []

        global_variables.player_points = 0
        global_variables.dealer_points = 0
        global_variables.dealer_points_visible = 0

        global_variables.player_turn = 0
        global_variables.dealer_turn = 0

        global_variables.player_last_turn = True #True = hit False = stand
        global_variables.dealer_last_turn = True #True = hit False = stand

        global_variables.player_points_remaining = 21
        global_variables.dealer_points_remaining = 21
    else:
        #global_variables.player_bank += global_variables.game_stake
        #global_variables.dealer_bank -= global_variables.game_stake
        
        global_variables.game_stake = 0
        global_variables.originalDeck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 'Jack', 'Jack', 'Jack', 'Jack', 'Queen', 'Queen', 'Queen', 'Queen', 'King', 'King', 'King', 'King', 'Ace', 'Ace', 'Ace', 'Ace', ]
        # deck of cards -> shuffle
        global_variables.shuffled_deck = random.sample(global_variables.originalDeck, len(
            global_variables.originalDeck))

        global_variables.player_hand = []
        global_variables.dealer_hand = []
        global_variables.dealer_hand_visible = []

        global_variables.player_points = 0
        global_variables.dealer_points = 0
        global_variables.dealer_points_visible = 0

        global_variables.player_turn = 0
        global_variables.dealer_turn = 0

        global_variables.player_last_turn = True #True = hit False = stand
        global_variables.dealer_last_turn = True #True = hit False = stand

        global_variables.player_points_remaining = 21
        global_variables.dealer_points_remaining = 21