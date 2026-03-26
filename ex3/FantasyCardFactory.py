from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Any
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            if "dragon" in name_lower:
                return CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY, 7, 5)
            elif "goblin" in name_lower:
                return CreatureCard("Goblin Warrior", 2, Rarity.COMMON, 5, 1)
            else:
                return CreatureCard(name_or_power.title(), 3, Rarity.COMMON, 3,
                                    3)

        elif isinstance(name_or_power, int):
            power = name_or_power
            monster_names = ["Orc Grunt", "Cave Spider",
                             "Troll Bruiser", "Dire Wolf", "Shadow Wraith"]
            name = random.choice(monster_names)

            # Tier shuffling logic
            if power <= 10:
                attack, health, cost = [
                    random.randint(1, 10) for _ in range(3)]
            elif power <= 20:
                attack, health, cost = [
                    random.randint(10, 20) for _ in range(3)]
            else:
                attack, health, cost = [
                    random.randint(20, 30) for _ in range(3)]

            return CreatureCard(name, cost, Rarity.RARE, attack, health)
        return CreatureCard("Generic Minion", 1, Rarity.COMMON, 1, 1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            if "fireball" in name_lower:
                return SpellCard("Fireball", 4, Rarity.RARE,
                                 "Deal 4 damage to target")
            elif "lightning" in name_lower:
                return SpellCard("Lightning Bolt", 3, Rarity.COMMON,
                                 "Deal 3 damage to target")
            else:
                return SpellCard(name_or_power.title(), 2, Rarity.COMMON,
                                 "Generic magic effect")

        elif isinstance(name_or_power, int):
            power = name_or_power
            spell_names = ["Frost Nova", "Chain Lightning",
                           "Arcane Blast", "Meteor Shower", "Healing Touch"]
            name = random.choice(spell_names)

            if power <= 10:
                cost = random.randint(1, 3)
                effect = f"Deal {power} damage"
            elif power <= 20:
                cost = random.randint(4, 6)
                effect = f"Deal {power} damage and freeze target"
            else:
                cost = random.randint(7, 10)
                effect = f"Deal {power} massive area damage"
            return SpellCard(name, cost, Rarity.EPIC, effect)

        return SpellCard("Minor Spark", 1, Rarity.COMMON, "Deal 1 damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:

        if isinstance(name_or_power, str):
            name_lower = name_or_power.lower()
            if "mana_ring" in name_lower or "mana ring" in name_lower:
                return ArtifactCard("Mana Ring", 2, Rarity.RARE, 5,
                                    "Permanent: +1 mana per turn")
            elif "crystal" in name_lower:
                return ArtifactCard("Mana Crystal", 2, Rarity.COMMON, 3,
                                    "Permanent: +1 mana per turn")
            else:
                return ArtifactCard(name_or_power.title(), 3, Rarity.COMMON, 4,
                                    "Generic aura")

        elif isinstance(name_or_power, int):
            power = name_or_power
            artifact_names = ["Staff of Power", "Amulet of Shielding",
                              "Tome of Secrets", "Cloak of Shadows",
                              "Chalice of Life"]
            name = random.choice(artifact_names)

            if power <= 10:
                cost, durability = random.randint(1, 3), random.randint(2, 4)
                effect = f"Passive: +{power // 2 + 1} to all stats"
            elif power <= 20:
                cost, durability = random.randint(4, 6), random.randint(3, 6)
                effect = f"Passive: +{power // 2} stats and draw a card"
            else:
                cost, durability = random.randint(7, 10), random.randint(5, 10)
                effect = f"Passive: +{power // 2} stats and immune to spells"

            return ArtifactCard(name, cost, Rarity.LEGENDARY,
                                durability, effect)
        return ArtifactCard("Rusty Shield", 1, Rarity.COMMON, 2,
                            "Block 1 damage")

    def create_themed_deck(self, size: int) -> dict[str, Any]:
        deck_cards = []

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])
            random_power = random.randint(1, 30)
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

    def get_supported_types(self) -> dict[str, list]:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
