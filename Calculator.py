print("Welcome to the calculator")
while True:
 option=input("Type A to Multiply,Type B to Divide,Type C to Add,Type D to Subtract and Q to exit, Caps only:")
 if option == 'Q':
   print("Thank you for playing the Game, hope you have a Great Day")
 break

 if option in ['A', 'B', 'C', 'D']:
    num1=int(input("First number: "))
    num2=int(input("Second Number: "))
    if option == 'A':
        print("Multiplication:",num1*num2)
    elif option == 'B':
        if num2 == 0 :
            print("Error: Number cant be divided by 0")
        else:
            print("Division:",num1/num2)
    elif option == 'C':
        print("Addition:",num1+num2)
    elif option == 'D':
        print("Subtraction:",num1-num2)
 else:
     print("Invalid option selected.Please read the instructions carefully")
