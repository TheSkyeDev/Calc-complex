#Variable initializations

Opp_select = input("What operation would you like to preform (+, -, *, /): ")
Num1 = int(input("What is your first number: "))
Num2 = int(input("What is your second number: "))


# Actual code

if Opp_select == "+":
    Answ = Num1 + Num2
elif Opp_select == "-":
    Answ = Num1 - Num2
if Opp_select == "*":
    Answ = Num1 * Num2
if Opp_select == "/":
    Answ = Num1 / Num2    

print(f"The answer to this equation is {Answ}, Thanks!")