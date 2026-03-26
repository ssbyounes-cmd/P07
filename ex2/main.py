from ex2.EliteCard import EliteCard
from ex0.Card import Rarity


class MockTarget:
    def __init__(self, name: str):
        self.name = name


game_state = {
    "mana": 12,
    "turn": 1,
    "player_health": 20,
    "opponent_health": 20
}

Elite_Card = {
    "name": "Arcane Warrior",
    "cost": 4,
    "rarity": Rarity.LEGENDARY.value,
    "attack_power": 5,
    "health": 5,
    "defense": 3,
    "available_mana": game_state["mana"]
}

# target_card = {
#     "name": "Enemy Soldier",
#     "cost": 2,
#     "rarity": Rarity.COMMON.value,
#     "attack_power": 2,
#     "health": 3,
#     "defense": 1,
#     "available_mana": 5
# }

# target_card2 = {
#     "name": "Enemy Archer",
#     "cost": 3,
#     "rarity": Rarity.RARE.value,
#     "attack_power": 3,
#     "health": 2,
#     "defense": 1,
#     "available_mana": 5
# }


if __name__ == "__main__":
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print(f"- Card: {['play', 'get_card_info', 'is_playable']}")
    print(f"- Combatable: {['attack', 'defend', 'get_combat_stats']}")
    print(f"- Magical: {['cast_spell', 'channel_mana', 'get_magic_stats']}")

    Ecard = EliteCard(**Elite_Card)
    print(f"\nPlaying {Ecard.name} (Elite Card):")
    play_result = Ecard.play(game_state)

    if "card_not_played" not in play_result:
        print("\nCombat phase:")
        target = MockTarget('Enemy')

        print(f"Attack result: {Ecard.attack(target)}")
        print(f"Defense result: {Ecard.defend(incoming_damage=5)}")

        print("\nMagic phase:")
        target1 = MockTarget('Enemy1')
        target2 = MockTarget('Enemy2')
        print(
            f"Spell cast: {Ecard.cast_spell(spell_name='Fireball', targets=[target1, target2])}")
        print(f"Mana channel: {Ecard.channel_mana(amount=3)}")
    else:
        print(f"Failed to play card: {play_result['reason']}")

    print("\nMultiple interface implementation successful!")
