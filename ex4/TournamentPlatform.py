from ex4.TournamentCard import TournamentCard

# TournamentPlatform (Platform Management)
class TournamentPlatform:
    def __init__(self):
        self.registered_cards = {}
        self.match_history = []
        self._category_counters = {}
    
    def register_card(self, card: TournamentCard) -> str:
        prefix = card.name.split()[-1].lower()
        count = self._category_counters.get(prefix, 0) + 1 # Increment count for this category
        self._category_counters[prefix] = count
        card_id = f"{prefix}_{count:03d}" # 000 to 999 format
        self.registered_cards[card_id] = card
        return card_id


    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self.registered_cards or card2_id not in self.registered_cards:
            return {"error": "One or both cards not registered"}
        card1 = self.registered_cards[card1_id]
        card2 = self.registered_cards[card2_id]

        # Simulate match (winner will be the last one standing. loser will be the one with 0 health first)
        while card1.health > 0 and card2.health > 0:
            attack_result = card1.attack(card2)
            defense_result = card2.defend(attack_result["damage"])
            if not defense_result["still_alive"]:
                winner, loser = card1, card2
                break
            
            attack_result = card2.attack(card1)
            defense_result = card1.defend(attack_result["damage"])
            if not defense_result["still_alive"]:
                winner, loser = card2, card1
                break

        self.match_history.append({
            "card1": card1.name,
            "card2": card2.name,
            "winner": winner.name,
            "loser": loser.name
        })

        winner.update_wins(1)
        loser.update_losses(1)
        
        return {
            "winner": card1_id if winner == card1 else card2_id,
            "loser": card1_id if loser == card1 else card2_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        ratings = list()
        for card in self.registered_cards.values():
            ratings.append(card.rating)
        sorted_ratings = sorted(ratings, reverse=True)
        sorted_ratings = list(dict.fromkeys(sorted_ratings))

        card_rating = list()
        for rate in sorted_ratings:
            for card in self.registered_cards.values():
                if card.rating == rate:
                    card_rating.append(card)
        
        ratings_info = list()
        index = 1
        for card in card_rating:
            ratings_info.append(f"{index}. {card.name} - Rating: {card.rating} ({card.wins}-{card.losses})")
            index += 1
        return ratings_info

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.registered_cards)
        match_played = len(self.match_history)
        ratings_list = [card.rating for card in self.registered_cards.values()]
        avg_rating = int(sum(ratings_list) / len(ratings_list) if ratings_list else 0)

        return {
            "total_cards": total_cards,
            "matches_played": match_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
