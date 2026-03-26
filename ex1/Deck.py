from ex0.Card import Card
from typing import Any
import random


class Deck():
    def __init__(self):
        self.deck_list: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.deck_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck_list:
            if card.name == card_name:
                self.deck_list.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck_list)

    def draw_card(self) -> Card:
        if not self.deck_list:
            raise IndexError("Cannot draw from an empty deck.")
        return self.deck_list.pop(0)

    def get_deck_stats(self) -> dict:
        res: dict[str, Any] = {
            "total_cards": len(self.deck_list),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }
        costs: list[int] = []
        for card in self.deck_list:
            card_info = card.get_card_info()
            card_type = card_info.get('type')
            if card_type == "Creature":
                res["creatures"] += 1
            elif card_type == "Spell":
                res["spells"] += 1
            elif card_type == "Artifact":
                res["artifacts"] += 1
            costs.append(card.cost)

        if costs:
            avg = sum(costs) / len(costs)
            res["avg_cost"] = round(float(avg), 1)

        return res
