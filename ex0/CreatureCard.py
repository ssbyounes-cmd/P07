from ex0.Card import Card
from ex0.Card import Rarity
from typing import Any


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack <= 0 or health <= 0:
            raise ValueError(
                "Attack and health values must be positive integers.")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict[str, Any]) -> dict:
        if "mana" in game_state and self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            return {"card_played": self.name, "mana_used": self.cost, "effect": "Creature summoned to battlefield"}
        else:
            return {"card_not_played": self.name, "reason": "Not enough mana to play this card"}

    def attack_target(self, target) -> dict:
        return {"attacker": self.name, "target": target.name, "damage_dealt": self.attack, "combat_resolved": True}

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result.update(
            {"type": "Creature", "attack": self.attack, "health": self.health})
        return result
