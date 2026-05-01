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
        docstring
    """
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return self.name + ": $" + str(self.price)

    def __repr__(self) -> str:
        return str(self)

class VendingMachine:
    """
        docstring
    """
    def __init__(self) -> None:
        self.balance = 0
        self.snacks: list[Item] = []
        self.candies: list[Item] = []
        self.drinks: list[Item] = []

        self.total: list[Item] = [self.snacks, self.candies, self.drinks] # type: ignore

    def add_item(self, name, price, category) -> None:
        """
            docstring
        """
        item = Item(name, price)
        if category == "snacks":
            self.snacks.append(item)

        if category == "drinks":
            self.drinks.append(item)

        if category == "candies":
            self.candies.append(item)

    def purchase_item(self, index, pay):
        """
            docstring
        """
        item = self.total[index]
        if item.price > pay:
            print("You don't have enough money!")
        else:
            self.balance += item.price
            change = pay - item.price
            return item, change

    def __str__(self) -> str:
        """
            docstring
        """
        info = "Vending Machine balance: " + str(self.balance) + "\n"
        for item in self.total:
            info += str(item) + "\n"

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
        ???
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
