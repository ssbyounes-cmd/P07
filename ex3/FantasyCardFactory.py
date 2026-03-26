from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        # The Registry: Maps keywords to card blueprints (stats)
        # This makes the factory 'Extensible' without changing method logic
        self._creature_registry = {
            "dragon": ("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5),
            "goblin": ("Goblin Warrior", 2, Rarity.COMMON, 5, 1)
        }
        self._spell_registry = {
            "fireball": ("Fireball", 4, Rarity.RARE, "Deal 4 damage to target"),
            "lightning": ("Lightning Bolt", 3, Rarity.COMMON, "Deal 3 damage to target")
        }
        self._artifact_registry = {
            "mana_ring": ("Mana Ring", 2, Rarity.RARE, 5, "Permanent: +1 mana per turn"),
            "crystal": ("Mana Crystal", 2, Rarity.COMMON, 3, "Permanent: +1 mana per turn")
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        # 1. String Lookup using the Registry
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            for key, stats in self._creature_registry.items():
                if key in name_lower:
                    # Unpacking the tuple into the constructor
                    return CreatureCard(*stats)
            return CreatureCard(name_or_power.title(), 3, Rarity.COMMON, 3, 3)

        # 2. Procedural Tier System (Power Level)
        elif isinstance(name_or_power, int):
            power = name_or_power
            monster_names = ["Orc Grunt", "Cave Spider", "Troll Bruiser", "Dire Wolf"]
            name = random.choice(monster_names)

            if power <= 10:
                attack, health, cost = random.randint(1, 5), random.randint(1, 5), random.randint(1, 3)
            elif power <= 20:
                attack, health, cost = random.randint(5, 10), random.randint(5, 10), random.randint(4, 6)
            else:
                attack, health, cost = random.randint(10, 20), random.randint(10, 20), random.randint(7, 10)

            return CreatureCard(name, cost, Rarity.RARE, attack, health)

        return CreatureCard("Generic Minion", 1, Rarity.COMMON, 1, 1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            for key, stats in self._spell_registry.items():
                if key in name_lower:
                    return SpellCard(*stats)
            return SpellCard(name_or_power.title(), 2, Rarity.COMMON, "Generic magic effect")

        elif isinstance(name_or_power, int):
            power = name_or_power
            if power <= 10:
                return SpellCard("Minor Spark", 1, Rarity.COMMON, f"Deal {power} damage")
            return SpellCard("Arcane Blast", 5, Rarity.EPIC, f"Deal {power} massive damage")

        return SpellCard("Minor Spark", 1, Rarity.COMMON, "Deal 1 damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            for key, stats in self._artifact_registry.items():
                if key in name_lower:
                    return ArtifactCard(*stats)
            return ArtifactCard(name_or_power.title(), 3, Rarity.COMMON, 4, "Generic aura")

        elif isinstance(name_or_power, int):
            power = name_or_power
            return ArtifactCard("Staff of Power", 5, Rarity.LEGENDARY, 5, f"Passive: +{power // 2} stats")

        return ArtifactCard("Rusty Shield", 1, Rarity.COMMON, 2, "Block 1 damage")

    def create_themed_deck(self, size: int) -> dict:
        deck_cards = []

        for _ in range(size):
            # 1. Randomly pick which type of card to create
            choice = random.choice(["creature", "spell", "artifact"])

            # 2. Generate a random power level between 1 and 30 for your tier system
            random_power = random.randint(1, 30)

            # 3. Pass the integer to trigger your procedural generation!
            if choice == "creature":
                deck_cards.append(self.create_creature(random_power))
            elif choice == "spell":
                deck_cards.append(self.create_spell(random_power))
            else:
                deck_cards.append(self.create_artifact(random_power))

        return {
            "theme": "Fantasy",
            "size": size,
            "cards": deck_cards
        }

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
