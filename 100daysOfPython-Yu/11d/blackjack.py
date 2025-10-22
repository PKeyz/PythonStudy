import ascii
import random
ascii.print_ascii_art()


# In Blackjack, everyone plays against the dealer.
# Players receive all cards face up, and the dealer’s first card is face up and the second is face down.
# The object of the game is to get closer to 21 than the dealer without going over 21.

# If a hand goes over 21, it is called a “bust” or “break,” and the wager is lost.

# In 21, Jacks, Queens, Kings, and 10s count as 10.
# An Ace may be played as a one or an 11.
# All other cards are played at face value.
#
# When you receive your first two cards, you may either “stand” or “hit.”
# When you “stand,” it means you feel you are close enough to 21 and no longer wish any additional cards, indicated by waving off with your hand.
# If you wish to receive another card or “hit,” tap or scratch the table behind your wager with your finger.
# In either situation, you will never touch the cards; everything is communicated using hand signals.
# You may draw as many cards as you want until you are close to 21 or until you “bust.”
#
# If you are closer to 21 than the dealer, you win and are paid an amount equal to your original wager.
# If your hand is less than the dealer’s, you lose.
# If the dealer’s hand “busts” or “breaks,” you win as well.
# Ties are a standoff or “push,” and your bet remains on the table.
#
# If your initial two cards total 21, any Ace with a 10, Jack, Queen, or King, you have a Blackjack.
# Blackjack is paid either 6 to 5 (player wager*1.2) or 3 to 2 (wager*1.5), depending on the type of Blackjack you are playing.
#
# In 21, the player has many options to choose from:

def decide_game_mode() -> int:
    """Player can decide to play 5:6 (wager * 1.2), or 3 to 2 (wager * 1.5)"""
    game_mode = input("Decide on a game mode: We can play 2:3: Type '23', or 5:6: Type '56'. \n")
    if game_mode == '56':
        multiplier = 1.2
    elif game_mode == '23':
        multiplier = 1.5
    return multiplier

def gather_players():
    more_players = True
    MAX_WAGER = 1000
    #init dealer
    player_name = "Dealer"
    player_wager = random.randint(100,MAX_WAGER)
    player_hand['name'].append(player_name)
    player_hand['wager'].append(player_wager)
    while more_players:
        #player_hand
        player_name = input("What is your name? \n")
        player_wager = int(input(f"What is your bet up to {MAX_WAGER}$ ? \n"))
        player_hand['name'].append(player_name)
        player_hand['wager'].append(player_wager)
        ask_for_more_players = input("are any other players at the table? Type 'Y' or ANY KEY \n").lower()
        if ask_for_more_players == 'y':
            more_players = True
        else:
            more_players = False

def get_player_info(index):
    """Helper Function to acquire player info by index later in the game"""
    return {
        'name': player_hand['name'][index],
        'wager':player_hand['wager'][index],
        'cards':player_hand['cards'][index],
        'sum_value':player_hand['sum_value'][index]
    }

def draw_card() -> list:
    """Generate a new random card from cards_dict that is not already in cards_played"""
    new = False
    while not new:
        card_rank_idx = random.randint(0,len(cards_dict['rank']) - 1)
        # reinit of card_value_idx leads to a new random num, while I need to keep the same one for both
        #card_value_idx = int(cards_dict['value'][card_rank])
        card_color_idx = random.randint(0, len(cards_dict['color']) - 1)
        new_card = [card_rank_idx,card_rank_idx,card_color_idx]

        if new_card not in cards_played:
            cards_played.append(new_card)
            new = True
    return new_card

def deal_cards():
    """Manages the dealing of the cards to the players"""

def print_comment():
    """Prints a statement about who is drawing an open card in the beginning, or when a card is disclosed"""

def split_cards():
    """
    If your first two cards have the same numerical value, you may split them into two hands.
    The second hand’s bet must be equal to the original bet. If the split pair is Aces, you are limited to a one-card draw on each hand. """


def double_down():
    """
    You can double down in blackjack after receiving your first two cards.
    You may elect to wager an additional amount not to exceed the value of the original bet.
    With a double down, you will be dealt one additional card only.
    """

def insurance():
    """
    If the dealer’s face-up card is an Ace, you may elect to take insurance.
    Insurance in blackjack is a wager that the dealer has a blackjack.
    You may bet up to one-half of your original bet.
    Insurance bets pay 2 to 1 if the dealer has a blackjack, but lose in all other instances.
    """

def surrender():
    """
    Players have the option of surrendering one half of their original wager after receiving their first two cards.
    If you surrender your cards, the dealer will take half of your wager. (Note: The Surrender option is not available in the Double Deck game.)
    """

options_dict = {
    "/": split_cards,
    "*": double_down,
    "+": insurance,
    "-": surrender
}

cards_dict = {
    "rank" : ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"],
    "value": ["2","3","4","5","6","7","8","9","10","10","10","10","11"],
    "color": ["hearts", "diamonds","spades","clubs"],
}

# dict of lists
# [0,0,0][0,0,0]
# index 0,1 cannot ever appear 2 times in a card draw
# index 2 always the same as index 0 to get the card value
# key can be any number 0 to x , access value to compare
# special treatment for ACE - option to select value = 1
# populate dict while game is running, check if random generates existing value, rerun card_draw_def()
cards_played = []


#first player is dealer
player_hand = {
    'name':     [],
    'wager':    [],
    'cards':    [], # list can contain multiple lists for each card-deck in a split
    'sum_value':[]
}


game = True
#
# while game:
#do basic init

#for x in range(len(player["name"])) x is index of player
gather_players()
decide_game_mode()





draw_card()






