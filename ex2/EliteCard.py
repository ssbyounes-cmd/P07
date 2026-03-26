from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import Any


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: Rarity, attack_power: int,
                 health: int, defense: int, available_mana: int):
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.defense = defense
        self.available_mana = available_mana

    def play(self, game_state: dict[str, Any]) -> dict:
        if "mana" in game_state and self.is_playable(game_state["mana"]):
            game_state["mana"] -= self.cost
            self.available_mana -= self.cost
            return {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"
            }
        else:
            return {"card_not_played": self.name,
                    "reason": "Not enough mana to play this card"}

    def attack(self, target: Any) -> dict:
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

    def cast_spell(self, spell_name: str, targets: list[Any]) -> dict:
        mana_cost = 4
        if self.available_mana >= mana_cost:
            self.available_mana -= mana_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [target.name if hasattr(target, 'name') else
                            str(target) for target in targets],
                "mana_used": mana_cost
            }
        else:
            return {"spell_not_cast": spell_name,
                    "reason": "Not enough mana to cast this spell"}

    def channel_mana(self, amount: int) -> dict:
        self.available_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.available_mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "name": self.name,
            "mana": self.available_mana
        }
