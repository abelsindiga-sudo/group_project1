"""
Emma, Dot, Abel
CSCI 1101-11
Prof R

Project #2 - vending machine v02
Functions, Try/Except, Dictionaries
"""

from random import randint #random integer for the customer's money amount
from Venting_Def_plusultra import show_vending_options, handle_selection

# Dictionaries for items
drinks = {
    1: ("Diet Pepsi", 3),
    2: ("Pepsi", 3),
    3: ("Water", 3),
    4: ("Gatorade", 3)
}

snacks = {
    1: ("Doritos", 2),
    2: ("Apples", 2),
    3: ("Granola Bar", 2),
    4: ("Trail Mix", 2)
}

candies = {
    1: ("M&Ms", 1),
    2: ("Hershey's", 1),
    3: ("Snickers", 1),
    4: ("Nerds", 1)
}


def main():
    """Main function to run vending machine."""
    money: int = randint(1, 10)
    cart: list = []

    name: str = input("Welcome to the Vending Machine!\nPlease state your name: ")
    print(f"\nHi {name}, you have ${money} to spend.")

    while money > 0:
        show_vending_options()
        response: str = input("Select an option: ")

        if response.lower() == "exit":
            break

        elif response == "1":
            money = handle_selection(drinks, money, "Drinks", cart)

        elif response == "2":
            money = handle_selection(snacks, money, "Snacks", cart)

        elif response == "3":
            money = handle_selection(candies, money, "Candy", cart)

        else:
            print("Invalid option.")

        print(f"You now have ${money} remaining.")

    # Receipt feature to show purchased items 
    print("\nItems you purchased:")
    if cart:
        for item in cart:
            print(f"- {item}")
    else:
        print("No items purchased.")

    print("Thank you for visiting the vending machine!")

if __name__ == "__main__":
    main()