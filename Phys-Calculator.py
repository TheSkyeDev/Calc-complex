import math as m
import random as r

#Variable initializations

Var_Needed = input("What are you solving for? ")
Vars_Obtained = input("What do you already have? ").split()
Values = {}

#Getting Variable Values

for var in Vars_Obtained:
    Values[var] = float(input(f"What is the value of {var}: ")) #Obtains the value of each variable that the user already has

print(Values)