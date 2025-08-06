print("Welcome to rollar coaster ride")
height=int(input("What is your height?"))
bill=0
if height>120:
    print("You can ride the rollar coaster")
    age=int(input("What is your age:"))
    if age<12:
        print("Your Ticket is $5")
        bill=5
    elif age>=18:
        print("Your Ticket is $12")
        bill=12
    else:
        print("Your Ticket is $7")
        bill=7
    photo=input("DO you want to photos?$3 will be added to your bill, if yes reply with Y ,if NO reply with N: ")
    if photo=="Y":
        bill+=3
        print(f"your total bill is ${bill}")
    elif photo=="N":
        print(f"The total bill is ${bill}")
else:
    print("You aren't tall enough to ride")