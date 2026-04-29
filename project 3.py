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
from project_two_functions import show_vending_options, handle_selection

# -------------------- NEW IMPORT --------------------
import time

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
    def __init__(self) -> None:
        pass

    def make_machine(self, t: Turtle) -> None:
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
        t.goto(-120, 60)
        t.write("Snacks\nSelection", align="left", font=("Verdana", 11, "bold"))

        # Candies
        t.goto(150, 110)
        t.pendown()
        t.goto(150, 10)
        t.goto(30, 10)
        t.goto(30, 110)
        t.goto(150, 110)
        t.penup()
        t.goto(60, 60)
        t.write("Candies\nSelection", align="left", font=("Verdana", 11, "bold"))

        # Drinks
        t.goto(-150, -20)
        t.pendown()
        t.goto(-150, -120)
        t.goto(150, -120)
        t.goto(150, -20)
        t.goto(-150, -20)
        t.penup()
        t.goto(-75, -70)
        t.write("Drinks Selection", align="left", font=("Verdana", 11, "bold"))


# -------------------- NEW FUNCTIONS --------------------

def draw_cart(t, cart):
    t.goto(-180, -200)
    t.write("Cart:", font=("Verdana", 10, "bold"))

    y = -220
    for item in cart:
        t.goto(-180, y)
        t.write(f"- {item}", font=("Verdana", 9, "normal"))
        y -= 20


def show_items_on_screen(t, machine, items_dict, title):
    t.clear()
    machine.make_machine(t)

    t.goto(0, 240)
    t.write(f"{title} Menu", align="center", font=("Verdana", 14, "bold"))

    y = 150
    for key in items_dict:
        name, price = items_dict[key]
        t.goto(-100, y)
        t.write(f"{key}. {name} - ${price}", font=("Verdana", 11, "normal"))
        y -= 30

    t.goto(0, -200)
    t.write("Enter item number in popup", align="center", font=("Verdana", 10, "italic"))


def animate_button(t, canvas, machine, x1, y1, x2, y2, label):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.fillcolor("gray")
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
    machine.make_machine(t)


# -------------------- MAIN --------------------

def main():
    canvas = turtle.Screen()
    canvas.title("Vending Machine")

    turt: Turtle = Turtle()
    turt.shape("turtle")

    # NEW UI SETUP
    turt.hideturtle()
    canvas.tracer(0)

    vending_machine: VendingMachine = VendingMachine()
    vending_machine.make_machine(turt)

    money: int = randint(1, 10)
    cart: list[str] = []

    answer = canvas.textinput("NAME", "What's your name?")

    def redraw_screen():
        turt.clear()
        vending_machine.make_machine(turt)

        turt.goto(0, 230)
        turt.write(f"Hi, {answer}! Welcome to the Vending Machine!",
                   align="center", font=("Verdana", 13, "normal"))

        turt.goto(0, 200)
        turt.write(f"You have ${money} to spend.",
                   align="center", font=("Verdana", 11, "normal"))

        draw_cart(turt, cart)

        canvas.update()

    redraw_screen()

    # CLICK SYSTEM (replaces while loop)
    def handle_click(x, y):
        nonlocal money

        if -150 < x < -30 and 10 < y < 110:
            animate_button(turt, canvas, vending_machine, -150, 10, -30, 110, "Snacks")
            show_items_on_screen(turt, vending_machine, snacks, "Snacks")
            canvas.update()
            money = handle_selection(snacks, money, "Snacks", cart)

        elif 30 < x < 150 and 10 < y < 110:
            animate_button(turt, canvas, vending_machine, 30, 10, 150, 110, "Candies")
            show_items_on_screen(turt, vending_machine, candies, "Candies")
            canvas.update()
            money = handle_selection(candies, money, "Candies", cart)

        elif -150 < x < 150 and -120 < y < -20:
            animate_button(turt, canvas, vending_machine, -150, -120, 150, -20, "Drinks")
            show_items_on_screen(turt, vending_machine, drinks, "Drinks")
            canvas.update()
            money = handle_selection(drinks, money, "Drinks", cart)

        redraw_screen()

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

            canvas.update()

    canvas.onclick(handle_click)

    done()


if __name__ == "__main__":
    main()