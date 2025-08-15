def highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder

    print(f"The winner is {winner} with the bid amount: ${highest_bid}")

continue_bidding=True
bid={}
while continue_bidding:
    name=input("what is your name?: ")
    price=int(input("What is your bid?: $"))
    bid[name]=price
    should_continue = input("are there any other bidders? Type Yes or No:").lower()
    if should_continue=="no":
        continue_bidding=False
        highest_bidder(bid)
    elif should_continue=="yes":
        print("\n"* 50)
        continue_bidding=True