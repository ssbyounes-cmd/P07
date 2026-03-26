from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable

# TournamentCard (Multiple Inheritance: Card + Combatable + Rankable)
class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack_power: int = 0, health: int = 0, defense: int = 0):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.defense = defense
        self.wins = 0
        self.losses = 0
        if self.rarity == Rarity.LEGENDARY:
            self.rating = 1200
        else:
            self.rating = 1150
    
    def play(self, game_state: dict) -> dict:
        if "mana" in game_state and self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            return {"card_played": self.name, "mana_used": self.cost, "effect": "Creature summoned to battlefield"}
        else:
            return {"card_not_played": self.name, "reason": "Not enough mana to play this card"}

    def attack(self, target: 'TournamentCard') -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_power,
            "combat_type": "melee"
        }
    
    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(incoming_damage, self.defense)
        damage_taken = incoming_damage - damage_blocked
        self.health = max(0, self.health - damage_taken)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "combat_type": "melee"
        }

    def calculate_rating(self) -> int:
        return self.rating

    def get_tournament_stats(self) -> dict:
        return {
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.rating
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        for win in range(wins):
            self.rating += 16  # Increase rating for each win

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        for loss in range(losses):
            self.rating -= 16  # Decrease rating for each loss

    def get_rank_info(self) -> dict:
        return {
            "name": self.name,
            "rating": self.rating
        }
