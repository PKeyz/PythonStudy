import ascii


def print_ascii_art():
    print(ascii.ascii_img)

def print_welcome_message():
    print("Welcome to the secret auction program.")

def is_auction_on() -> bool:
    """find out who else participates to move on, or finish calculation"""
    any_bidder = input("Are there any other bidders? Type 'yes', or type ANY BUTTON. \n").lower()
    if any_bidder == "yes":
        auction_status = True
    else:
        auction_status = False

    return auction_status

def ask_user_data():
    """get user data to add to list -> dict for further calculation"""
    name = input("What is your name? \n").lower()
    bid = int(input("What is your bid in $ ? \n"))
    return name, bid

def add_user_id():
    name_index = len(name_dict['name'])-1
    user_id_list.append(name_index)
    return name_index

def confirm_user_input(name, bid, user_id):
    name_index = name_dict['name'].index(name)
    bid_index = name_dict['bid'].index(bid)

    if name_index == bid_index == user_id:
        print(f"Your ID is: {user_id}, your NAME is : {name} and you BID is: ${bid}. \n")


def find_highest_bidder(bid_list) -> list:
    """iterate over dict find the highest value, get its index, find index of according name, return both"""

    duplicate_bids = []
    highest_bid = 0

    for index, any_bid in enumerate(bid_list):
        if any_bid > highest_bid:
            duplicate_bids.clear()
            duplicate_bids.append(index)
            highest_bid = any_bid
        elif any_bid == highest_bid:
            duplicate_bids.append(index)

    return duplicate_bids





auction_on = True

print_ascii_art()
print_welcome_message()

name = ""
bid = 0

name_list = []
bid_list = []
user_id_list = []

name_dict = {'name': name_list, 'bid': bid_list, 'userID':user_id_list}

while auction_on:

    name, bid = ask_user_data()

    name_list.append(name)
    bid_list.append(bid)
    user_id = add_user_id()

    confirm_user_input(name,bid,user_id)

    auction_on = is_auction_on()

highest_bidder = find_highest_bidder(bid_list)

if len(highest_bidder) == 1:
    winner_index = highest_bidder[0]
    winner_name = name_dict['name'][winner_index]
    winner_bid = name_dict['bid'][winner_index]
    winner_user_id = name_dict['userID'][winner_index]
    print(f"The winner is: {winner_name}, with ${winner_bid} and UserID: {winner_user_id}")
else:
    for index in highest_bidder:
        co_winner_name = name_dict['name'][index]
        co_winner_bid = name_dict['bid'][index]
        co_winner_user_id = name_dict['userID'][index]
        print(f"UserID {co_winner_user_id} with the name: {co_winner_name} bid the same $ amount as another user.\n "
              f"You need to bid higher, to win the auction!")
    auction_on = True