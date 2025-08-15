Secret Auction Program

This Python project simulates a silent auction where multiple participants can place their bids without knowing others' offers until the end.
The program stores each participant's name and bid, then determines the winner with the highest bid.

Features

Accepts multiple participants.

Records each participant’s name and bid.

Clears the screen between bids to keep bids hidden.

Determines and announces the highest bidder.

Simple, interactive, and beginner-friendly.

How It Works:

1.The program asks for the participant's name and bid amount.

2.It asks whether there are any more bidders:

    {If yes, the screen is cleared, and the next bidder enters their details.

    If no, the program calculates and announces the winner.}

3.The highest bid is determined by iterating through the bids stored in a dictionary.
Example-Output:
What is your name?: Alice
What is your bid?: $150
Are there any other bidders? Type Yes or No: yes

What is your name?: Bob
What is your bid?: $200
Are there any other bidders? Type Yes or No: no

The winner is Bob with the bid amount: $200
