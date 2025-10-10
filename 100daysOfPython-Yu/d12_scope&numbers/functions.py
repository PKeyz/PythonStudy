import constants

def guess_loop(difficulty:str): 
    if difficulty == 'easy':
        attempts = 10
        while (attempts != 0):
            print(f'You have {attempts} attempts remaining to guess the number.')
            guess = int(input("Make a guess: "))
            if guess > constants.guess_number:
                print("Too high\nGuess again.")
                attempts -= 1
            elif guess < constants.guess_number:
                print("Too low\nGuess again.")
                attempts -= 1
            else:
                print(f"You got it! The answer was {constants.guess_number}.")
                break
    elif difficulty == 'hard':
        attempts = 5
        while (attempts != 0):
            print(f'You have {attempts} attempts remaining to guess the number.')
            guess = int(input("Make a guess: "))
            if guess > constants.guess_number:
                print("Too high\nGuess again.")
                attempts -= 1
            elif guess < constants.guess_number:
                print("Too low\nGuess again.")
                attempts -= 1
            else:
                print(f"You got it! The answer was {constants.guess_number}.")
                break