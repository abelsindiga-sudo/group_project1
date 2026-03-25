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