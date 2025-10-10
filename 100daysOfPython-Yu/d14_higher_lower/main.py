"""Breakdown:
-logo of the game gets printed
-data A (values from list/dict "data" by value: name, description, country -> choosen randomly) gets printed
-logo : VS gets printed
-data B (values from list/dict "data" by value: name, description, country -> choosen randomly) gets printed
-Player chooses if option B hast HIGHER or LOWER amount of followers
-if Player wrong game is over/ counter is displayed
-else Player is right and counter += 1 / data A = data B / new data B is again choosen randomly from list/dict / game repeats 
"""

"""To-Do-list:
+print game logo
-from constants.data: 
    -choose random list item
    -get list items keys and values > move to new constant via dict comprehension 
    -assign to dict_A/B as a list
    -embedd into a def
-use def in main to create random lists for A,B 
-compare follower_count of A,B (higher, lower)
-if player wrong > print(lost + constants.round_count)
-else player wins round > reassign A = B ; create new B via def; rerun until is_game_lost = True
"""

"""Comments:
"""

import constants
import functions
import os

is_playing = True
counter = 0


while is_playing:
    print (constants.logo)
    functions.populate_AB()
    
    print(f"Your current score is: {counter}")
    print(f"Compare A: {constants.dict_A[0]}, a {constants.dict_A[2]}, from {constants.dict_A[3]}.")
    print(constants.vs)
    print(f"Against B: {constants.dict_B[0]}, a {constants.dict_B[2]}, from {constants.dict_B[3]}.")
    higher_lower_choice = input("Who has more follower? Type 'A' or 'B': ")
    
    if (higher_lower_choice == 'A') and (constants.dict_A[1] > constants.dict_B[1]) :
        #print Correct - message
        print(f"You're right {constants.dict_A[0]} has {constants.dict_A[1]} million followers and {constants.dict_B[0]} has {constants.dict_B[1]} million followers")
        
        #set A=B
        constants.dict_A = constants.dict_B
        
        #generate new B
        functions.repopulate_B()
        
        #adjust counter
        counter += 1
        
        #clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        #repeat game
    elif (higher_lower_choice == 'B') and (constants.dict_A[1] < constants.dict_B[1]) :
        #print Correct - message
        print(f"You're right A: {constants.dict_A[0]} has {constants.dict_A[1]} million followers and B: {constants.dict_B[0]} has {constants.dict_B[1]} million followers")
        
        #set A=B
        constants.dict_A = constants.dict_B
        
        #generate new B
        functions.repopulate_B()
        
        #adjust counter
        counter += 1
        
        #clear console
        os.system('cls' if os.name == 'nt' else 'clear')
        
        #repeat game
    else:
        #print loose message
        print(f"You're wrong A: {constants.dict_A[0]} has {constants.dict_A[1]} million followers and B: {constants.dict_B[0]} has {constants.dict_B[1]} million followers.")
        print("You've lost the game!")
        
        #print counter
        print(f"Your final score is: {counter}")
        #end game
        is_playing = False
        
