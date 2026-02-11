"""
Emma, Dot, Abel
CSCI 1101-11
Prof R

Project #1 - vending machine

"""
from random import randint

money: int = randint(0, 50)

name: str = input("Welcome to the Vending Machine!\nPlease state your name: ")

print(f"Hi {name}, you have ${money} to spend.")

print("Your options from the vending machine come from three categories!")
print("Enter '1' for Drinks,")
print("Enter '2' for Snacks,")
print("Enter '3' for Candy.")
response: str = input()

if response == "1":
    print("Here are your Drinks options:")
elif response == "2":
    print("Here are your Snacks options:")
elif response == "3":
    print("Here are your Candy options:")
else:
    print("Please choose one of the options.")
response: str = input()
