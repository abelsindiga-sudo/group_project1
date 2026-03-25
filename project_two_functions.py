"""
project_two_functions.py

Emma, Dot, Abel
CSCI 1101-12
Prof R

Project #2 - vending machine v02
    Functions page for calling in the main file
"""

def show_vending_options() -> None:
    """
    Displays main vending categories.
        Drinks, Snacks, Candy
    """
    print("\nYour options from the vending machine:")
    print("Enter '1' for Drinks")
    print("Enter '2' for Snacks")
    print("Enter '3' for Candy")
    print("Type 'exit' to leave")

def handle_selection(items: dict, dollar: int, category: str, cart: list) -> int:
    """
    Handles item selection, validates input, and updates money.

    Parameters
    ----------
        items: dict
            dictionary of items available for purchase
        dollar: int
            current money user has to buy with
        category: str
            category name that the user wishes to purchase from
        cart: list[str]
            purchased items displayed in user's cart at the end

    Returns
    -------
        dollar: int
            Updated money for user to make purchases with ("dollar - price")
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
