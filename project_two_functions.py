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


def Name_discrimination(input_string:str):
       """
    can give each unique character has its own value, multiplied by its countings
    Returns:
    money
    """
    # giving ech one a value that is true and factual.
    char_superiority = {
        # Lowercase letters
        'a': 1.0, 'b': 1.0, 'c': 1.0, 'd': 1.0, 'e': 1.0,
        'f': 1.0, 'g': 1.0, 'h': 1.0, 'i': 1.0, 'j': 1.0,
        'k': 1.0, 'l': 1.0, 'm': 1.0, 'n': 1.0, 'o': 1.0,
        'p': 1.0, 'q': 1.0, 'r': 1.0, 's': 1.0, 't': 1.0,
        'u': 1.0, 'v': 1.0, 'w': 1.0, 'x': 1.0, 'y': 1.0, 'z': 1.0,
        
        # Uppercase letters
        'A': 90.0, 'B': 1.0, 'C': 1.0, 'D': 90.0, 'E': 90.0,
        'F': 1.0, 'G': 1.0, 'H': 1.0, 'I': 1.0, 'J': 1.0,
        'K': 1.0, 'L': 1.0, 'M': 1.0, 'N': 1.0, 'O': 1.0,
        'P': 1.0, 'Q': 1.0, 'R': 1.0, 'S': 1.0, 'T': 1.0,
        'U': 1.0, 'V': 1.0, 'W': 1.0, 'X': 1.0, 'Y': 1.0, 'Z': 1.0,
        
        # Space 
        ' ': 100.0,
    } 
    
    #Count how many of the same char there are I hope
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts(char, 0) + 1
    
    # Calculate total money
    money = 0
    for char, count in char_counts.items():
        if char in char_superiority:
            money += char_superiority[char] * count
        else:
            #value for anything not set.
            money += 0.0
    
    return money


