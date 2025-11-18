"""
Simple Turn-Based Battle Game
Demonstrates clean class structure and separation of concerns
"""
from typing import Optional
from dataclasses import dataclass
from enum import Enum
import random


# ============================================================================
# CONFIGURATION - All magic numbers in one place
# ============================================================================
class GameConfig:
    PLAYER_STARTING_HP = 100
    PLAYER_STARTING_MANA = 50
    ENEMY_MIN_HP = 50
    ENEMY_MAX_HP = 100
    ATTACK_MIN_DAMAGE = 10
    ATTACK_MAX_DAMAGE = 20
    SPELL_DAMAGE = 35
    SPELL_MANA_COST = 20
    HEAL_AMOUNT = 30
    HEAL_MANA_COST = 15


# ============================================================================
# DOMAIN MODELS - Pure data, no game logic
# ============================================================================
class ActionType(Enum):
    ATTACK = "attack"
    SPELL = "spell"
    HEAL = "heal"
    DEFEND = "defend"


@dataclass
class BattleAction:
    """Represents a single action taken in battle"""
    action_type: ActionType
    actor_name: str
    damage: int = 0
    healing: int = 0
    mana_cost: int = 0
    
    def describe(self) -> str:
        """Return a human-readable description of the action"""
        if self.action_type == ActionType.ATTACK:
            return f"{self.actor_name} attacks for {self.damage} damage!"
        elif self.action_type == ActionType.SPELL:
            return f"{self.actor_name} casts a spell for {self.damage} damage!"
        elif self.action_type == ActionType.HEAL:
            return f"{self.actor_name} heals for {self.healing} HP!"
        elif self.action_type == ActionType.DEFEND:
            return f"{self.actor_name} defends, reducing incoming damage!"
        return ""


# ============================================================================
# CORE GAME ENTITIES - Business logic
# ============================================================================
class Character:
    """Base class for all battle participants"""
    
    def __init__(self, name: str, max_hp: int, max_mana: int = 0):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.max_mana = max_mana
        self.current_mana = max_mana
        self.is_defending = False
    
    def take_damage(self, amount: int) -> int:
        """Apply damage, return actual damage taken after defense"""
        actual_damage = amount // 2 if self.is_defending else amount
        self.current_hp = max(0, self.current_hp - actual_damage)
        self.is_defending = False  # Defense only lasts one turn
        return actual_damage
    
    def heal(self, amount: int) -> int:
        """Heal up to max HP, return actual amount healed"""
        actual_healing = min(amount, self.max_hp - self.current_hp)
        self.current_hp += actual_healing
        return actual_healing
    
    def use_mana(self, amount: int) -> bool:
        """Try to use mana, return success"""
        if self.current_mana >= amount:
            self.current_mana -= amount
            return True
        return False
    
    def is_alive(self) -> bool:
        return self.current_hp > 0
    
    def defend(self):
        """Set defending state for next attack"""
        self.is_defending = True
    
    def get_stats(self) -> str:
        """Return formatted stats string"""
        stats = f"{self.name}: {self.current_hp}/{self.max_hp} HP"
        if self.max_mana > 0:
            stats += f", {self.current_mana}/{self.max_mana} Mana"
        return stats


class Player(Character):
    """Player with special abilities"""
    
    def __init__(self, name: str):
        super().__init__(
            name=name,
            max_hp=GameConfig.PLAYER_STARTING_HP,
            max_mana=GameConfig.PLAYER_STARTING_MANA
        )
    
    def attack(self) -> BattleAction:
        """Perform basic attack"""
        damage = random.randint(
            GameConfig.ATTACK_MIN_DAMAGE,
            GameConfig.ATTACK_MAX_DAMAGE
        )
        return BattleAction(
            action_type=ActionType.ATTACK,
            actor_name=self.name,
            damage=damage
        )
    
    def cast_spell(self) -> Optional[BattleAction]:
        """Cast spell if enough mana"""
        if not self.use_mana(GameConfig.SPELL_MANA_COST):
            return None
        
        return BattleAction(
            action_type=ActionType.SPELL,
            actor_name=self.name,
            damage=GameConfig.SPELL_DAMAGE,
            mana_cost=GameConfig.SPELL_MANA_COST
        )
    
    def heal_self(self) -> Optional[BattleAction]:
        """Heal if enough mana"""
        if not self.use_mana(GameConfig.HEAL_MANA_COST):
            return None
        
        actual_healing = self.heal(GameConfig.HEAL_AMOUNT)
        return BattleAction(
            action_type=ActionType.HEAL,
            actor_name=self.name,
            healing=actual_healing,
            mana_cost=GameConfig.HEAL_MANA_COST
        )
    
    def defend_action(self) -> BattleAction:
        """Set up defense"""
        self.defend()
        return BattleAction(
            action_type=ActionType.DEFEND,
            actor_name=self.name
        )


