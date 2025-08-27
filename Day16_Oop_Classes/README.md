Quiz Game (OOP in Python)

This is a simple Quiz Game built in Python using Object-Oriented Programming (OOP) principles.
The project demonstrates the use of classes, objects, and modular code design while providing an interactive command-line quiz experience.

🎯 Features

Loads questions and answers from a separate data.py file.

Uses a Question class to create question objects.

The QuizBrain class controls the quiz flow.

Tracks the player’s score and progress.

Ends when all questions are completed and shows the final score.

🛠 Project Structure
quiz-game/
│── data.py              # Contains question data (list of dicts)
│── question_model.py    # Defines the Question class
│── quiz_brain.py        # Handles the quiz logic
│── main.py              # Runs the game
│── README.md            # Documentation