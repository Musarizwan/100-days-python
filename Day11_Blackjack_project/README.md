🃏 Blackjack Game (Python)

This is a Command-Line Blackjack Game built with Python.
You play against the computer dealer following standard Blackjack rules: try to get as close to 21 as possible without going over.

Features

Full Blackjack rules:

Aces can count as 11 or 1 depending on your score.

A hand with 21 on the first two cards is a Blackjack.

The computer dealer automatically draws cards until the score is 17 or higher.

Player can decide whether to draw another card (hit) or pass (stand).

Results are displayed at the end with clear win/lose/draw messages.

How the Game Works:

    The player and computer dealer are both dealt 2 cards.

    Player decides to:

        y → draw another card.

        n → stand with current hand.

    If the player goes over 21, they bust.

    The computer dealer then plays by Blackjack rules.

     The result is compared, and the winner is declared.

Example Gameplay:
Do you want to play a game of Blackjack? Type 'y' or 'n': y
   Your cards: [11, 10], current score: 21
   Computer's first card: 8
   Your final hand: [11, 10], final score: 21
   Computer's final hand: [8, 9, 4], final score: 21
Draw 🙃

Do you want to play a game of Blackjack? Type 'y' or 'n': y
   Your cards: [5, 10], current score: 15
   Computer's first card: 7
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [5, 10, 9], current score: 24
   Computer's first card: 7
   Your final hand: [5, 10, 9], final score: 24
   Computer's final hand: [7, 2], final score: 9
You went over. You lose 😭