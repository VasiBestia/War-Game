🃏 War Card Game in Python
Welcome to the War Card Game, a simple simulation of one of the most well-known classic card games, written entirely in Python.
Two players battle using a standard 52-card deck — the player who collects all the cards wins the war! ⚔️

📚 Table of Contents

📦 Features
🧠 How the Game Works
💻 Code Structure
🎮 Example Gameplay
❤️ Author
📃 License

📦 Features
✅ Complete 52-card deck (♠️ ♥️ ♣️ ♦️)
✅ Card shuffling before the game
✅ Turn-based card comparison
✅ Automatic "WAR" logic when cards tie
✅ Dynamic print statements for each round
✅ Ends automatically when one player runs out of cards
✅ Object-Oriented Programming design

🧠 How the Game Works
Here’s a detailed breakdown of the game logic:

🎴 Deck Creation
A standard 52-card deck is created using all suits (Hearts, Diamonds, Spades, Clubs) and all ranks from "Two" to "Ace".

Each card is an object with attributes: suit, rank, and value.

👥 Player Setup
The deck is shuffled and split evenly between two players.

Each player has their own list of cards.

🔁 Game Loop
On each round, both players remove the top card from their decks.

The cards are compared:

The player with the higher value wins both cards.

If the cards are equal in value, WAR begins.

⚔️ WAR Logic
During war:

Each player places 5 cards: 4 face-down, 1 face-up.

The last card is compared again.

The winner takes all 10 cards (or more, if war continues).

If a player does not have enough cards, they lose the game.

🏁 Game Over
The game ends when one player runs out of cards.

💻 Code Structure
war_game.py         # Main script that contains the full game logic
Classes:
├── Card            # Represents a single card (suit, rank, value)
├── Deck            # Contains all 52 cards, shuffles, and deals
└── Player          # Represents each player and their actions

🎮 Example Gameplay Output
Round 1
Jose plays: Queen of Hearts
Karina plays: Nine of Spades
Jose wins the round!

Round 2
Jose plays: Five of Diamonds
Karina plays: Five of Clubs
WAR!
...

Player Karina is out of cards!
Player Jose wins the game!
Each round shows:

The cards drawn

Who wins the round

WAR announcements

Final game winner

❤️ Author
Made with ❤️ by a Python enthusiast learning Object-Oriented Programming.

If you'd like to contribute or improve the project, feel free to fork it!

📃 License
This project is open-source and free to use under the MIT License.
Feel free to use, modify, and share it!

📌 Notes
Always access the .value attribute from a Card, not a list:

card.value         # ✅ correct
list_of_cards.value  # ❌ wrong
WAR logic can repeat recursively if there's another tie — make sure to handle that edge case!

This is a terminal-based simulation — no graphical interface (yet)
