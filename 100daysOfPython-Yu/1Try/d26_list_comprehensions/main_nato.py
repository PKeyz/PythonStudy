
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

#open/safe csv to dict with pandas
import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')

# #for each row in df create dict entry with key == word[0] and value == word
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()

# #for each letter in user_input, get the phonetic code word from nato_dict
# #and append to list
nato_list = [nato_dict[letter] for letter in user_input]

