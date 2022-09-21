import turtle       # Import the turtle module for the program

turtle.width(4)
turtle.speed(10)

##### Initialize the colour
pencolor = "black"
fillcolor = "black"
turtle.pencolor(pencolor)
turtle.fillcolor(fillcolor)

print("Welcome to the Python Sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""


while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw a generated explosion ")
    print("a - Draw the author's information")
    print("q - Quit the program")
    print()

    option = input("Please enter your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        # ask the user to enter the angle of rotation
        a = int(input("Please enter the angle of rotation: "))

        # turtle turn
        turtle.left(a)

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y value
        x = input("Please enter the x value: ")
        x = int(x)
        y = input("Please enter the y value: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        # ask the user for the width and height
        w = int(input("Please enter the width of the rectangle: "))
        h = int(input("Please enter the height of the rectangle: "))
        
        # Draw rectangle
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(w)
            turtle.left(90)
            turtle.forward(h)
            turtle.left(90)
        turtle.end_fill()

    ##### Handle the circle option
    if option == "c":
        print()

        # ask circle radius
        r = int(input("Please enter the radius of the circle: "))
        
        # DRAW CIRCLE
        turtle.begin_fill()
        turtle.circle(r)
        turtle.end_fill()

    ##### Handle the pen colour option
    if option == "p":
        print()

        # input pen color
        pencolor = input("Please enter a colour name for the pen colour: ")
        
        # change pen color
        turtle.pencolor(pencolor)

    ##### Handle the fill colour option
    if option == "f":
        print()

        # ask for fill color
        fillcolor = input("Please enter a colour name for the fill colour: ")
        
        # change fill color
        turtle.fillcolor(fillcolor)

    ##### Handle the generated flower
    if option == "g":
        print()

        # input size of petal
        s = int(input("Please enter the size of the flower petal: "))

        # draw
        for _ in range(12):
            for _ in range(3):
                turtle.forward(s)
                turtle.left(120)
            turtle.left(30)

    ##### Handle explosion
    if option == "e":
        print()

        # input size of explosion
        k = int(input("Please enter the size of the explosion (>150): "))
        for color in ["firebrick","DarkOrange","goldenrod","bisque"]:
            for i in range(1,5):
                turtle.color(color+str(i))
                turtle.dot(k)
                k -= 10

        # return og colors
        turtle.color(pencolor,fillcolor)

    ##### Your Initial
    if option == "a":
        for _ in range(2):
            turtle.right(70)
            turtle.forward(50)
            turtle.left(140)
            turtle.forward(50)
            turtle.right(70)
            
        turtle.up()
        turtle.goto(turtle.xcor()+25,turtle.ycor()-15)
        turtle.dot(35)

        turtle.goto(turtle.xcor()+25,turtle.ycor()-15)
        turtle.down()
        turtle.left(90)
        turtle.forward(15)
        turtle.right(180)
        turtle.circle(15,-180)
        turtle.backward(15)

        turtle.up()
        turtle.goto(turtle.xcor()+25,turtle.ycor()+15)
        turtle.dot(35)
        turtle.up()
        turtle.goto(turtle.xcor()+15,turtle.ycor())
        turtle.down()
        turtle.backward(30)
        turtle.circle(15,-180)

turtle.done()
