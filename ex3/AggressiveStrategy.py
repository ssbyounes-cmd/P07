from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from typing import Any


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        # Simple logic: Put "Enemy Player" at the front if they exist
        prioritized = [target for target in available_targets
                       if target.name == "Enemy Player"]
        non_prioritized = [target for target in available_targets
                           if target.name != "Enemy Player"]
        return prioritized + non_prioritized

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # Standard helper function
        def get_card_cost(card):
            return card.cost

        # Rule: Plays low-cost creatures first
        creatures = list()
        others = list()
        for card in hand:
            if isinstance(card, CreatureCard):
                creatures.append(card)
            else:
                others.append(card)

        sorted_creatures = sorted(creatures, key=get_card_cost)
        sorted_others = sorted(others, key=get_card_cost)
        sorted_cards = sorted_creatures + sorted_others

        cards_played = []
        mana_used = 0
        game_dict: dict[str, Any] = {"mana": 5}
        damage_dealt = 0

        # Rule: Targets enemy creatures and player directly
        targets = self.prioritize_targets(battlefield)
        primary_target = targets[0].name if targets else "No Target"

        # Play what we can afford
        for card in sorted_cards:
            result: dict[str, Any] = card.play(game_dict)
            if "card_played" in result:
                cards_played.append(card.name)
                mana_used += card.cost
                if isinstance(card, CreatureCard):
                    damage_dealt += card.attack
                elif isinstance(card, SpellCard):
                    damage_dealt += 3
                else:
                    continue

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [primary_target],
            "damage_dealt": damage_dealt
        }
