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
from random import randint # random integer for the customer's money amount
from project_two_functions import show_vending_options, handle_selection

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

class VendingMachine:
    """
        class docstring
    """
    def __init__(self) -> None:
        pass
    def make_machine(self, t: Turtle) -> None:
        """
            This is the vending machine drawn in the turtle window
        """
        # box for outer vending machine
        t.penup()
        t.goto(200, 300)
        t.pendown()
        t.goto(-200, 300)
        t.goto(-200, -300)
        t.goto(200, -300)
        t.goto(200, 300)
        t.penup()

        # line on top (title)
        t.goto(150, 220)
        t.pendown()
        t.goto(-150, 220)
        t.penup()

        # snacks box <-- make these classes
        t.goto(-150, 110)
        t.pendown()
        t.goto(-150, 10)
        t.goto(-30, 10)
        t.goto(-30, 110)
        t.goto(-150, 110)
        t.penup()
        t.goto(-120, 60)
        t.write("Snacks\nSelection", False, align="left", font=("Verdana", 11, "bold"))

        # candies box <-- make these classes
        t.goto(150, 110)
        t.pendown()
        t.goto(150, 10)
        t.goto(30, 10)
        t.goto(30, 110)
        t.goto(150, 110)
        t.penup()
        t.goto(60, 60)
        t.write("Candies\nSelection", False, align="left", font=("Verdana", 11, "bold"))

        # drinks box <-- make these classes
        t.goto(-150, -20)
        t.pendown()
        t.goto(-150, -120)
        t.goto(150, -120)
        t.goto(150, -20)
        t.goto(-150, -20)
        t.penup()
        t.goto(-75, -70)
        t.write("Drinks Selection", False, align="left", font=("Verdana", 11, "bold"))


def main():
    """
    Main function to run vending machine.
    """

    canvas = turtle.Screen()
    canvas.title("Vending Machine")
    turt: Turtle = Turtle()
    turt.shape("turtle")

    money: int = randint(1, 10)
    cart: list[str] = []

    answer = canvas.textinput("NAME", "What's your name?")
    turt.goto(0, 230)
    # turt.hideturtle()
    turt.write(f"Hi, {answer}! Welcome to the Vending Machine!", True, align="center",
               font=("Verdana", 13, "normal"))
    turt.penup()

    money: int = randint(1, 10)
    turt.goto(0, 200)
    turt.write(f"You have ${money} to spend.", align="center", font=("Verdana", 11, "normal"))
    turt.penup()
    turt.goto(0,0)

    # turt.onclick( 1, True)

    while money > 0:
        show_vending_options()
        selection = canvas.textinput("SELECTION", "What items would you like to view? "
        "(Or 'exit' to leave)")

        response: str = str(selection)

        if response.lower() == "exit":
            pass

        elif response == "Drinks":
            money = handle_selection(drinks, money, "Drinks", cart)

        elif response == "Snacks":
            money = handle_selection(snacks, money, "Snacks", cart)

        elif response == "Candies":
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
    vending_machine: VendingMachine = VendingMachine()
    main()

    done()
