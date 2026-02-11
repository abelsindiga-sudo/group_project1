"""
Emma, Dot, Abel
CSCI 1101-11
Prof R

Project #1 - vending machine

"""
from random import randint #random integer for the customer's money amount

money: int = randint(1, 20)

name: str = input("Welcome to the Vending Machine!\nPlease state your name: ")

print(f"\nHi {name}, you have ${money} to spend.")

while money > 0:
    print("Your options from the vending machine come from three categories!")
    print("Enter '1' for Drinks,")                  #three options to start
    print("Enter '2' for Snacks,")
    print("Enter '3' for Candy.")
    print("You may also type \"exit\" when you are ready to leave.")
    response: str = input()

    if response.lower().startswith("exit"):         #overall exit option
        break
    if response == "1":
        print("Here are your Drinks options:")
        print("All drinks are $3")
        print("1) Diet Pepsi")                      #four more options
        print("2) Pepsi")
        print("3) Water")
        print("4) Gatorade")
        drink_choice: int = int(input())
        if money > 3:
            if drink_choice == 1:                   #choice 1
                print("Here's your Diet Pepsi!")
                money -= 3                          #deplete their money
                print(f"You now have ${money}.")
            elif drink_choice == 2:
                print("Here's your Pepsi!")
                money -= 3
                print(f"You now have ${money}.")
            elif drink_choice == 3:
                print("Here's your water!")
                money -= 3
                print(f"You now have ${money}.")
            elif drink_choice == 4:
                print("Here is your Gatorade!")
                money -= 3
                print(f"You now have ${money}.")
            elif "exit":                            # exit option
                break
            elif drink_choice < 4:                  # in case don't follow rules
                print("Please choose an option.")
        print("Please make another selection.\n")   #return to OG selections

    if response == "2":                             # copy paste for snacks
        print("Here are your Snacks options:")
        print("All snacks are $2")
        print("1) Doritos")
        print("2) Apples")
        print("3) Granola Bar")
        print("4) Trail Mix")
        snack_choice: int = int(input())
        if money > 2:
            if snack_choice == 1:
                print("Here are you Doritos!")
                money -= 2
                print(f"You now have ${money}.")
            elif snack_choice == 2:
                print("Here are your apple slices!")
                money -= 2
                print(f"You now have ${money}.")
            elif snack_choice == 3:
                print("Here's your granola bar!")
                money -= 2
                print(f"You now have ${money}.")
            elif snack_choice == 4:
                print("Here is your Trail Mix!")
                money -= 2
                print(f"You now have ${money}.")
            elif "exit":
                break
            elif snack_choice < 4:
                print("Please choose an option.")
        print("Please choose one of the options.\n")

    if response == "3":                                 #copy paste for candy
        print("Here are your Candy options:")
        print("All candies are $1")
        print("1) M&Ms")
        print("2) Hershey's")
        print("3) Snickers")
        print("4) Nerds")
        candy_choice: int = int(input())
        if money > 1:
            if candy_choice == 1:
                print("Here are your M&Ms!")
                money -= 1
                print(f"You now have ${money}.")
            elif candy_choice == 2:
                print("Here's your Hershey's!")
                money -= 1
                print(f"You now have ${money}.")
            elif candy_choice == 3:
                print("Here's your Snickers!")
                money -= 1
                print(f"You now have ${money}.")
            elif candy_choice == 4:
                print("Here's your Nerds!")
                money -= 1
                print(f"You now have ${money}.")
            elif "exit":
                break
            elif candy_choice < 4:
                print("Please choose an option.")
        print("Please choose one of the options.\n")

print("Thank you for visiting the vending machine!")       # final goodbye when done