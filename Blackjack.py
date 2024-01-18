import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = [str(i) for i in range(1, 14)]
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_total(self):
        total = 0
        num_aces = 0

        for card in self.hand:
            if card.rank.isdigit():
                total += int(card.rank)
            elif card.rank in ['Jack', 'Queen', 'King']:
                total += 10
            elif card.rank == 'Ace':
                total += 11
                num_aces += 1

        # Adjust total for Aces
        while total > 21 and num_aces:
            total -= 10
            num_aces -= 1

        return total

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()

    def deal_initial_cards(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal())

    def display_initial_cards(self):
        print(f"Player's cards: {', '.join(str(card) for card in self.player.hand)}")
        print(f"Dealer's cards: {str(self.dealer.hand[0])}, [Hidden]")

    def player_turn(self):
        while True:
            action = input("Do you want to 'Hit' or 'Stand'? ").lower()

            if action == 'hit':
                self.player.add_card(self.deck.deal())
                print(f"Player's cards: {', '.join(str(card) for card in self.player.hand)}")
                total = self.player.calculate_total()
                print(f"Total: {total}")

                if total > 21:
                    print("Bust! You lose.")
                    return 'bust'
            elif action == 'stand':
                break
            else:
                print("Invalid action. Please enter 'Hit' or 'Stand'.")

    def dealer_turn(self):
        while self.dealer.calculate_total() < 17:
            self.dealer.add_card(self.deck.deal())

    def determine_winner(self):
        player_total = self.player.calculate_total()
        dealer_total = self.dealer.calculate_total()

        print(f"Player's total: {player_total}")
        print(f"Dealer's total: {dealer_total}")

        if player_total > 21:
            return 'dealer'
        elif dealer_total > 21 or player_total > dealer_total:
            return 'player'
        elif dealer_total > player_total:
            return 'dealer'
        else:
            return 'tie'

    def play_game(self):
        print("Welcome to Python Blackjack!")
        self.deal_initial_cards()
        self.display_initial_cards()

        # Player's turn
        player_result = self.player_turn()
        if player_result == 'bust':
            return

        # Dealer's turn
        self.dealer_turn()

        # Determine winner
        winner = self.determine_winner()

        if winner == 'player':
            print("Congratulations! You win.")
        elif winner == 'dealer':
            print("Sorry, you lose. Better luck next time.")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.play_game()
