from abc import ABC, abstractmethod
from typing import Any
from enum import Enum


class Rarity(Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: Rarity):
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost,
                "rarity": self.rarity.value}

    def is_playable(self, available_mana: int) -> bool:
        return self.cost <= available_mana
