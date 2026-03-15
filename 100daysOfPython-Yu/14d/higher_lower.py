import random
from unittest import skip

import pandas_script as celebrity_csv_script


celebrities_dict = celebrity_csv_script.transform_list_to_dict()

#TODO 1: List of People
#TODO 2: Generate random Number to assign it to every one of the people
#TODO 3: Deconstruct the game: Think of relevant functions parameters and variable_names

#### Set magic numbers ####

#Entries in the csv file
AMOUNT_OF_ENTRIES = 49

#Set score variable for right guesses
user_score = 0
#Boolean for the running/exiting the loop
guessing_on_track = True

#### Define functions here ####

def increase_user_score():
    '''Increases current user_score by +1'''
    global user_score
    user_score += 1


def compare_equality(number1, number2):
    '''Compares if number of followers of both celebs are unequal --> one is higher than the other'''
    if number1 != number2:
        return False
    else:
        return True

#get random entry from celebrities.csv
def retrieve_rand_celebrity_from_dict():
    '''Generates a random number for a celebrity and returns a single entry as a dictionary'''
    random_celebrities_dict_entry_number = random.randint(0,AMOUNT_OF_ENTRIES)
    random_celebrity_dict_entry = celebrities_dict[random_celebrities_dict_entry_number]
    return random_celebrity_dict_entry

def retrieve_rand_celebrity_list(random_celebrity_dict_entry):
    '''Resaves a single celebrity entry, to a list of values'''
    owner = random_celebrity_dict_entry['Owner']
    number = random_celebrity_dict_entry['Followers (Millions)']
    activity = random_celebrity_dict_entry['Profession/Activity']
    country = random_celebrity_dict_entry['Country']
    celebrity_entry_list = [owner,number,activity,country]
    return celebrity_entry_list

# def get_follower_count():
#     num1 = retrieve_rand_celebrity_from_dict()
#     celebrity_data_list1 = retrieve_rand_celebrity_list(num1)
#     follower_count = celebrity_data_list1[1]
#     return follower_count

def generate_comparison_string(celebrity_entry_list):
    """
    GENERATE COMPARISON STRING for a given instagram account
    """
    random_celebrity = celebrity_entry_list

    celebrity_string = (f"{random_celebrity[0]}, a {celebrity_entry_list[2]}, from {celebrity_entry_list[3]}")
    return celebrity_string


#### GAME ####

isGame = True
while isGame:

    num1 = retrieve_rand_celebrity_from_dict()
    celebrity_data_list1 = retrieve_rand_celebrity_list(num1)
    follower_count_1 = celebrity_data_list1[1]

    isWinning = True
    while isWinning:
        # Generate both entries and retrieve their data

        # print ascii when starting the game:
        print(r''' 
         _   _ _       _                 _                           
        | | | (_) __ _| |__   ___ _ __  | |    _____      _____ _ __ 
        | |_| | |/ _` | '_ \ / _ \ '__| | |   / _ \ \ /\ / / _ \ '__|
        |  _  | | (_| | | | |  __/ |    | |__| (_) \ V  V /  __/ |   
        |_|_|_|_|\__, |_| |_|\___|_|    |_____\___/ \_/\_/ \___|_|   
         / ___|_ |___/___  ___ ___  ___ _ __                         
        | |  _| | | |/ _ \/ __/ __|/ _ \ '__|                        
        | |_| | |_| |  __/\__ \__ \  __/ |                           
         \____|\__,_|\___||___/___/\___|_|                                                      
                                                                      ''')

        isEqual = True
        while isEqual:
            num2 = retrieve_rand_celebrity_from_dict()
            celebrity_data_list2 = retrieve_rand_celebrity_list(num2)
            follower_count_2 = celebrity_data_list2[1]

            # Compare their numbers, if unequal repeat generation, else use for the comparison
            isEqual = compare_equality(follower_count_1, follower_count_2)

        celebrity_string_1 = generate_comparison_string(celebrity_data_list1)
        print(f"Compare A: {celebrity_string_1}")
        print(r'''
        __     ______   
        \ \   / / ___|  
         \ \ / /\___ \  
          \ V /  ___) | 
           \_/  |____(_)
        ''')

        celebrity_string_2 = generate_comparison_string(celebrity_data_list2)
        print(f"Compare B: {celebrity_string_2}")

        # print(r'''
        #  ____
        # / ___|  ___ ___  _ __ ___ _
        # \___ \ / __/ _ \| '__/ _ (_)
        #  ___) | (_| (_) | | |  __/_
        # |____/ \___\___/|_|  \___(_)
        #
        # {user_score}
        # ''')

        user_choice = input('Who has more followers? Type "A" or "B": ')
        if user_choice == "A" and (celebrity_data_list1[1] > celebrity_data_list2[1]):
            increase_user_score()
            print(f"This is correct!\n{celebrity_data_list1[0]} has more followers!\nYour new score is {user_score}\n")
        elif user_choice == "B" and (celebrity_data_list2[1] > celebrity_data_list1[1]):
            increase_user_score()
            print(f"This is correct!\n{celebrity_data_list2[0]} has more followers!\nYour new score is {user_score}\n")
            celebrity_data_list1 = celebrity_data_list2
            follower_count_1 = follower_count_2
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            isWinning = False
            isGame = False


