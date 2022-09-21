# rmb we uses idle to help them oh god why why
# not showing them this code 
# should be how the final works!!!!
# remind them about that the lab should be the version with turtle graphics!!!!!!!!!
import random               # Import the 'random' library
import turtle               # Import the 'turtle' library

target = 0                  # We will store the number to be guessed here
finished = False            # This is true if the game has finished
guess_input_text = ""       # We will store text in here
guess_input = 0             # We will store a number in here
xposition = -100            # the starting position of the turtle
yposition = 150

turtle.penup()

# should only be counting the number of valid guesses
count = 0                   # The counter that will store the number of times it took you to guess the answer

# Generate a new integer random number
target = random.randint(1,100)
print("I am thinking of a number. What number am I thinking of?")

# Do the main game loop
while not finished:
    # Get the user's guess, turtle style
    # First attribute is the title of the input box
    # Second one is the prompt/ the questin to be answered for the input
    # title = "", prompt = ""
    guess_input_text = turtle.textinput("Guessing Game", "Please enter a number between 1 and 100:")
    # input is always string
    guess_input = int(guess_input_text)

    # Check the user's guess
    # the comma is a print() special operation, in turtle.write it must be string so you must 
    # use string concatinaton operands (+)
    # the font= is the attributes of the write function of the turtle aka changing the looks
    # NO TURTLE.CLEAR IN THE FINAL PRODUCT I REPEAT NO TURTLE.CLEAR IN THE FINAL PRODUCT
    if guess_input > 100 or guess_input < 1: # out of range
        
        turtle.goto(xposition, yposition)
        turtle.write("Please enter an integer number between 1 and 100.", )
        yposition = yposition - 40 # Move to a new line

    elif guess_input < target: # checking if it is too low

        count = count + 1 # the more intuitive syntax
        #count += 1

        turtle.goto(xposition, yposition)
        turtle.write("Too Low.", font=("Arial", 40, "bold"))
        yposition = yposition - 40

    elif guess_input > target: # checking if it is too high

        count = count + 1 
        #count += 1

        turtle.goto(xposition, yposition)
        turtle.write("Too High.", font=("Arial", 40, "bold"))
        yposition = yposition - 40

    else:
        count = count + 1 
        #count += 1

        turtle.goto(xposition, yposition)
        turtle.write("You got it! My number is " + str(target) + ".", font=("Arial", 40, "bold"))
        yposition = yposition - 40

        turtle.goto(xposition, yposition)
        turtle.write("It took you " + str(count) + " guesses to get the number!", font=("Arial", 40, "bold"))
        yposition = yposition - 40

        finished = True # to exit the while loop

# At this point, the game is finished
