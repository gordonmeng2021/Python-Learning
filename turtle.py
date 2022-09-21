import turtle
import random
import turtle_color

# turtle stats
def stats():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    turtle.hideturtle()
    turtle.speed(10)
    
    turtle.penup()
    turtle.width(random.randint(1,10))
    turtle.goto(x,y)
    turtle.right(random.randint(0,89))
    turtle.color(random.choice(turtle_color.turtle_color),random.choice(turtle_color.turtle_color))
    turtle.pendown()

# Draw a sqare or recrangle
def rectangle_or_square(a,b):
    stats()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
    turtle.end_fill()

# Draw a circle or sector
def circle_or_sector(a):
    stats()
    r = random.randint(1,150)
    turtle.begin_fill()
    turtle.circle(r,a)
    turtle.end_fill()


# interface
def draw_stuff():
    print("Beautiful Mordern Art!!!!!\n")
    print("this program will display some beautiful modern art, accordint to your choices.\n")
    print("Please choose one of the following.\n")
    print("1 - using squares/rectangles")
    print("2 - using turtle.circle")
    print()
    n = input("Which one do you want? ")

    if n == "1":
        print("Please choose one of the following:\n")
        print("a - simple art")
        print("b - advanced art")
        print()
        m = input("Which one do you want? ")
        if m == "a":
            for _ in range(70):
                a = random.randint(1,150)
                rectangle_or_square(a,a)
        elif m == "b":
            for _ in range(70):
                a = random.randint(1,150)
                b = random.randint(1,150)
                rectangle_or_square(a,b)
        else:
            print("Invalid you piece of shit.")
            draw_stuff()
    elif n == "2":
        print("Please choose one of the following:\n")
        print("a - simple art")
        print("b - advanced art")
        print()
        m = input("Which one do you want? ")
        if m == "a":
            for _ in range(70):
                circle_or_sector(360)
        elif m == "b":
            for _ in range(70):
                circle_or_sector(random.randint(1,360))
        else:
            print("Invalid you piece of shit.")
            draw_stuff()
    else:
        print("Invalid you piece of shit.")
        draw_stuff()


draw_stuff()