class Enemy(Character):
    """AI-controlled enemy"""
    
    def __init__(self, name: str):
        hp = random.randint(GameConfig.ENEMY_MIN_HP, GameConfig.ENEMY_MAX_HP)
        super().__init__(name=name, max_hp=hp)
    
    def choose_action(self) -> BattleAction:
        """Simple AI: just attack"""
        damage = random.randint(
            GameConfig.ATTACK_MIN_DAMAGE,
            GameConfig.ATTACK_MAX_DAMAGE
        )
        return BattleAction(
            action_type=ActionType.ATTACK,
            actor_name=self.name,
            damage=damage
        )


# ============================================================================
# GAME ENGINE - Orchestrates battles
# ============================================================================
class Battle:
    """Manages a single battle between player and enemy"""
    
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.turn_count = 0
    
    def execute_turn(self, player_action: BattleAction) -> tuple[BattleAction, bool]:
        """
        Execute one turn of battle.
        Returns (enemy_action, battle_continues)
        """
        self.turn_count += 1
        
        # Player acts
        if player_action.damage > 0:
            actual_damage = self.enemy.take_damage(player_action.damage)
            player_action.damage = actual_damage  # Update with actual damage
        
        # Check if enemy defeated
        if not self.enemy.is_alive():
            return (player_action, False)
        
        # Enemy acts
        enemy_action = self.enemy.choose_action()
        if enemy_action.damage > 0:
            actual_damage = self.player.take_damage(enemy_action.damage)
            enemy_action.damage = actual_damage
        
        # Check if player defeated
        if not self.player.is_alive():
            return (enemy_action, False)
        
        return (enemy_action, True)
    
    def get_winner(self) -> Optional[Character]:
        """Return winner or None if battle ongoing"""
        if not self.enemy.is_alive():
            return self.player
        if not self.player.is_alive():
            return self.enemy
        return None


# ============================================================================
# USER INTERFACE - Separated from game logic
# ============================================================================
class ConsoleUI:
    """Handles all console input/output"""
    
    @staticmethod
    def print_separator():
        print("=" * 60)
    
    @staticmethod
    def print_stats(player: Player, enemy: Enemy):
        ConsoleUI.print_separator()
        print(player.get_stats())
        print(enemy.get_stats())
        ConsoleUI.print_separator()
    
    @staticmethod
    def print_action(action: BattleAction):
        print(action.describe())
    
    @staticmethod
    def get_player_name() -> str:
        """Get and validate player name"""
        while True:
            name = input("Enter your name: ").strip()
            if name:
                return name
            print("Name cannot be empty!")
    
    @staticmethod
    def get_player_action(player: Player) -> Optional[BattleAction]:
        """Get and validate player action choice"""
        print("\nChoose your action:")
        print("1. Attack")
        print(f"2. Cast Spell (costs {GameConfig.SPELL_MANA_COST} mana)")
        print(f"3. Heal (costs {GameConfig.HEAL_MANA_COST} mana)")
        print("4. Defend")
        
        while True:
            choice = input("Enter choice (1-4): ").strip()
            
            if choice == "1":
                return player.attack()
            elif choice == "2":
                action = player.cast_spell()
                if action:
                    return action
                print("Not enough mana!")
            elif choice == "3":
                action = player.heal_self()
                if action:
                    return action
                print("Not enough mana!")
            elif choice == "4":
                return player.defend_action()
            else:
                print("Invalid choice! Enter 1-4.")
    
    @staticmethod
    def print_victory(winner: Character):
        ConsoleUI.print_separator()
        print(f"🎉 {winner.name} WINS! 🎉")
        ConsoleUI.print_separator()
    
    @staticmethod
    def ask_play_again() -> bool:
        """Ask if player wants another battle"""
        while True:
            choice = input("\nPlay again? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            if choice in ['n', 'no']:
                return False
            print("Please enter 'y' or 'n'")


# ============================================================================
# GAME COORDINATOR - Main game loop
# ============================================================================
class Game:
    """Coordinates overall game flow"""
    
    def __init__(self):
        self.ui = ConsoleUI()
    
    def run(self):
        """Main game loop"""
        print("Welcome to Battle Game!")
        player_name = self.ui.get_player_name()
        
        while True:
            self.play_battle(player_name)
            
            if not self.ui.ask_play_again():
                print("Thanks for playing!")
                break
    
    def play_battle(self, player_name: str):
        """Play a single battle"""
        # Setup
        player = Player(player_name)
        enemy = Enemy("Goblin")
        battle = Battle(player, enemy)
        
        print(f"\n{player.name} encounters a {enemy.name}!")
        
        # Battle loop
        while True:
            self.ui.print_stats(player, enemy)
            
            # Get player action
            player_action = self.ui.get_player_action(player)
            if not player_action:
                continue
            
            # Execute turn
            self.ui.print_action(player_action)
            enemy_action, battle_continues = battle.execute_turn(player_action)
            
            if not battle_continues:
                break
            
            self.ui.print_action(enemy_action)
        
        # Battle ended
        winner = battle.get_winner()
        if winner:
            self.ui.print_victory(winner)


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    game = Game()
    game.run()
