import random
from dataclasses import dataclass

# ============================================================================
# GENERAL RUN THROUGH
# ============================================================================
# Number Guessing Game:
# Welcome to NGG!
# I'm thinking of a number between x and y
# Choose a difficuly. Type 'easy' or 'hard':
# You have 10/5 attempts remaining to guess the correct number.
# Make a guess:
# Too high/low..
# Guess again:
# You have x attempts left.
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

# ============================================================================
# DOMAIN MODELS - Pure data, no game logic
# ============================================================================
class Enums:
    """Contains enum values of the game"""
    EASY = "easy"
    DIFFICULT = "hard"

# ============================================================================
# Game Entity
# ============================================================================

@dataclass
class Guesser:
    """Generates a random number in a range"""

    # def generate_a_rand_num(self):
    #     """Generates a random number for the user to guess"""
    #     rand_num = random.randint(GameConfig.LOWEST_NUMBER,GameConfig.HIGHEST_NUMBER)
    #     return rand_num

    # def __init__(self,rand_num:int):
    #     self.rand_num = random.randint(GameConfig.LOWEST_NUMBER,GameConfig.HIGHEST_NUMBER)

    rand_num = random.randint(GameConfig.LOWEST_NUMBER,GameConfig.HIGHEST_NUMBER)


# ============================================================================
# USER INTERFACE - Separated from game logic
# ============================================================================

class ConsoleUI:
    """Handles UI i/o"""

    @staticmethod
    def print_welcome_screen(self):
        """Prints the welcome screen message, including LOWEST_NUMBER and HIGHEST_NUMBER"""
        print(f"""# ============================================================================
# WELCOME TO THE NUMBER GUESSING GAME! 
# ============================================================================\n I'm thinking of a number
between {GameConfig.LOWEST_NUMBER} and {GameConfig.HIGHEST_NUMBER}""")

    # @staticmethod
    # def choose_difficulty():
    #     """Prompts the user for the game difficulty setting"""
    #     game_difficulty = input(f"Choose a difficulty. Print '{Enums.EASY}' or '{Enums.DIFFICULT}': ")
    #     return game_difficulty



# ============================================================================
# GAME COORDINATOR
# ============================================================================
class Game:
    """Coordinates general game flow"""

    # def __init__(self):
    #     self.ui = ConsoleUI()

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

    def define_max_attempt_amount(self):
        """Counts attempts of the user to finish the game if the amount is reached"""
        difficulty_level = self.choose_difficulty()
        if difficulty_level == Enums.EASY:
            player_attempts = GameConfig.DIFFICULTY_EASY
        elif difficulty_level == Enums.DIFFICULT:
            player_attempts = GameConfig.DIFFICULTY_HARD
        else:
            "You failed the game even before starting!"
        return player_attempts

    def run(self):
        self.print_welcome_screen()
        attempts = self.define_max_attempt_amount()
        for x in attempts:
            x



# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    game = Game()
    game.run()