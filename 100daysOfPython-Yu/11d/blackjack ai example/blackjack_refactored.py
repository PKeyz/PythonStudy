"""
Blackjack Game - Refactored with Clean Architecture
Demonstrates proper separation of concerns and testable design
"""
from typing import List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import random


# ============================================================================
# CONFIGURATION
# ============================================================================
class GameConfig:
    """All game constants in one place"""
    MIN_WAGER = 100
    MAX_WAGER = 1000
    MAX_PLAYERS = 5
    DEALER_HIT_THRESHOLD = 17
    BLACKJACK_VALUE = 21
    MULTIPLIER_6_TO_5 = 1.2
    MULTIPLIER_3_TO_2 = 1.5


class Suit(Enum):
    """Card suits"""
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    SPADES = "Spades"
    CLUBS = "Clubs"


class Rank(Enum):
    """Card ranks with their blackjack values"""
    TWO = ("2", 2)
    THREE = ("3", 3)
    FOUR = ("4", 4)
    FIVE = ("5", 5)
    SIX = ("6", 6)
    SEVEN = ("7", 7)
    EIGHT = ("8", 8)
    NINE = ("9", 9)
    TEN = ("10", 10)
    JACK = ("Jack", 10)
    QUEEN = ("Queen", 10)
    KING = ("King", 10)
    ACE = ("Ace", 11)
    
    def __init__(self, display_name: str, value: int):
        self.display_name = display_name
        self.value = value


# ============================================================================
# DOMAIN MODELS
# ============================================================================
@dataclass(frozen=True)
class Card:
    """Immutable card representation"""
    rank: Rank
    suit: Suit
    
    def __str__(self) -> str:
        return f"{self.rank.display_name} of {self.suit.value}"
    
    @property
    def value(self) -> int:
        return self.rank.value


class Hand:
    """Represents a hand of cards with scoring logic"""
    
    def __init__(self):
        self.cards: List[Card] = []
    
    def add_card(self, card: Card):
        """Add a card to the hand"""
        self.cards.append(card)
    
    def get_value(self) -> int:
        """Calculate hand value, handling Aces intelligently"""
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == Rank.ACE)
        
        # Convert Aces from 11 to 1 if needed to avoid bust
        while total > GameConfig.BLACKJACK_VALUE and aces > 0:
            total -= 10
            aces -= 1
        
        return total
    
    def is_bust(self) -> bool:
        """Check if hand value exceeds 21"""
        return self.get_value() > GameConfig.BLACKJACK_VALUE
    
    def is_blackjack(self) -> bool:
        """Check if hand is a natural blackjack (21 with 2 cards)"""
        return (len(self.cards) == 2 and 
                self.get_value() == GameConfig.BLACKJACK_VALUE)
    
    def clear(self):
        """Remove all cards from hand"""
        self.cards.clear()
    
    def __str__(self) -> str:
        return ", ".join(str(card) for card in self.cards)


class Deck:
    """Standard 52-card deck with drawing logic"""
    
    def __init__(self):
        self.cards: List[Card] = []
        self.reset()
    
    def reset(self):
        """Create a fresh shuffled deck"""
        self.cards = [
            Card(rank, suit) 
            for suit in Suit 
            for rank in Rank
        ]
        random.shuffle(self.cards)
    
    def draw(self) -> Card:
        """Draw one card from the deck"""
        if not self.cards:
            self.reset()  # Reshuffle if deck empty
        return self.cards.pop()
    
    def cards_remaining(self) -> int:
        return len(self.cards)


class Player:
    """Represents a player with name, wager, and hands"""
    
    def __init__(self, name: str, wager: int):
        self.name = name
        self.initial_wager = wager
        self.wager = wager
        self.hands: List[Hand] = [Hand()]  # Support for splits
        self.is_standing = False
    
    def get_current_hand(self) -> Hand:
        """Get the primary hand"""
        return self.hands[0]
    
    def reset_for_new_round(self):
        """Prepare for a new round"""
        self.hands = [Hand()]
        self.is_standing = False
        self.wager = self.initial_wager


class Dealer(Player):
    """Dealer with specific rules"""
    
    def __init__(self):
        super().__init__("Dealer", 0)
    
    def should_hit(self) -> bool:
        """Dealer must hit on 16 or less, stand on 17+"""
        return self.get_current_hand().get_value() < GameConfig.DEALER_HIT_THRESHOLD
    
    def get_upcard(self) -> Optional[Card]:
        """Get the dealer's visible first card"""
        hand = self.get_current_hand()
        return hand.cards[0] if hand.cards else None


