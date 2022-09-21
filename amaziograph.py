# Done by WONG, Hiu Tung SID: 20859316
import turtle

turtle.setup(800,600)    # Set the width and height be 800 x 600

number_of_divisions = 8  # The number of subdivisions around the centre
turtle_width = 3         # The width of the turtles

# Don't show the animation
turtle.tracer(False)

# Draw the background lines

backgroundLineTurtle = turtle.Turtle()

backgroundLineTurtle.width(1)

backgroundLineTurtle.down()
backgroundLineTurtle.color("gray84") # Draw the centered line
for i in range(number_of_divisions):
    backgroundLineTurtle.forward(500)
    backgroundLineTurtle.backward(500)
    backgroundLineTurtle.left(360 / number_of_divisions)

backgroundLineTurtle.up()

# Show the instructions
backgroundLineTurtle.color("purple")
backgroundLineTurtle.goto(-turtle.window_width()/2+50, 100)
backgroundLineTurtle.write("""s - change a colour for one of the colour buttons
m - all 8 drawing turtles go to middle
c - clear all drawings made by the 8 drawing turtles
""", font=("Arial", 14, "normal"))

backgroundLineTurtle.hideturtle()

# Set up a turtle for handling message on the turtle screen
textTurtle = turtle.Turtle()
# This sets the colour of the text to red
textTurtle.color("red")
# We do not want it to show/draw anything, except the message text
textTurtle.up() 
# Set it the be at center, near the colour selections
textTurtle.goto(0, -200)
# We do not want to show it on the screen
textTurtle.hideturtle()

# Part 2 Preparing the drawing turtles

# The drawing turtles are put in a list
allDrawingTurtles = [] 

# Part 2.1 Add the 8 turtles in the list
for _ in range(number_of_divisions):
    new_turtle = turtle.Turtle()
    
    #set up
    new_turtle.hideturtle()
    new_turtle.speed(0)
    new_turtle.width(turtle_width)
    
    #add to the list
    allDrawingTurtles.append(new_turtle)
    
# Part 2.2 Set up the first turtle for drawing
dragTurtle = allDrawingTurtles[0]
dragTurtle.showturtle()
dragTurtle.shape("circle")
dragTurtle.shapesize(2,2)

# Part 3 Preparing the basic drawing system
# Set up the ondrag event
def draw(x,y):
    dragTurtle.ondrag(None)
    turtle.tracer(False)

    textTurtle.clear()

    #control drawing turtle
    dragTurtle.goto(x,y)

    #move all 7 other turtle
    x_transform = [1, 1, -1, -1, 1, 1, -1, -1] 
    y_transform = [1, -1, 1, -1, 1, -1, 1, -1]
    for i in range(1,number_of_divisions):
        new_x = x * x_transform[i]
        new_y = y * y_transform[i]
        if i < 4:
            allDrawingTurtles[i].goto(new_x,new_y)
        else:
            allDrawingTurtles[i].goto(new_y,new_x)
        
    turtle.tracer(True)
    dragTurtle.ondrag(draw)
    '''
    note to urself why recursive function???? its to close the previous ondrag
    and too much ondrag stacked tgt
    so shut down first, then reopen it to ensure only one ondrag is going on
    '''

    
# Part 5.2 clear all drawings made by the 8 drawing turtles
def clearDrawing():
    textTurtle.clear()
    
    for i in allDrawingTurtles:
        i.clear()
        
    textTurtle.write("The screen is cleared",align="center", font="Arial")


# Part 5.3 all 8 drawing turtles go to middle
def goToMiddle():
    textTurtle.clear()

    for i in allDrawingTurtles:
        i.up()
        i.goto(0,0)
        i.down()
    
    textTurtle.write("All 8 turtles returned to middle",align="center", font="Arial")


# Part 4 handling the colour selection
# Make the colour selection turtles
# Here is the list of colours
colours = ["black", "orange red", "lawn green", "light sky blue", "medium purple", "orchid", "gold"]

# Part 4.2 Set up the onclick event
def handleColourChange(x,y):
    for i in range(len(colours)):
        if x <= (-130 + 50 * i):
            for j in allDrawingTurtles:
                j.color(colours[i])
            break

        
# Part 5.4 change a colour in the colour selection
def changeColour():
    textTurtle.clear()
    num = -1
    while num < 0 or num > 6: 
        num = turtle.textinput("Change color","Please enter a correct index number: (0-6)")
        if num == None:
            break
        num = int(num)
    if num != None:
        new_c = turtle.textinput("Change color","Please type the color you want to use e.g. LightBlue2:")
        if new_c != None:
            colours[num] = new_c
            colourSelectionTurtles[num].color(new_c)
            textTurtle.write("This colour is set and can be used",align="center", font="Arial")
    turtle.listen()

# Part 4.1 Make the colour selection turtles
colourSelectionTurtles = []
for i in range(len(colours)):
    t = turtle.Turtle(shape="square")
    t.up()
    t.color(colours[i])
    t.shapesize(2,2)
    t.goto(-150+50*i,-250)
    t.onclick(handleColourChange)
    colourSelectionTurtles.append(t)

turtle.tracer(True)
turtle.listen()
dragTurtle.ondrag(draw)
turtle.onkeypress(clearDrawing,'c')
turtle.onkeypress(goToMiddle,'m')
turtle.onkeypress(changeColour,'s')

turtle.done()

