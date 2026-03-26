from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from typing import Any


card_one: dict[str, Any] = {
    "name": "Fire Dragon",
    "cost": 5,
    "rarity": Rarity.LEGENDARY.value,
    "attack": 7,
    "health": 5
}
card_two: dict[str, Any] = {
    "name": "Goblin Warrior",
    "cost": 5,
    "rarity": Rarity.COMMON.value,
    "attack": 4,
    "health": 10
}
game_state: dict[str, Any] = {
    "mana": 6,
    "turn": 1,
    "player_health": 20,
    "opponent_health": 20
}


def play_card(card: CreatureCard):
    mana = game_state.get("mana")
    result = card.play(game_state)
    if "card_not_played" not in result:
        print(f"\nPlaying {card.name} with {mana} mana available:")
        print("Playable: True")
        print(f"Play result: {result}")
    else:
        print("Playable: False")


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    card1 = CreatureCard(**card_one)
    print(card1.get_card_info())

    # Playing the card with sufficient mana
    play_card(card1)

    # Attacking another creature
    card2 = CreatureCard(**card_two)
    print(f"\n{card1.name} attacks {card2.name}:")
    print(f"Attack result: {card1.attack_target(card2)}")

    # Playing the card with insufficient mana
    game_state["mana"] = 3
    print("\nTesting insufficient mana (3 available):")
    play_card(card2)

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
