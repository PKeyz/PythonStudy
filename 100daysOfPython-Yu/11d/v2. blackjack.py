import ascii
import random
ascii.print_ascii_art()

# MVP::
# cards
# deal cards
# dealer and one player
# hit stand bust in a game loop

# MVP Checklist:
# [ ] Deal 2 cards to player
# [ ] Deal 2 cards to dealer (1 hidden)
# [ ] Player can hit or stand
# [ ] Dealer plays (hit until 17+)
# [ ] Determine winner
# [ ] Play again?


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
def print_break_sequence():
    print(r"==============================================================================================")

def gather_players():
    print("The maximum amount of players is 6. \n")
    MAX_PLAYERS = 5
    more_players = True
    MIN_WAGER = 100
    MAX_WAGER = 1000
    while (len(player_hand['name']) <= MAX_PLAYERS) and (more_players):
        #player_hand
        player_name = input("What is your name? \n")
        player_wager = int(input(f"What is your bet between {MIN_WAGER} and {MAX_WAGER}$ ? \n"))
        player_hand['name'].append(player_name)
        player_hand['wager'].append(player_wager)
        ask_for_more_players = input("are any other players at the table? Type 'Y' or ANY KEY \n").lower()
        if ask_for_more_players == 'y':
            more_players = True
        else:
            more_players = False
    # init dealer
    player_name = "Dealer"
    player_wager = random.randint(MIN_WAGER, MAX_WAGER)
    player_hand['name'].append(player_name)
    player_hand['wager'].append(player_wager)

def init_players():
    """Initializes lists and starting values for the players"""
    #for player in range(len(player_hand['name'])):
    player_hand['cards'].append([   []    ])      # Always nested - 1 hand by default
    player_hand['sum_value'].append([0])   # Always a list

def get_player_info(index):
    """Helper Function to acquire player info by index later in the game"""
    return {
        'name': player_hand['name'][index],
        'wager':player_hand['wager'][index],
        'cards':player_hand['cards'][index],
        'sum_value':player_hand['sum_value'][index]
    }

def decide_game_mode() -> float:
    """Player can decide to play 5:6 (wager * 1.2), or 3 to 2 (wager * 1.5)"""
    game_mode = input("Decide on a game mode: We can play 2:3: Type '23', or 5:6: Type '56'. \n")
    if game_mode == '56':
        multiplier = 1.2
    elif game_mode == '23':
        multiplier = 1.5
    return multiplier

def draw_card() -> list:
    """Generate a new random card from cards_dict that is not already in cards_played"""
    new = False
    while not new:
        card_rank_idx = random.randint(0,len(cards_dict['rank']) - 1)
        # reinit of card_value_idx leads to a new random num, while I need to keep the same one for both
        #card_value_idx = int(cards_dict['value'][card_rank])
        card_color_idx = random.randint(0, len(cards_dict['color']) - 1)
        random_card = [card_rank_idx,card_rank_idx,card_color_idx]
        if random_card not in cards_played:
            if random_card[0] == "Ace":
                user_choice_value = input(
                    "You drew an Ace: Do you want to keep it for 1 point, or 11 points? \nPrint '1', or '11' \n")
            #Original ACE is saved to played_cards list for later comparison, but the adjusted Ace goes to player hand
                cards_played.append(random_card)
                if user_choice_value == "1":
                    random_card[1] = user_choice_value
        new_card = random_card
        new = True
        return new_card

def deal_cards():
    """Manages the dealing of the cards to the players"""
    for player in range(len(player_hand['name'])):
        card = draw_card()
        player_hand['cards'][player][0].append(card)  # Always append to hand 0


def transform_card_list_to_str(card) -> str:
    """Takes the card as list and returns two variables with Rank + Color: E.g. card [12,12,2] card_rank = 'Ace', card_color = 'Spaces' """
    card_rank_idx = card[0]
    card_color_idx = card[2]
    card_rank = cards_dict['rank'][card_rank_idx].title()
    card_color = cards_dict['color'][card_color_idx].title()
    return f"{card_rank} of {card_color}"

def print_comment():
    """Prints a statement about who is drawing an open card in the beginning, or when a card is disclosed"""
    LAST_DEALER_CARD = 2
    for player in range(len(player_hand['name'])):
        player_info = get_player_info(player)

        if (player_info['name'] == "Dealer") and (len(player_info['cards'][0]) == LAST_DEALER_CARD):
            print(f"{player_info['name']}'s second card will be kept secret for now.")
        else:
            # Get the newest card from the last hand
            last_hand = player_info['cards'][-1]  # Get last hand
            newest_card = last_hand[-1]  # Get last card from that hand
            card_string = transform_card_list_to_str(newest_card)
            print(f"{player_info['name']} got a {card_string}")

def count_card_value(player_index):
    """Count cards for a specific hand"""
    player_cards = player_hand['cards'][player_index]

    total = 0
    for card in player_cards:
        value_index = card[1]
        card_value = int(cards_dict['value'][value_index])
        total += card_value

    player_hand['sum_value'][player_index] = total
#if player has ace ask if he wants to count it as 11 or 1

def hit(player):
    """Deals an extra card to the user"""
    player_info = get_player_info(player)
    card = draw_card()
    player_hand['cards'][player].append(card)
    print(f"{player_info['name']} draws a card!")

def stand(player):
    """Player has enough cards, turns move to the next player"""
    """Useless function because you just need to skip to the next player"""

def player_options(player):
    player_info = get_player_info(player)
    while player_info['sum_value'] <= 21:
        player_choice = input("HIT: '0' \nSTAND: '1' \n")
        if player_choice in options_dict:
            options_dict[player_choice](player)

    if player_info['sum_value'] >= 21:
        print("BUST! Player hast a total over 21 points")

options_dict = {
    '0': hit,
    '1': stand
    #"/": split_cards,
    #'*': double_down,
    #+': insurance,
    #'-': surrender
}

cards_dict = {
    "rank" : ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"],
    "value": ["2","3","4","5","6","7","8","9","10","10","10","10","11"],
    "color": ["hearts", "diamonds","spades","clubs"],
}

cards_played = []

#last player is dealer
player_hand = {
    'name':     [],
    'wager':    [],
    'cards':    [], # list contains multiple lists for each card
    'sum_value':[]
}


game = True

gather_players()
init_players()
multiplier = decide_game_mode()
while game:

    deal_cards()
    print_comment()
    print_break_sequence()
    for player in range(len(player_hand['name'])):

        deal_cards() # to player and Dealer twice
        print_comment() # to let the users know who got what
        deal_cards()
        print_comment()
        for player in range(len(player_hand['name'])):
            print_break_sequence()

            player_options(player)  # options hit or stand :: +1 card +x to sum_value  check >=< 21 for BUST!









