import random

#Reads word_list.txt
#Adds len(words) >= 4 into word_list [] for later iteration
with open("word_list.txt","r") as word_text_file:
    lines = word_text_file.readlines()

    word_list = []

    for line in lines:
        line = line.strip()
        as_list = line.split(",")
        if len(line) >= 4:
            word_list.append(line)

#print(word_list) test of word_list[]

#starting img print before loop starts
hangman_intro_print = r""" /$$   /$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$      /$$  /$$$$$$  /$$   /$$
| $$  | $$ /$$__  $$| $$$ | $$ /$$__  $$| $$$    /$$$ /$$__  $$| $$$ | $$
| $$  | $$| $$  \ $$| $$$$| $$| $$  \__/| $$$$  /$$$$| $$  \ $$| $$$$| $$
| $$$$$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$| $$ $$/$$ $$| $$$$$$$$| $$ $$ $$
| $$__  $$| $$__  $$| $$  $$$$| $$|_  $$| $$  $$$| $$| $$__  $$| $$  $$$$
| $$  | $$| $$  | $$| $$\  $$$| $$  \ $$| $$\  $ | $$| $$  | $$| $$\  $$$
| $$  | $$| $$  | $$| $$ \  $$|  $$$$$$/| $$ \/  | $$| $$  | $$| $$ \  $$
|__/  |__/|__/  |__/|__/  \__/ \______/ |__/     |__/|__/  |__/|__/  \__/                                                                    
"""
print(hangman_intro_print)

#hangman img list, prints at each step according to user life count
hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

#Add counter with each mistake
hangman_count = 0

user_life = 6


#Random word choice from word_list[]
random_word = random.choice(word_list).lower()
#Word transformed into list of chars
random_word_list = list(random_word)
#User progress in guessing the word
word_to_guess = list("_" * len(random_word_list))
#Total list of letters guessed by the user
guessed_letters_list = []

#Init hangman print with count = 0
print(hangman_pics[hangman_count])


while (user_life != 0) and (hangman_count < 7) and (random_word_list != word_to_guess):
    prompt_word_to_guess = "Word to guess: "
    word_guess_print = prompt_word_to_guess + "".join(word_to_guess)
    print(word_guess_print)
    # Display
    guess_a_letter = str(input("Guess a letter:")).lower()


    if guess_a_letter in guessed_letters_list:
        print(f"You've already guessed {guess_a_letter}")
        print(hangman_pics[hangman_count])

    elif guess_a_letter not in random_word_list:
        print(f"You guessed {guess_a_letter}, that's not in the word. You lose a life.")
        hangman_count += 1
        user_life -= 1
        print(hangman_pics[hangman_count])
        print(f"****************************{user_life}/6 LIVES LEFT****************************")

    elif guess_a_letter in random_word_list:
        for letter in range(len(random_word_list)):
            if random_word_list[letter] == guess_a_letter:
                word_to_guess[letter] = guess_a_letter

    else:
        print("This is probably not a letter. Try again!")
    guessed_letters_list.append(guess_a_letter)

if user_life == 0:
    print(hangman_pics[hangman_count])
    print(f"****************************NO LIVES LEFT, YOU LOSE! ****************************")

if random_word_list == word_to_guess:
    print("".join(word_to_guess))
    print("YOU WIN!")