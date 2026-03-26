from ex0.Card import Card, Rarity
from typing import Any


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict[str, Any]) -> dict:
        if "mana" in game_state and self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            return {"card_played": self.name, "mana_used": self.cost, "effect": self.effect_type}
        else:
            return {"card_not_played": self.name, "reason": "Not enough mana to play this card"}

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell_name": self.name,
            "effect_type": self.effect_type,
            "targets_affected": [target.name if hasattr(target, 'name') else str(target) for target in targets],
            "effect_resolved": True
        }

    def get_card_info(self) -> dict:
        result = super().get_card_info()
        result.update({"type": "Spell", "effect_type": self.effect_type})
        return result