# ============================================================================
# GAME LOGIC
# ============================================================================
class BlackjackGame:
    """Core game engine - no I/O, pure logic"""
    
    def __init__(self, multiplier: float):
        self.deck = Deck()
        self.players: List[Player] = []
        self.dealer = Dealer()
        self.multiplier = multiplier
    
    def add_player(self, name: str, wager: int) -> Player:
        """Add a player to the game"""
        player = Player(name, wager)
        self.players.append(player)
        return player
    
    def deal_initial_cards(self):
        """Deal 2 cards to each player and dealer"""
        # First card to everyone
        for player in self.players:
            player.get_current_hand().add_card(self.deck.draw())
        self.dealer.get_current_hand().add_card(self.deck.draw())
        
        # Second card to everyone
        for player in self.players:
            player.get_current_hand().add_card(self.deck.draw())
        self.dealer.get_current_hand().add_card(self.deck.draw())
    
    def hit(self, player: Player) -> Card:
        """Give player another card"""
        card = self.deck.draw()
        player.get_current_hand().add_card(card)
        return card
    
    def play_dealer_turn(self) -> List[Card]:
        """Play dealer's turn according to rules"""
        drawn_cards = []
        while self.dealer.should_hit():
            card = self.deck.draw()
            self.dealer.get_current_hand().add_card(card)
            drawn_cards.append(card)
        return drawn_cards
    
    def calculate_result(self, player: Player) -> Tuple[str, int]:
        """
        Calculate result for a player.
        Returns (outcome, final_wager) where outcome is:
        'blackjack', 'win', 'push', 'lose', 'bust'
        """
        player_hand = player.get_current_hand()
        dealer_hand = self.dealer.get_current_hand()
        
        # Player bust
        if player_hand.is_bust():
            return ('bust', 0)
        
        # Player blackjack
        if player_hand.is_blackjack() and not dealer_hand.is_blackjack():
            winnings = int(player.wager * self.multiplier)
            return ('blackjack', player.wager + winnings)
        
        # Both blackjack - push
        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            return ('push', player.wager)
        
        player_value = player_hand.get_value()
        dealer_value = dealer_hand.get_value()
        
        # Dealer bust or player higher
        if dealer_hand.is_bust() or player_value > dealer_value:
            return ('win', player.wager * 2)
        
        # Tie
        if player_value == dealer_value:
            return ('push', player.wager)
        
        # Dealer wins
        return ('lose', 0)
    
    def reset_for_new_round(self):
        """Prepare for a new round"""
        for player in self.players:
            player.reset_for_new_round()
        self.dealer = Dealer()
        
        # Reshuffle if deck is low
        if self.deck.cards_remaining() < (len(self.players) + 1) * 10:
            self.deck.reset()


