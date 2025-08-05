print("Welcome to advanced tip calculator without loops")
print("This calculator is for 3 people only")
people=int(input("How many people are eating?"))
person_1=float(input("Enter the cost of 1st person: $"))
person_2=float(input("Enter the cost of 2nd person: $"))
person_3=float(input("Enter the cost of 3rd person: $"))
tip=int(input("Enter the tip amount: 5,10,15 :"))
adding_3person_bill=person_1+person_2+person_3
tip_calculation=tip/100*adding_3person_bill
total_bill=tip_calculation + adding_3person_bill
splitting_bill=total_bill/people
print(f"Each Should pay: ${round(splitting_bill,2)}")

