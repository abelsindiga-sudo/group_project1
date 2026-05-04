"""
project_two_functions.py

Emma, Dot, Abel
CSCI 1101-12
Prof R

Project #2 - vending machine v02
    Functions page for calling in the main file
"""
import turtle
from turtle import Turtle
import time

class Item:
    """
        A representation of an item in the vending machine.
    """
    def __init__(self, name, price) -> None:
        """
            The constructor for the items
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.name + ": $" + str(self.price)

class VendingMachine:
    """
        A representation of a vending machine.
    """
    def __init__(self) -> None:
        """
            The constructor for the vending machine.
        """
        self.balance = 0
        self.snacks: list[Item] = []
        self.candies: list[Item] = []
        self.drinks: list[Item] = []

    def __add__(self, pay) -> list:
        """
            Will create a list of all of the items in the vending machine, not in categories.
        """
        snacks = self.snacks
        candies = self.candies
        drinks = self.drinks

        total: list[Item] = [snacks, candies, drinks] # type: ignore
        return total

    def add_item(self, name: str, price: int, category: str) -> None:
        """
            Function works to add items into the vending machine.

            Parameters
            ----------
            name: str 
                the name of the item
            price: int
                the price of the item
            category: str
                the category the item falls into (drinks, snacks, or candies)
        """
        item = Item(name, price)
        if category == "snacks":
            self.snacks.append(item)

        if category == "drinks":
            self.drinks.append(item)

        if category == "candies":
            self.candies.append(item)

    def purchase_item(self, index, pay, total):
        """
            Function works to buy items from the vending machine.

            Parameters
            ----------
            index: str 
                the name of the item
            pay: int
                the amount of money the user has
            total: list[Item]
                the total stock as given by the earlier function __add__()
        """
        item = total[index]
        if item.price > pay:
            print("You don't have enough money!")
        else:
            self.balance += item.price
            change = pay - item.price
            return item, change

    def __str__(self) -> str:
        """
            Provides the amount of money left to buy things as a string.
        """
        info = "Vending Machine balance: " + str(self.balance) + "\n"
        return info

def make_machine(vm) -> None:
    """
        This is the code that creates the vending machine boxes and graphic in Turtle.
    """
    t: Turtle = Turtle()

    canvas = turtle.Screen()
    canvas.title("Vending Machine")

    answer = canvas.textinput("NAME", "What's your name?")

    t.penup()
    t.goto(0, 230)
    t.write(f"Hi, {answer}! Welcome to the Vending Machine!",
               align="center", font=("Verdana", 13, "normal"))

    t.goto(0, 200)
    t.write("You have unlimited money to spend!",
               align="center", font=("Verdana", 11, "normal"))

    t.hideturtle()
    canvas.tracer(0)

    # ---------- ALL BELOW IS MAKING TURTLE MACHINE -----------

    # Building the basic machine
    t.penup()
    t.goto(200, 300)
    t.pendown()
    t.goto(-200, 300)
    t.goto(-200, -300)
    t.goto(200, -300)
    t.goto(200, 300)
    t.penup()

    t.goto(150, 220)
    t.pendown()
    t.goto(-150, 220)
    t.penup()

    # Snacks
    t.goto(-150, 110)
    t.pendown()
    t.goto(-150, 10)
    t.goto(-30, 10)
    t.goto(-30, 110)
    t.goto(-150, 110)
    t.penup()

    t.goto(-130, 85)
    for snack in vm.snacks:
        t.write(snack, font=("Verdana", 11, "normal"))
        t.goto(-130, t.ycor() - 15)

    # Candies
    t.goto(150, 110)
    t.pendown()
    t.goto(150, 10)
    t.goto(30, 10)
    t.goto(30, 110)
    t.goto(150, 110)
    t.penup()

    t.goto(60, 85)
    for candy in vm.candies:
        t.write(candy, font=("Verdana", 11, "normal"))
        t.goto(60, t.ycor() - 15)

    # Drinks
    t.goto(-150, -20)
    t.pendown()
    t.goto(-150, -100)
    t.goto(150, -100)
    t.goto(150, -20)
    t.goto(-150, -20)
    t.penup()

    t.goto(0, -45)
    for drink in vm.drinks:
        t.write(drink, font=("Verdana", 11, "normal"))
        t.goto(0, t.ycor() - 15)

    t.goto(0, -200)
    t.write("Click which category would you like to choose?", align="center",
            font=("Verdana", 10, "italic"))


def animate_button(t, canvas, x1, y1, x2, y2, label, vm):
    """
        Makes the clicking on the screen work to produce an output through turtle

        Parameters
        ----------
        t: Turtle
            the turtle that is on screen
        canvas: Screen
            the screen/window
        x1, y1, x2, y2: int
            the coordinates for the boxes for where the click on screen will come from.
        label: str
            what heading will appear when the screen is clicked
        vm: VendingMachine
            the general vending machine as a whole
    """
    if label == "Return":
        t.clear()

    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.fillcolor("lavender")
    t.begin_fill()
    t.goto(x1, y2)
    t.goto(x2, y2)
    t.goto(x2, y1)
    t.goto(x1, y1)
    t.end_fill()
    t.penup()

    t.goto((x1 + x2)//2 - 35, (y1 + y2)//2 - 10)
    t.write(label, font=("Verdana", 11, "bold"))

    canvas.update()
    time.sleep(0.15)

    t.clear()
    make_machine(vm)
