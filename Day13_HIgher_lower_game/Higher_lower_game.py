import random
from game_data import data

print("Welcome to the Higher-Lower Game!")

score = 0
game = True

# Pick 2 random accounts
account_a = random.choice(data)
account_b = random.choice(data)

while game:
    # Make sure A and B are not the same
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"\nCompare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
    print("VS")
    print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    # ------------------ check winner logic directly here -------------------
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    if choice == "a" and a_followers > b_followers:
        score += 1
        print(f"✅ Correct! Current score: {score}")
        account_a = account_b   # Winner moves on
        account_b = random.choice(data)

    elif choice == "b" and b_followers > a_followers:
        score += 1
        print(f"✅ Correct! Current score: {score}")
        account_a = account_b   # Winner moves on
        account_b = random.choice(data)

    else:
        print(f"❌ Wrong! Final score: {score}")
        game = False