# remind them about that the lab should be the version with turtle graphics!!!!!!!!!
import random               # Import the 'random' library

target = 0                  # We will store the number to be guessed here
finished = False            # This is true if the game has finished
guess_input_text = ""       # We will store text in here
guess_input = 0             # We will store a number in here

# should only be counting the number of valid guesses
count = 0                   # The counter that will store the number of times it took you to guess the answer

# Generate a new integer random number
target = random.randint(1,100)
print("I am thinking of a number. What number am I thinking of?")

# Do the main game loop
while not finished:
    # Get the user's guess
    guess_input_text = input("Please enter a number between 1 and 100: ")
    # Input is string so change it to the correct data type
    guess_input = int(guess_input_text)

    # Check the user's guess
    if guess_input > 100 or guess_input < 1: # out of range
        print("Please enter an integer number between 1 and 100.")
    elif guess_input < target: # checking if it is too low
        guess = guess + 1 # the more intuitive syntax
        # guess += 1
        print("Too Low.")
    elif guess_input > target: # checking if it is too high
        guess = guess + 1 
        # guess += 1
        print("Too High.")
    else:
        print("You got it! My number is", target, ".")
        print("You took", count, "tries to guess the correct answer.")
        finished = True # to exit the while loop

# At this point, the game is finished