# ============================================================================
# USER INTERFACE
# ============================================================================
class ConsoleUI:
    """Handles all user input/output - separated from game logic"""
    
    @staticmethod
    def print_separator():
        print("=" * 80)
    
    @staticmethod
    def print_welcome():
        print("=" * 80)
        print(" " * 30 + "BLACKJACK")
        print("=" * 80)
    
    @staticmethod
    def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
        """Get validated integer input"""
        while True:
            try:
                value = int(input(prompt))
                if min_val <= value <= max_val:
                    return value
                print(f"Please enter a number between {min_val} and {max_val}")
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    @staticmethod
    def get_non_empty_string(prompt: str) -> str:
        """Get non-empty string input"""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty!")
    
    @staticmethod
    def get_yes_no(prompt: str) -> bool:
        """Get yes/no response"""
        while True:
            response = input(prompt).strip().lower()
            if response in ['y', 'yes']:
                return True
            if response in ['n', 'no']:
                return False
            print("Please enter 'y' or 'n'")
    
    @staticmethod
    def setup_game() -> Tuple[List[Tuple[str, int]], float]:
        """
        Gather all game setup information.
        Returns (player_info_list, multiplier)
        """
        ConsoleUI.print_welcome()
        
        # Get game mode
        print("\nChoose game mode:")
        print("1. 3:2 payout (traditional, better for players)")
        print("2. 6:5 payout (house advantage)")
        mode = ConsoleUI.get_valid_int("Enter choice (1-2): ", 1, 2)
        multiplier = (GameConfig.MULTIPLIER_3_TO_2 if mode == 1 
                     else GameConfig.MULTIPLIER_6_TO_5)
        
        # Get players
        players_info = []
        print(f"\nMaximum {GameConfig.MAX_PLAYERS} players allowed.")
        
        while len(players_info) < GameConfig.MAX_PLAYERS:
            name = ConsoleUI.get_non_empty_string(
                f"\nPlayer {len(players_info) + 1} name: "
            )
            wager = ConsoleUI.get_valid_int(
                f"Wager (${GameConfig.MIN_WAGER}-${GameConfig.MAX_WAGER}): ",
                GameConfig.MIN_WAGER,
                GameConfig.MAX_WAGER
            )
            players_info.append((name, wager))
            
            if len(players_info) < GameConfig.MAX_PLAYERS:
                if not ConsoleUI.get_yes_no("Add another player? (y/n): "):
                    break
        
        return players_info, multiplier
    
    @staticmethod
    def show_initial_deal(players: List[Player], dealer: Dealer):
        """Display initial cards dealt"""
        ConsoleUI.print_separator()
        print("INITIAL DEAL:")
        print()
        
        for player in players:
            hand = player.get_current_hand()
            print(f"{player.name}: {hand} (Value: {hand.get_value()})")
        
        upcard = dealer.get_upcard()
        print(f"Dealer: {upcard} and [Hidden]")
        ConsoleUI.print_separator()
    
    @staticmethod
    def get_player_action(player: Player) -> str:
        """Get player's action choice"""
        hand = player.get_current_hand()
        print(f"\n{player.name}'s turn:")
        print(f"Current hand: {hand} (Value: {hand.get_value()})")
        
        while True:
            choice = input("(H)it or (S)tand? ").strip().lower()
            if choice in ['h', 'hit']:
                return 'hit'
            if choice in ['s', 'stand']:
                return 'stand'
            print("Invalid choice! Enter 'h' or 's'")
    
    @staticmethod
    def show_card_drawn(player_name: str, card: Card, hand_value: int):
        """Display a card that was drawn"""
        print(f"{player_name} drew: {card}")
        print(f"Hand value: {hand_value}")
    
    @staticmethod
    def show_bust(player_name: str):
        """Display bust message"""
        print(f"💥 {player_name} BUSTS!")
    
    @staticmethod
    def show_dealer_turn(dealer: Dealer, cards_drawn: List[Card]):
        """Display dealer's turn"""
        ConsoleUI.print_separator()
        print("DEALER'S TURN:")
        hand = dealer.get_current_hand()
        print(f"Dealer reveals: {hand}")
        print(f"Value: {hand.get_value()}")
        
        if cards_drawn:
            print("\nDealer draws:")
            for card in cards_drawn:
                print(f"  {card}")
            print(f"\nFinal hand: {hand}")
            print(f"Final value: {hand.get_value()}")
        
        if hand.is_bust():
            print("💥 Dealer BUSTS!")
        
        ConsoleUI.print_separator()
    
    @staticmethod
    def show_results(players: List[Player], results: List[Tuple[str, int]]):
        """Display final results"""
        print("\n" + "=" * 80)
        print(" " * 35 + "RESULTS")
        print("=" * 80)
        
        for player, (outcome, final_wager) in zip(players, results):
            if outcome == 'blackjack':
                print(f"🎉 {player.name}: BLACKJACK! Wins ${final_wager}")
            elif outcome == 'win':
                print(f"✅ {player.name}: WIN! Wins ${final_wager}")
            elif outcome == 'push':
                print(f"🤝 {player.name}: PUSH (keeps ${final_wager})")
            elif outcome == 'bust':
                print(f"💥 {player.name}: BUST (loses ${player.initial_wager})")
            elif outcome == 'lose':
                print(f"❌ {player.name}: LOSE (loses ${player.initial_wager})")
        
        print("=" * 80)


# ============================================================================
# GAME COORDINATOR
# ============================================================================
class GameCoordinator:
    """Coordinates game flow using game logic and UI"""
    
    def __init__(self):
        self.ui = ConsoleUI()
        self.game: Optional[BlackjackGame] = None
    
    def run(self):
        """Main game loop"""
        # Setup
        players_info, multiplier = self.ui.setup_game()
        self.game = BlackjackGame(multiplier)
        
        for name, wager in players_info:
            self.game.add_player(name, wager)
        
        # Play rounds
        while True:
            self.play_round()
            
            if not self.ui.get_yes_no("\nPlay another round? (y/n): "):
                print("\nThanks for playing!")
                break
            
            self.game.reset_for_new_round()
    
    def play_round(self):
        """Play one complete round"""
        # Deal initial cards
        self.game.deal_initial_cards()
        self.ui.show_initial_deal(self.game.players, self.game.dealer)
        
        # Players' turns
        for player in self.game.players:
            self.play_player_turn(player)
        
        # Dealer's turn (if any players still in)
        if any(not p.get_current_hand().is_bust() for p in self.game.players):
            cards_drawn = self.game.play_dealer_turn()
            self.ui.show_dealer_turn(self.game.dealer, cards_drawn)
        
        # Calculate and show results
        results = [self.game.calculate_result(p) for p in self.game.players]
        self.ui.show_results(self.game.players, results)
    
    def play_player_turn(self, player: Player):
        """Play one player's turn"""
        hand = player.get_current_hand()
        
        # Check for natural blackjack
        if hand.is_blackjack():
            print(f"\n🎉 {player.name} has BLACKJACK!")
            return
        
        # Player actions
        while not player.is_standing and not hand.is_bust():
            action = self.ui.get_player_action(player)
            
            if action == 'stand':
                player.is_standing = True
                print(f"{player.name} stands.")
                break
            
            elif action == 'hit':
                card = self.game.hit(player)
                self.ui.show_card_drawn(player.name, card, hand.get_value())
                
                if hand.is_bust():
                    self.ui.show_bust(player.name)
                    break


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    coordinator = GameCoordinator()
    coordinator.run()
