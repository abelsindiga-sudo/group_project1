"""
Emma, Dot, Abel
CSCI 1101-11
Prof R

Project #1 - vending machine

"""
from random import randint

money: int = randint(1, 20)

name: str = input("Welcome to the Vending Machine!\nPlease state your name: ")

print(f"Hi {name}, you have ${money} to spend.")

print("Your options from the vending machine come from three categories!")
print("Enter '1' for Drinks,")
print("Enter '2' for Snacks,")
print("Enter '3' for Candy.")
print("You may also type \"exit\" when you are ready to leave.")
response: str = input()

while money > 0:
    if response.lower().startswith("exit"):
        break
    if response == "1":
        print("Here are your Drinks options:")
        print("All drinks are $3")
        print("1) Diet Pepsi")
        print("2) Pepsi")
        print("3) Water")
        print("4) Gatorade")
        print("You may also type \"exit\" when you are ready to leave.")
        drink_choice = input()
        if drink_choice.lower().startswith("exit"):
            break
        if money >= 3 and drink_choice == 1:
            print("Here's your Diet Pepsi!")
            money -= 3
        elif money>= 3 and drink_choice == 2:
            print("Here's your Pepsi!")
            money -= 3
        elif money >= 3 and drink_choice == 3:
            print("Here's your water!")
            money -= 3
        elif money >= 3 and drink_choice == 4:
            print("Here is your Gatorade!")
            money -= 3
        else:
            print("You don't have enough funds.")
        print("Please make another selection.")

    if response == "2":
        print("Here are your Snacks options:")
        print("All snacks are $2")
        print("1) Doritos")
        print("2) Apples")
        print("3) Granola Bar")
        print("4) Trail Mix")
        print("You may also type \"exit\" when you are ready to leave.")
        snack_choice = input()
         if snack_choice.lower().startswith("exit"):
            break
        if money >= 2 and snack_choice == 1:
            print("Here are you Doritos!")
            money -= 2
        elif money>= 2 and snack_choice == 2:
            print("Here are your apple slices!")
            money -= 2
        elif money >= 2 and snack_choice == 3:
            print("Here's your granola bar!")
            money -= 2
        elif money >= 2 and snack_choice == 4:
            print("Here is your Trail Mix!")
            money -= 2
        else:
            print("You don't have enough funds.")
        print("Please choose one of the options.")

    if response == "3":
        print("Here are your Candy options:")
        print("All candies are $1")
        print("1) M&Ms")
        print("2) Hershey's")
        print("3) Snickers")
        print("4) Nerds")
        print("You may also type \"exit\" when you are ready to leave.")
        candy_choice = input()
        if candy_choice.lower().startswith("exit"):
            break
        if money >= 1 and candy_choice == 1:
            print("Here are you M&Ms!")
            money -= 1
        elif money>= 1 and candy_choice == 2:
            print("Here's your Hershey's!")
            money -= 1
        elif money >= 1 and candy_choice == 3:
            print("Here's your Snickers!")
            money -= 1
        elif money >= 1 and candy_choice == 4:
            print("Here's your Nerds!")
            money -= 1
        else:
            print("You don't have enough funds.")
        print("Please choose one of the options.")
print("Get out of here you brookey")
