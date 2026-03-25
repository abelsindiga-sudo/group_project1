"""
Emma, Dot, Abel
CSCI 1101-11
Prof R

Project #2 - vending machine v02
Functions, Try/Except, Dictionaries
"""

from random import randint #random integer for the customer's money amount

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

def show_vending_options() -> None:
    """Displays main vending categories."""
    print("\nYour options from the vending machine:")
    print("Enter '1' for Drinks")
    print("Enter '2' for Snacks")
    print("Enter '3' for Candy")
    print("Type 'exit' to leave")

def handle_selection(items: dict, dollar: int, category: str, cart: list) -> int:
    """
    Handles item selection, validates input, and updates money.

    Parameters:
        items (dict): dictionary of items
        dollar (int): current money
        category (str): category name
        cart (list): purchased items

    Returns:
        int: updated money
    """
    print(f"\nHere are your {category} options:")

    for key, (name, price) in items.items():
        print(f"{key}) {name} - ${price}")

    while True:
        try:
            choice = int(input("Choose an option: "))

            if choice in items:
                name, price = items[choice]

                if dollar < price:
                    print("Not enough money.")
                    return dollar

                print(f"Here's your {name}!")
                cart.append(name)
                return dollar - price
            else:
                print("Invalid choice. Choose 1-4.")
        except ValueError:
            print("Please enter a valid number.")

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