rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to rock,paper,scissors game: ")
game=int(input("Type 0 for rock\n1 for paper\n2 for scissors :\n"))
if game==0:
    print("You Chose rock :\n"+ rock)
elif game==1:
    print("You chose paper :\n"+ paper)
elif game==2:
    print("You chose scissors :\n"+ scissors)
else:
    print("Game Over")
# Randomization
game_list=[0,1,2]
computer=random.choice(game_list)
if computer==0:
    print("Computer Chose rock :\n"+rock)
elif computer==1:
    print("Computer Chose paper :\n"+ paper)
else:
    print("Computer Chose scissors: \n "+ scissors)
# Game Logic
if game==computer:
    print("Game draw")
elif game==0 and computer==1:
        print("Computer won")
elif game==1 and computer==2:
        print("Computer Won")
elif game==2 and computer==0:
        print("Computer won")
else:
        print("Player Won")