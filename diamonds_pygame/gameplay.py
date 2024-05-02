
from strategy import Player, AIPlayer, AIPlayer2
import random

class DiamondsGame:
    def __init__(self, num_players):
        self.players = []
        self.banker = None
        self.num_players = num_players
        self.setup_game()

    def setup_game(self):
        suits = ["Hearts", "Clubs", "Spades"]
        self.banker = Banker(self.create_deck())
        remaining_suits = suits.copy()

        for i in range(self.num_players):
            player_suit = random.choice(remaining_suits)
            remaining_suits.remove(player_suit)

            if i == self.num_players - 1:
                aggressiveness = float(input("Enter aggressiveness level for AI player (0 - cautious, 1 - aggressive): "))
                player = AIPlayer(f"AI Player", aggressiveness)
            elif i == self.num_players - 2:
                player = AIPlayer2(f"AI Player2")
            else:
                player = Player(f"Player {i+1}")
            player.suit = player_suit
            self.players.append(player)

        for player in self.players:
            for rank in range(2, 15):
                player.hand.append(Card(player.suit, rank))

    def create_deck(self):
        deck = []
        for suit in ["Diamonds", "Hearts", "Clubs", "Spades"]:
            for rank in range(2, 15):
                deck.append(Card(suit, rank))
        random.shuffle(deck)
        return deck

    def play(self):
        while True:
            diamond = self.banker.draw_diamond()
            if diamond is None:
                break
            self.play_round(diamond)

        self.display_scores()

    def play_round(self, diamond):
        print(f"\nAuctioning Diamond: {diamond.point_value}")

        bids = [player.make_bid(self, diamond) for player in self.players]
        winners = self.get_winners(bids, diamond)
        self.update_scores(winners, diamond)

    def get_winners(self, bids, diamond):
        highest_bid = max(bid.rank for bid in bids if bid is not None)
        return [i for i, bid in enumerate(bids) if bid and bid.rank == highest_bid and bid.rank >= diamond.rank]

    def update_scores(self, winners, diamond):
        for winner_index in winners:
            winner = self.players[winner_index]
            winner.score += diamond.point_value
            print(f"{winner.name} wins the round with {winner.bid.rank} and gets {diamond.point_value} points!")

    def display_scores(self):
        print("\nGame Over! Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score}")
        winner = max(self.players, key=lambda p: p.score)
        print(f"\nWinner: {winner.name}")

if __name__ == "__main__":
    game = DiamondsGame(3)  # Change to 3 for 3 players
    game.play()