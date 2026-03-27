from ex0.CreatureCard import CreatureCard
from ex0.main import card_one
from ex0.Card import Rarity
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from typing import Any


Spell: dict[str, Any] = {
    "name": "Lightning Bolt",
    "cost": 3,
    "rarity": Rarity.RARE,
    "effect_type": "Deal 3 damage to target"
}
Artifact: dict[str, Any] = {
    "name": "Mana Crystal",
    "cost": 2,
    "rarity": Rarity.COMMON,
    "durability": 5,
    "effect": "Permanent: +1 mana per turn"
}
game_state: dict[str, Any] = {
    "mana": 10,
    "turn": 1,
    "player_health": 20,
    "opponent_health": 20
}


if __name__ == "__main__":
    print("=== DataDeck Deck Builder ===\n")

    # Building a deck with different card types
    deck = Deck()
    deck.add_card(SpellCard(**Spell))
    deck.add_card(ArtifactCard(**Artifact))
    deck.add_card(CreatureCard(**card_one))
    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")

    # Drawing and playing cards from the deck
    print("\nDrawing and playing cards:")
    while deck.deck_list:
        drawn_card = deck.draw_card()
        card_info = drawn_card.get_card_info()
        print(f"\nDrew: {drawn_card.name} ({card_info.get('type')})")
        print(f"Play result: {drawn_card.play(game_state)}")

    print("\nPolymorphism in action: Same interface,"
          " different card behaviors!")
