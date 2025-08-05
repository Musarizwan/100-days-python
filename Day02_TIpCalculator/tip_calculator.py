print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_calculator=tip/100*bill
total_bill=tip_calculator+bill
dividing=total_bill/people
rounding=round(dividing,2)
print(f"Each person should pay=${rounding}")
