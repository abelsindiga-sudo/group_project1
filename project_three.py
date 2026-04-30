"""
Emma, Dot, Abel
CSCI 1101-12
Prof R

Project #3 - vending machine v03
    Classes, files, turtle addition

    LINK TO TURTLE GRAPHICS INFO --> https://docs.python.org/3/library/turtle.html#module-turtle
"""

import turtle
from turtle import Turtle, done
from random import randint
from project_two_functions import redraw_screen
from project_two_functions import show_items_on_screen, animate_button
from project_two_functions import VendingMachine


def handle_selection(items: dict, dollar: int, cart: list, selection: str) -> int:
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

    while True:
        try:

            if selection in items:
                name, price = items[selection]

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

# -------------------- MAIN --------------------

def main():
    """
        This is where the main bulk of our code will go.
    """
    turt: Turtle = Turtle()

    money: int = randint(1, 10)

    screen = turtle.Screen()

    redraw_screen(turt, screen, money)

    vm: VendingMachine = VendingMachine()

    # Creating the stock of the machine.
    vm.add_item("Diet Pepsi", 3, "drinks")
    vm.add_item("Pepsi", 3, "drinks")
    vm.add_item("Water", 3, "drinks")
    vm.add_item("Gatorade", 3, "drinks")

    vm.add_item("Doritos", 2, "snacks")
    vm.add_item("Apples", 2, "snacks")
    vm.add_item("Granola Bar", 2, "snacks")
    vm.add_item("Trail Mix", 2, "snacks")

    vm.add_item("M&Ms", 1, "candies")
    vm.add_item("Hershey's", 1, "candies")
    vm.add_item("Snickers", 1, "candies")
    vm.add_item("Nerds", 1, "candies")

    # CLICK SYSTEM (replaces while loop)
    def handle_click(x, y):
        """
            docstring
        """
        if -150 < x < -30 and 10 < y < 110:
            animate_button(turt, screen, -150, 10, -30, 110, "Snacks")
            show_items_on_screen(turt, vm.snacks, "Snacks")
            screen.update()
            response = screen.textinput("SELECTION", "What would you like?")
            money = handle_selection(vm.snacks, money, screen, response) # type: ignore

        elif 30 < x < 150 and 10 < y < 110:
            animate_button(turt, screen, 30, 10, 150, 110, "Candies")
            show_items_on_screen(turt, vm.candies, "Candies")
            screen.update()
            response = screen.textinput("SELECTION", "What would you like?")
            money = handle_selection(vm.candies, money, screen, response) # type: ignore

        elif -150 < x < 150 and -120 < y < -20:
            animate_button(turt, screen, -150, -100, 150, -20, "Drinks")
            show_items_on_screen(turt, vm.drinks, "Drinks")
            screen.update()
            response = screen.textinput("SELECTION", "What would you like?")
            money = handle_selection(vm.drinks, money, screen, response) # type: ignore

        elif -150 < x < 150 and -175 < y < -125:
            animate_button(turt, screen, -150, -125, 150, -175, "Return")

        redraw_screen(turt, screen, money)

        if money <= 0:
            turt.clear()
            turt.goto(0, 100)
            turt.write("Thank you!", align="center", font=("Verdana", 14, "bold"))

            turt.goto(0, 50)
            turt.write("Items Purchased:", align="center", font=("Verdana", 12, "bold"))

            y_pos = 20
            for item in cart:
                turt.goto(0, y_pos)
                turt.write(item, align="center", font=("Verdana", 10, "normal"))
                y_pos -= 20

            screen.update()

    screen.onclick(handle_click)

    done()


if __name__ == "__main__":
    main()
