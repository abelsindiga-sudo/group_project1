"""
Emma, Dot, Abel
CSCI 1101-11
Prof R

Project #2 - vending machine v02
    Functions and Try/Except
"""
from random import randint  # random integer for the customer's money amount

def show_vending_options() -> None:
    """
        Will print the options for vending machine.

    """
    print("Your options from the vending machine come from three categories!")
    print("Enter '1' for Drinks,")
    print("Enter '2' for Snacks,")
    print("Enter '3' for Candy.")
    print("You may also type \"exit\" when you are ready to leave.")

def drink_choices() -> None:
    """
        Will print the options for drinks from vending machine.     
    """
    print("Here are your Drinks options:")
    print("All drinks are $3")
    print("1) Diet Pepsi")
    print("2) Pepsi")
    print("3) Water")
    print("4) Gatorade")
def drink_options(dollar: int) -> int:
    """
        And lets you choose which drinks you want.

        Parameters
        ----------
        dollar: int
            the amount of money a person has, depletes when purchasing

        Returns
        -------
        dollar: int
            the amount of money left over after purchasing
    """
    drink: int = int(input())
    drinks: list[str] = ["Diet Pepsi", "Pepsi", "water", "Gatorade"]

    try:
        if 0 < drink <= 4:
            print(f"Here's your {drinks[drink - 1]}!")
            dollar -= 3
    except ValueError:
        print("Please choose an option.")
    return dollar

def snack_choices() -> None:
    """
        Will print the options for snacks from vending machine. 
    """
    print("Here are your Snacks options:")
    print("All snacks are $2")
    print("1) Doritos")
    print("2) Apples")
    print("3) Granola Bar")
    print("4) Trail Mix")
def snack_options(dollar: int) -> int:
    """
        And lets you choose which snacks you want.

        Parameters
        ----------
        dollar: int
            the amount of money a person has, depletes when purchasing

        Returns
        -------
        dollar: int
            the amount of money left over after purchasing
    """
    snack: int = int(input())
    snacks: list[str] = ["Doritos", "Apples", "Granola Bar", "Trail Mix"]

    try:
        if 0 < snack <= 4:
            print(f"Here's your {snacks[snack - 1]}!")
            dollar -= 2
    except ValueError:
        print("Please choose an option.")
    return dollar

def candy_choices() -> None:
    """
        Will print the options for candies from vending machine. 
    """
    print("Here are your Candy options:")
    print("All candies are $1")
    print("1) M&Ms")
    print("2) Hershey's")
    print("3) Snickers")
    print("4) Nerds")
def candy_options(dollar: int) -> int:
    """
        And lets you choose which candies you want.

        Parameters
        ----------
        dollar: int
            the amount of money a person has, depletes when purchasing

        Returns
        -------
        dollar: int
            the amount of money left over after purchasing
    """
    candy: int = int(input())
    candies: list[str] = ["M&Ms", "Hershey's", "Snickers", "Nerds"]

    try:
        if 0 < candy <= 4:
            print(f"Here's your {candies[candy - 1]}!")
            dollar -= 1
    except ValueError:
        print("Please choose an option.")
    return dollar

def main():
    """
        Using a `main()` function hides any of your variables from the "global
        scope", allowing you to use the same names in multiple functions without
        Pylint and Pylance getting angry!
    """
    money: int = randint(1, 10)

    name: str = input("Welcome to the Vending Machine!\nPlease state your name: ")

    print(f"\nHi {name}, you have ${money} to spend.")

    try:
        if money <= 0:
            raise ValueError("You're money has run out!")

        show_vending_options()
        response: str = input()

        if response.lower().startswith("exit"):
            pass

        if response == "1":
            drink_choices()
            print(f"You now have ${drink_options(money)} remaining.")
            print("Please make another selection.\n")

        if response == "2":
            snack_choices()
            print(f"You now have ${snack_options(money)} remaining.")
            print("Please choose one of the options.\n")

        if response == "3":
            candy_choices()
            print(f"You now have ${candy_options(money)} remaining.")
            print("Please choose one of the options.\n")

    except ValueError:
        print("You're done.")

    print("Thank you for visiting the vending machine!")

if __name__ == "__main__":
    main()
