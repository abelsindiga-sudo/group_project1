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
from project_two_functions import make_machine
from project_two_functions import animate_button
from project_two_functions import VendingMachine

def handle_click(x, y, screen, turt, vm, cart):
    """
        docstring
    """
    if -150 < x < -30 and 10 < y < 110:
        animate_button(turt, screen, -150, 10, -30, 110, "Snacks", vm)
        screen.update()

    elif 30 < x < 150 and 10 < y < 110:
        animate_button(turt, screen, 30, 10, 150, 110, "Candies", vm)
        screen.update()

    elif -150 < x < 150 and -120 < y < -20:
        animate_button(turt, screen, -150, -100, 150, -20, "Drinks", vm)
        screen.update()

    response = screen.textinput("SELECTION", "What would you like?\n Feel free to move the"
        " window to see, or type 'exit' to stop")
    while response != "exit":
        cart.append(response) # type: ignore
        response = screen.textinput("SELECTION", "What would you like?\n Feel free to move the"
                                    " window to see, or type 'exit' to stop")

    screen.clear()
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

# -------------------- MAIN --------------------

def main():
    """
        This is where the main bulk of our code will go.
    """
    turt: Turtle = Turtle()

    cart: list[str] = []

    screen = turtle.Screen()

    vm: VendingMachine = VendingMachine()

    # Creating the stock of the machine.
    drinks: list[str] = ["Diet Pepsi", "Pepsi", "Water", "Gatorade"]
    vm.add_item(drinks[0], 3, "drinks")
    vm.add_item(drinks[1], 3, "drinks")
    vm.add_item(drinks[2], 3, "drinks")
    vm.add_item(drinks[3], 3, "drinks")

    vm.add_item("Doritos", 2, "snacks")
    vm.add_item("Apples", 2, "snacks")
    vm.add_item("Granola Bar", 2, "snacks")
    vm.add_item("Trail Mix", 2, "snacks")

    vm.add_item("M&Ms", 1, "candies")
    vm.add_item("Hershey's", 1, "candies")
    vm.add_item("Snickers", 1, "candies")
    vm.add_item("Nerds", 1, "candies")

    make_machine(vm)
    screen.update()
    x: int = 0
    y: int = 0
    screen.onclick(handle_click(x, y, screen, turt, vm, cart)) # type: ignore

    done()


if __name__ == "__main__":
    main()
