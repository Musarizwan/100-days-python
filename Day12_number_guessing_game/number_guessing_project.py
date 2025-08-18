import random
def easy(random_number):
    attempts=10
    for i in range(1,11):

        guess=int(input("Make a Guess: "))
        if random_number==guess:
            print("You Guessed it right")
            return 0
        elif random_number>guess and random_number!=guess:

            attempts-=1
            if attempts==0:
                print("you have used all your attempts")
                print(f"The real answer was {random_number}")
            elif attempts>0:
                print("TOO low")
                print("guess again")
                print(f"you have left with {attempts} attempts")

        elif random_number<guess and random_number!=guess:
            attempts-=1
            if attempts==0:
                print("you have used all your attempts")
                print(f"The real answer was {random_number}")
            elif attempts>0:
                print("Too high")
                print("Guess again")
                print(f"you have left with {attempts} attempts")





def hard(random_number):
    attempts=5
    for i in range(1,6):

        guess = int(input("Make a Guess: "))
        if random_number == guess:
            print("You Guessed it right")
            return 0
        elif random_number > guess and random_number != guess:

            attempts -= 1
            if attempts == 0:
                print("you have used all your attempts")
                print(f"The real answer was {random_number}")
            elif attempts > 0:
                print("TOO low")
                print("guess again")
                print(f"you have left with {attempts} attempts")

        elif random_number < guess and random_number != guess:
            attempts -= 1
            if attempts == 0:
                print("you have used all your attempts")
                print(f"The real answer was {random_number}")
            elif attempts > 0:
                print("Too high")
                print("Guess again")
                print(f"you have left with {attempts} attempts")


print("Welcome to Number Guessing game!")
print("I am thinking of a number from 1-100.")
level=input("Choose Difficulty level: Easy or Hard: ").lower()
random_number=random.randint(1,101)
if level=="easy":
    print("You have 10 attempt left")
    easy(random_number)
elif level=="hard":
    print("you have 5 attempt left")
    hard(random_number)
else:
    print("Invalid")