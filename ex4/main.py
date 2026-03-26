from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform
from ex0.Card import Rarity

if __name__ == "__main__":
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")
    FireDragon = TournamentCard("Fire Dragon", 5, Rarity.LEGENDARY, attack_power=8, health=10, defense=3)
    IceWizard = TournamentCard("Ice Wizard", 4, Rarity.RARE, attack_power=5, health=6, defense=2)
    Platform = TournamentPlatform()
    card1_id = Platform.register_card(FireDragon)
    card2_id = Platform.register_card(IceWizard)
    print(f"{FireDragon.name} (ID: {card1_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {FireDragon.rating}")
    print(f"- Record: {FireDragon.wins}-{FireDragon.losses}\n")

    print(f"{IceWizard.name} (ID: {card2_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {IceWizard.rating}")
    print(f"- Record: {IceWizard.wins}-{IceWizard.losses}\n")

    print("Creating tournament match...")
    print(f"Match result: {Platform.create_match(card1_id, card2_id)}\n")

    print("Tournament Leaderboard:")
    for card in Platform.get_leaderboard():
        print(card)

    print("\nPlatform Report:")
    print(Platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
