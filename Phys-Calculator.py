import math as m
import random as r

#Variable initializations

Var_Needed = input("What are you solving for? ")
Vars_Obtained = input("What do you already have? ").split()
Values = {}

#Getting Variable Values

for var in Vars_Obtained:
    Values[var] = float(input(f"What is the value of {var}: ")) #Obtains the value of each variable that the user already has

if Var_Needed.lower() == "d" and "v1" in Values and "t" in Values:
    answ = Values["v1"] * Values["t"] + (0.5 * -9.8) * (Values["t"] * Values["t"])


print(f"{Var_Needed} is {answ}")