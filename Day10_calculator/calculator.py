logo = r"""
 _____________________
|  _________________  |
| | MusaRizwan     . | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return(n1/n2)
operations={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}
print(logo)

def calculator():
    n1=int(input("Enter the first number :"))
    game_continue=True
    while game_continue:
        operators=input("Type the mathematical operator: \n * \n - \n + \n / \n")
        n2=int(input("Enter the Second number :"))
        result=operations[operators](n1,n2)
        print(f"The result is {result}")
        previous_result=input("Do you want to work with the previous result?: Type:Yes,\n if You want to reset the calculator type : No\n").lower()
        if previous_result=="yes":
            n1=result
            game_continue=True
        elif previous_result=="no":
            print("\n"*50)
            game_continue=False
            calculator()

calculator()