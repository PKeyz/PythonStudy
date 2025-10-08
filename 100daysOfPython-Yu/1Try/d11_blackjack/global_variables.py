import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
player_bank = 1000
dealer_bank = 10000
game_stake = 0

new_values = []
originalDeck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'Jack','Jack','Jack','Jack','Queen','Queen','Queen','Queen','King','King','King','King','Ace','Ace','Ace','Ace',]
# deck of cards -> shuffle
shuffled_deck = random.sample(originalDeck, len(originalDeck))

player_hand = []
dealer_hand = []
dealer_hand_visible = dealer_hand[1::]

player_points = 0
dealer_points = 0
dealer_points_visible = 0

player_turn = 0
dealer_turn = 0

player_last_turn = True #True = hit False = stand
dealer_last_turn = True #True = hit False = stand

player_points_remaining = 21
dealer_points_remaining = 21

point_limit = 21

