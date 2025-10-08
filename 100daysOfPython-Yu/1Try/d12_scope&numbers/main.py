
import functions

"""_summary_
could export constants to const 
could export def to functions
"""


print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

functions.guess_loop(difficulty)

