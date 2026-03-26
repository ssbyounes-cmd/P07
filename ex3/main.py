from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine

if __name__ == "__main__":
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    print("=== DataDeck Game Engine ===\n")
    print("Configuring Fantasy Card Game...")

    # Configure the engine!
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.__class__.__name__)
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")

    # Let the Engine do the work
    turn_data = engine.simulate_turn()

    # Format and print the hand
    hand_display = [f'{card.name} ({card.cost})' for card in turn_data["hand"]]
    hand_display_str = ", ".join(hand_display)
    print(f"Hand: [{hand_display_str}]")

    print("\nTurn execution:")
    print("Strategy:", strategy.get_strategy_name())
    print("Actions:", turn_data["actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("\nAbstract Factory + Strategy Pattern: Maximum flexibility"
          " achieved!")
