# ATTENTION! to better debug the game, when it asks for a guess
# enter in "admin" (without quotes) for the password
# it will then give the user the random number generated


# import only randint to generate random number
# import regular expression searching for input error checking
# import sleep for loading effect and trailing "." effect when
# starting a new game
from random import randint
from re import search
from time import sleep

# constants to determine range of randint
START_NUM = 1
END_NUM = 1000


# main(bool) to determine whether or not to show welcome message
def main(first_try):
    # call start_game() and get game variables
    rand_num, correct, num_guess = start_game(first_try)

    # main game loop
    while not correct:
        # keep getting guesses and checking for correct
        guess, num_guess = get_guess(num_guess, rand_num)
        correct = check_guess(rand_num, guess, num_guess)
    # when correct, see if the user wants to play again
    play_again()


# function to reset game variables and display welcome message
def start_game(first_try):
    # reset vars
    correct = False
    num_guess = 0

    # generate new number
    new_number = randint(START_NUM, END_NUM)

    # display welcome message based off if it's the first time
    if first_try:
        print(f"This is a guessing game where you will guess a number between {START_NUM} and {END_NUM}.\n"
              f"Invalid answers will still count to your number of guesses so be careful!\n")
    else:
        print("Starting new game", end="")
        # period animation (add . every 1/4 sec)
        # to give the illusion of loading
        for i in range(4):
            print(".", end="")
            sleep(.25)
        print("\n")

    return new_number, correct, num_guess


def get_guess(num_guess, rand_num):
    # set guess to empty and start validation loop
    guess = ""
    valid = False
    while not valid:
        guess = input("Enter your guess: ")
        # if admin pass is correct, show rand_num and get guess again
        if guess == "admin":
            print(f"***YOU ARE NOW ENTERING ADMIN MODE***\nTHE RANDOM NUMBER IS: {rand_num}.")
            guess = input("Enter your guess: ")

        # add to number of guesses (all user inputs, except admin password, will
        # count as a guess, even invalid ones
        num_guess += 1

        # REGEX KEY
        # ^ = start of string
        # [-]? = optional negative
        # \d* = zero or more digit (0-9)
        # \d+ = one or more digit (0-9)
        # \. = literal "."
        # $ = end of string

        # search for float ((-)x.x/(-).x)
        regex_float = search(r"^[-]?\d*\.\d+$", guess)

        # search for float part ((-)x.)
        regex_float_part = search(r"^[-]?\d+\.$", guess)

        # search for int ((-)x)
        regex_int = search(r"^[-]?\d+$", guess)

        # if match, display error message based on type
        if regex_float:
            print("The value must be an integer (number without a decimal), please try again. ")
        elif regex_float_part:
            print("It's like you wanted to type a decimal number, but you didn't finish!\n"
                  "I only take integers (numbers without decimals), please try again.")

        # if type(guess) == int (inferred type, not literal type)
        elif regex_int:
            # convert to int literal
            guess = int(guess)

            # if guess too high or too low, tell the player, otherwise exit loop and return values
            if guess < START_NUM:
                print("That value is lower than the given range, please try again.")
            elif guess > END_NUM:
                print("That value is larger than the given range, please try again.")
            else:
                valid = True
        # if not float, float_part, or int, it must have a non-digit character so it's not a num
        else:
            print("That is not a number, please try again.")

    return guess, num_guess


# check to see if guess is correct
def check_guess(num, guess, num_guess):
    # if guess is correct, no need to do any checks, just celebrate!
    if num == guess:
        # print num, and num_guess and congratulate
        print(f"\nThe number was {num}!\nYou rock! You guessed the number in {num_guess}", end=" ")
        # use num_guess to pick between plural and singular
        if num_guess == 1:
            print("try!\n")
            # wait a half second for the user to feel congratulated
            sleep(.5)
        else:
            print("tries!\n")
            sleep(.5)
        return True
    # if greater than but not greater than by more than 5 (range 10)
    elif num < guess <= num + 5:
        print("Getting warm but still high!")
    # if less than but not less than by more than 5 (range 10)
    elif num - 5 <= guess <= num:
        print("Getting warm but still low!")
    # if greater by more than 5
    elif guess < num:
        print("Too low!")
    # if less by more than 5
    elif guess > num:
        print("Too high!")
    # i don't even know how the user gets here, but why not, its only 77 bytes
    else:
        print("I don't know what number you even typed that it got this far...")

    return False


def play_again():
    # start validation loop
    correct_input = False
    while not correct_input:
        # whatever the user input is, make it lowercase
        user_input = input("Do you want to play again? (y/n): ").lower()

        # error checking
        if user_input == "y" or user_input == "yes":
            # start over
            main(first_try=False)
            correct_input = True
        elif user_input == "n" or user_input == "no":
            print("\nThanks for playing! Goodbye!")
            correct_input = True
        else:
            print("That was not a valid input, try again.")


# call main
main(first_try=True)
