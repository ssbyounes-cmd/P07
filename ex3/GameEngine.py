from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Any, Optional


class MockTarget:
    def __init__(self, name: str):
        self.name = name


class GameEngine:
    def __init__(self):
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.turns_simulated: int = 0
        self.total_damage: int = 0
        self.cards_created: int = 0

    # Fixed signature: -> None
    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if not self.factory or not self.strategy:
            return {}

        # 1. Engine uses the factory to build the hand
        card1 = self.factory.create_creature("dragon")
        card2 = self.factory.create_creature("goblin")
        card3 = self.factory.create_spell("lightning")

        hand = [card1, card2, card3]
        self.cards_created += len(hand)

        battlefield = [MockTarget("Enemy Player")]

        # 2. Engine passes the hand to the strategy
        actions: dict[str, Any] = self.strategy.execute_turn(hand, battlefield)

        # 3. Engine updates its internal trackers
        self.turns_simulated += 1
        self.total_damage += actions.get("damage_dealt", 0)

        # We return both the hand (so main can print it) and the actions
        return {
            "hand": hand,
            "actions": actions
        }

    def get_engine_status(self) -> dict:
        strategy_name = (self.strategy.get_strategy_name()
                         if self.strategy else "None")
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created
        }
