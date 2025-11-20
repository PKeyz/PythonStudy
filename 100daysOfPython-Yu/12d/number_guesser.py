import random
from dataclasses import dataclass

# ============================================================================
# GENERAL RUN THROUGH
# ============================================================================
# Number Guessing Game:
# Welcome to NGG!
# I'm thinking of a number between x and y
# Choose a difficulty. Type 'easy' or 'hard':
# You have 10/5 attempts remaining to guess the correct number.
# Make a guess:
# Too high/low!
# You have x attempts left.
# Guess again:
# Make a guess:
# ....
# You guessed right! / The right number was xxxx
# ============================================================================


# ============================================================================
# Configuration
# ============================================================================

class GameConfig:
    """Contains all the magic numbers"""
    LOWEST_NUMBER = 0
    HIGHEST_NUMBER = 100
    DIFFICULTY_EASY = 10
    DIFFICULTY_HARD = 5
    NO_REMAINING_ATTEMPTS = 0

# ============================================================================
# DOMAIN MODELS - Pure data, no game logic
# ============================================================================
class Enums:
    """Contains enum values of the game"""
    EASY = "easy"
    DIFFICULT = "hard"
    GUESS_CORRECT = "correct"
    GUESS_TOO_HIGH = "too high"
    GUESS_TOO_LOW = "too low"
# ============================================================================
# Game Entities
# ============================================================================

@dataclass
class Guesser:
    """Guesser class generates a random number in a range, checks if user_guess is correct"""
    def __init__(self):
        self.rand_num = random.randint(GameConfig.LOWEST_NUMBER,GameConfig.HIGHEST_NUMBER)

    def check_number_correctness(self, user_number) -> str:
        """Checks if the user number is correct. If not prompts to try again"""
        if self.rand_num == user_number:
            return Enums.GUESS_CORRECT
        elif self.rand_num < user_number:
            return Enums.GUESS_TOO_HIGH
        elif self.rand_num > user_number:
            return Enums.GUESS_TOO_LOW
        else:
            pass

# ============================================================================
# USER INTERFACE - Separated from game logic
# ============================================================================

class ConsoleUI:
    """Handles UI i/o"""

    @staticmethod
    def print_welcome_screen():
        """Prints the welcome screen message, including LOWEST_NUMBER and HIGHEST_NUMBER"""
        print(f"""# ============================================================================
    # WELCOME TO THE NUMBER GUESSING GAME! 
    # ============================================================================\n I'm thinking of a number
    between {GameConfig.LOWEST_NUMBER} and {GameConfig.HIGHEST_NUMBER}""")

    @staticmethod
    def choose_difficulty():
        """Prompts the user for the game difficulty setting"""
        game_difficulty = input(f"Choose a difficulty. Print '{Enums.EASY}' or '{Enums.DIFFICULT}': ")
        return game_difficulty

    @staticmethod
    def prompt_user_guess(amount_attempts) -> int:
        """ask the user to place his guess"""
        user_guess_num = int(input(f"You have {amount_attempts} attempts left.\nMake a guess: "))
        return user_guess_num

    @staticmethod
    def correct(user_number):
        """Prints"""
        print(f"You guessed right!\nThe right number is {user_number}")

    @staticmethod
    def too_high():
        print(f"Too high!\nGuess again.")

    @staticmethod
    def too_low():
        print(f"Too low!\nGuess again.")

# ============================================================================
# GAME COORDINATOR
# ============================================================================
class Game:
    """Coordinates general game flow"""
    ui = ConsoleUI()
    def define_max_attempt_amount(self):
        """Counts attempts of the user to finish the game if the amount is reached"""
        difficulty_level = self.ui.choose_difficulty()
        if difficulty_level == Enums.EASY:
            player_attempts = GameConfig.DIFFICULTY_EASY
        elif difficulty_level == Enums.DIFFICULT:
            player_attempts = GameConfig.DIFFICULTY_HARD
        else:
            "You failed the game even before starting!"
        return player_attempts

    def run(self):
        """Game loop repeats for the amount of times set in difficulty settings"""
        ui = ConsoleUI()
        guesser = Guesser()

        self.ui.print_welcome_screen()
        max_attempts = self.define_max_attempt_amount()
        user_tries = max_attempts
        while user_tries != GameConfig.NO_REMAINING_ATTEMPTS  :
            user_guess = ui.prompt_user_guess(amount_attempts=user_tries)
            number_verification_string = guesser.check_number_correctness(user_number=user_guess)
            if number_verification_string == Enums.GUESS_TOO_HIGH:
                ui.too_high()
                user_tries -= 1
            elif number_verification_string == Enums.GUESS_TOO_LOW:
                ui.too_low()
                user_tries -= 1
            else:
                ui.correct(user_number=user_guess)
                break


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    game = Game()
    game.run()