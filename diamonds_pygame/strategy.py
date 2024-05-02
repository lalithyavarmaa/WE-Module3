from enum import Enum, auto
import random

class BiddingStrategy(Enum):
    AGGRESSIVE = auto()
    CONSERVATIVE = auto()
    BALANCED = auto()
    STRATEGIC_BLUFFING = auto()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0
        self.suit = None
        self.bid = None

    def make_bid(self, game, diamond, bidding_strategy):
        if bidding_strategy == BiddingStrategy.AGGRESSIVE:
            return self.aggressive_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.CONSERVATIVE:
            return self.conservative_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.BALANCED:
            return self.balanced_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.STRATEGIC_BLUFFING:
            return self.strategic_bluff_bid(game, diamond)
        else:
            raise ValueError("Invalid bidding strategy")

    def aggressive_bid(self, game, diamond):
        highest_card = max(card.rank for card in self.hand) if self.hand else 0
        if diamond.rank > highest_card:
            return None
        else:
            for card in sorted(self.hand, key=lambda c: c.rank, reverse=True):
                if card.rank >= diamond.rank:
                    self.bid = card
                    return card
            return random.choice(self.hand) if self.hand else None

    def conservative_bid(self, game, diamond):
        lowest_card = min(card.rank for card in self.hand) if self.hand else 0
        if diamond.rank < lowest_card:
            return None
        else:
            for card in sorted(self.hand, key=lambda c: c.rank):
                if card.rank <= diamond.rank:
                    self.bid = card
                    return card
            return random.choice(self.hand) if self.hand else None

    def balanced_bid(self, game, diamond):
        return random.choice(self.hand) if self.hand else None

    def strategic_bluff_bid(self, game, diamond):
        return random.choice(self.hand) if self.hand else None

class AIPlayer(Player):
    def __init__(self, name, aggressiveness):
        super()._init_(name)
        self.aggressiveness = aggressiveness

    def make_bid(self, game, diamond, bidding_strategy):
        if bidding_strategy == BiddingStrategy.AGGRESSIVE:
            return self.aggressive_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.CONSERVATIVE:
            return self.conservative_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.BALANCED:
            return self.balanced_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.STRATEGIC_BLUFFING:
            return self.strategic_bluff_bid(game, diamond)
        else:
            raise ValueError("Invalid bidding strategy")

    def aggressive_bid(self, game, diamond):
        highest_card = max(card.rank for card in self.hand) if self.hand else 0
        if self.aggressiveness > 0.5 and diamond.rank > highest_card:
            return None
        else:
            for card in sorted(self.hand, key=lambda c: c.rank, reverse=True):
                if card.rank >= diamond.rank:
                    self.bid = card
                    return card
            return random.choice(self.hand) if self.hand else None

    def conservative_bid(self, game, diamond):
        lowest_card = min(card.rank for card in self.hand) if self.hand else 0
        if self.aggressiveness < 0.5 and diamond.rank < lowest_card:
            return None
        else:
            for card in sorted(self.hand, key=lambda c: c.rank):
                if card.rank <= diamond.rank:
                    self.bid = card
                    return card
            return random.choice(self.hand) if self.hand else None

    def balanced_bid(self, game, diamond):
        return random.choice(self.hand) if self.hand else None

    def strategic_bluff_bid(self, game, diamond):
        return random.choice(self.hand) if self.hand else None

class AIPlayer2(Player):
    def make_bid(self, game, diamond, bidding_strategy):
        if bidding_strategy == BiddingStrategy.AGGRESSIVE:
            return self.aggressive_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.CONSERVATIVE:
            return self.conservative_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.BALANCED:
            return self.balanced_bid(game, diamond)
        elif bidding_strategy == BiddingStrategy.STRATEGIC_BLUFFING:
            return self.strategic_bluff_bid(game, diamond)
        else:
            raise ValueError("Invalid bidding strategy")

    def aggressive_bid(self, game, diamond):
        sorted_computer_deck = sorted(self.hand, key=lambda card: card.rank)
        for card in sorted_computer_deck:
            if card.rank >= diamond.rank:
                self.bid = card
                return card
        return sorted_computer_deck[0] if sorted_computer_deck else None

    def conservative_bid(self, game, diamond):
        sorted_computer_deck = sorted(self.hand, key=lambda card: card.rank, reverse=True)
        for card in sorted_computer_deck:
            if card.rank <= diamond.rank:
                self.bid = card
                return card
        return random.choice(self.hand) if self.hand else None

    def balanced_bid(self, game, diamond):
        return random.choice(self.hand) if self.hand else None

    def strategic_bluff_bid(self, game, diamond):
        return random.choice(self.hand) if self.hand else None