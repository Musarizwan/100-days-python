Hangman Game 🎯
A simple Python implementation of the classic Hangman game.
The player must guess the hidden word letter by letter. Wrong guesses reduce lives, and when lives reach zero, the game ends.
📜 How to Play
1.The game randomly chooses a word from the word_list in hangman_words.py.

2.The player guesses one letter at a time.

3.If the guessed letter is correct, it is revealed in the word.

4.If the guess is wrong, the player loses a life.

5.The game ends when:

 <The player guesses all the letters (Win 🎉)>

 <Lives reach zero (Lose 💀)>
 Example Output: _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       
Word to guess: _ _ _ _ _ 
****************************6/6 LIVES LEFT****************************
Guess a letter: 


