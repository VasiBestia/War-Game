import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        print(f"Player {self.name} has {len(self.all_cards)} cards left.")


# Game Setup
player_one = Player("Jose")
player_two = Player("Karina")

new_deck = Deck()
new_deck.shuffle()

for card in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

round_number = 0
game_on = True
while game_on:
    round_number += 1
    print(f"Is round no.:{round_number}")
    if len(player_one.all_cards) == 0:
        print(
            f"Player {player_one.name} is out of cards! "
            f"Player {player_two.name} wins!"
        )
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print(
            f"Player {player_two.name} is out of cards! "
            f"Player {player_one.name} wins!"
        )
        game_on = False
        break

    player_one_card = player_one.remove_one()
    player_two_card = player_two.remove_one()

    print(f"{player_one.name} plays: {player_one_card}")
    print(f"{player_two.name} plays: {player_two_card}")

    table_cards = [player_one_card, player_two_card]

    # comparăm valorile
    if player_one_card.value > player_two_card.value:
        player_one.add_cards(table_cards)
        print(f"{player_one.name} wins the round.")

    elif player_two_card.value > player_one_card.value:
        player_two.add_cards(table_cards)
        print(f"{player_two.name} wins the round.")

    else:
        print("WAR!")

        at_war = True
        while at_war:
            if len(player_one.all_cards) < 5:
                print(f"{player_one.name} doesn't have enough cards for war.")
                print(f"{player_two.name} wins!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print(f"{player_two.name} doesn't have enough cards for war.")
                print(f"{player_one.name} wins!")
                game_on = False
                break

            else:
                # fiecare pune 5 cărți: 4 cu fața în jos, 1 cu fața în sus
                for _ in range(5):
                    table_cards.append(player_one.remove_one())
                    table_cards.append(player_two.remove_one())

                war_card_one = table_cards[-2]
                war_card_two = table_cards[-1]

                print(f"WAR cards: {war_card_one} vs {war_card_two}")

                if war_card_one.value > war_card_two.value:
                    player_one.add_cards(table_cards)
                    print(f"{player_one.name} wins the war!")
                    at_war = False

                elif war_card_two.value > war_card_one.value:
                    player_two.add_cards(table_cards)
                    print(f"{player_two.name} wins the war!")
                    at_war = False

                else:
                    print("Another tie! Continuing war...")
