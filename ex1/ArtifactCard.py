from ex0.Card import Card, Rarity
from typing import Any


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict[str, Any]) -> dict:
        if "mana" in game_state and self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            return {"card_played": self.name, "mana_used": self.cost, "effect": self.effect}
        else:
            return {"card_not_played": self.name, "reason": "Not enough mana to play this card"}

    def activate_ability(self) -> dict:
        return {
            "action": "artifact_activated",
            "artifact_name": self.name,
            "effect_triggered": self.effect,
            "current_durability": self.durability
        }

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result.update({"type": "Artifact", "durability": self.durability, "effect": self.effect})
        return result
