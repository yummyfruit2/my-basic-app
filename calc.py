# Code from https://github.com/joodh999/basic-calculator

calculate = True 

while calculate:
    try:
        x = int(input("Enter your 1st number :"))
        y = int(input("Enter your 2nd number :"))
    except(ValueError):
        print("Not a Number!")
    
    else:
        o = input("enter your operator in words :")
   
        if o == "addition":
            a = x + y
            print(f"{x} + {y} = {a}")

        elif o == "subtraction":
            a = x - y  
            print(f"{x} - {y} = {a}")
            
        elif o == "division":
            a = x * y
            print(f"{x} / {y} = {a}")

        elif o == "multiplication":
            a = x * y  
            print(f"{x} * {y} = {a}")  
        else:
            print("wrong operator")
            print((("""
type addition for addition
type subtraction for subtraction
type multiplication for multiplication
type division for division
            """)))
        try_again = input("do you want to try again y/n : ")

        if try_again == "yes" or "y":
            calculate = True
        else:
            calculate = False
            
