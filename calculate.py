#Author: GMelyanovskiy

print("Enter the zero (0), for exit.")
while True:
    userInput = input("Char (+,-,*,/): ")
    if userInput == '0': break
    if userInput in ('+','-','*','/'):
        x = float(input("First number: "))
        y = float(input("Second number: "))
        if userInput == '+':
            print("%.2f" % (x+y))
        elif userInput == '-':
            print("%.2f" % (x-y))
        elif userInput == '*':
            print("%.2f" % (x*y))
        elif userInput == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Zero division!")
    else:
        print("Uncorrect char operation!")