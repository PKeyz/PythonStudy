import random
import pandas_script as celebrity_csv_script


celebrities_dict = celebrity_csv_script.transform_list_to_dict()

#TODO 1: List of People
#TODO 2: Generate random Number to assign it to every one of the people
#TODO 3: Deconstruct the game: Think of relevant functions parameters and variable_names

#### Set magic numbers ####

#Entries in the csv file
AMOUNT_OF_ENTRIES = 50

#Set score variable for right guesses
user_score = 0
#Boolean for the running/exiting the loop
guessing_on_track = True

#### Define functions here ####

#pre-check numbers, if equal rerun random to keep values different
def check_if_numbers_uneven(a,b):
    if a != b:
        return True

#
def higher_lower(user_guess,second_option):
    if user_guess > second_option:
        return True
    else:
        return False

#get random entry from celebrities.csv
def retrieve_rand_celebrity_number():
    random_celebrities_dict_entry_number = random.randint(0,AMOUNT_OF_ENTRIES)
    random_celebrity_dict_entry = celebrities_dict[random_celebrities_dict_entry_number]
    return random_celebrity_dict_entry

def retrieve_rand_celebrity_data(random_celebrity_dict_entry):
    random_celebrity = random_celebrity_dict_entry

    owner = random_celebrity['Owner']
    number = random_celebrity['Followers (Millions)']
    activity = random_celebrity['Profession/Activity']
    country = random_celebrity['Country']
    celebrity_entry_list = [owner,number,activity,country]
    return celebrity_entry_list


def generate_comparison_string(celebrity_entry_list):
    """
    GENERATE COMPARISON STRING for a given instagram account
    """
    random_celebrity = celebrity_entry_list

    print(f"{random_celebrity[0]}, a {celebrity_entry_list[2]}, from {celebrity_entry_list[3]}")


# print ascii when starting the game:
print(r''' _   _ _       _                 _
| | | (_) __ _| |__   ___ _ __  | |    _____      _____ _ __
| |_| | |/ _` | '_ \ / _ \ '__| | |   / _ \ \ /\ / / _ \ '__|
|  _  | | (_| | | | |  __/ |    | |__| (_) \ V  V /  __/ |
|_|_|_|_|\__, |_| |_|\___|_|    |_____\___/ \_/\_/ \___|_|
 / ___|_ |___/___  ___ ___  ___ _ __
| |  _| | | |/ _ \/ __/ __|/ _ \ '__|
| |_| | |_| |  __/\__ \__ \  __/ |
 \____|\__,_|\___||___/___/\___|_|                           
                                                              ''')

num1 = retrieve_rand_celebrity_number()
celebrty_data_list = retrieve_rand_celebrity_data(num1)
generate_comparison_string(celebrty_data_list)
print(r'''
__     ______   
\ \   / / ___|  
 \ \ / /\___ \  
  \ V /  ___) | 
   \_/  |____(_)
''')
# enter loop based on boolean e.g. UserGuessCorrect = True

#while (guessing_on_track):

num2 = retrieve_rand_celebrity_number()
celebrty_data_list = retrieve_rand_celebrity_data(num2)
generate_comparison_string(celebrty_data_list)

# print Compare A + their attr + their attr. values
# print Compare B + their attr + their attr. values
# compare who has higher value as float
# save as some higher/winner variable
# take user input as A | B .toLowerCase
# if value not A | B .. prompt to repeat input
# elif wrong guess  !+ higher value/winner :
#
#     exit loop
#
#     print You lost with score x text
# else: score += 1
#     A = last winner
#     B = new random entry from list
#     repeat loop



# guess who has more followers in M  - A or B
#
# when False -> Print you lost + score of right answers
#
# if right B becomes new A + new B is generated from dict
#     repeat the cycle
#     += 1 to score for each right guess

#     terminate game when guess = False
#     display score

