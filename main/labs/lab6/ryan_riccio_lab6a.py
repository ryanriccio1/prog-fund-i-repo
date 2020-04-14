# import custom module, sleep, and os functions
from metric_conversion import show_menu, save_to_file, IncorrectEntryException, TooManyTriesError
from time import sleep
from os import path, remove


# main
def main():
    # delete the file at start of program
    if path.exists("conversions.txt"):
        remove("conversions.txt")

    # display welcome message
    print('Hi William! This will convert from imperial units to the metric system.\n'
          "Just put in the value that you want, and then hit enter! It's simple!\n"
          f'{"Code by Ryan Riccio":-^69}\n')

    try:
        # to keep count of number of complete conversions
        count = 1
        keep_looping = True
        # will stop after 10 complete conversions
        while keep_looping and count < 11:
            try:
                # from custom module
                show_menu(count)
            # if the user enters a bad input during show_menu()
            except IncorrectEntryException:
                print("Please enter a letter between 'a' and 'e'.\n")
            else:
                # if no bad input, add to count
                count += 1
            finally:
                # no matter what happens, wait a second for user
                # to be able to see error or the conversions before
                # the menu gets printed again (this is to draw more
                # attention to the output, not the menu, also so user has time to read)
                sleep(1)

        # after loop, close the file and print the reason
        save_to_file(close=True, reason="Success!")
    # if error occurs, except, close file, and give reason
    except TooManyTriesError:
        save_to_file(close=True, reason="TooManyTriesError")
    # if file errors occur, except, and exit
    except FileNotFoundError:
        print("ERROR: The file has not been found! Exiting...")
    except IOError as err:
        print("ERROR: File Error. REASON:")
        print(err)
    # if all goes well, thank the user
    else:
        print("\nThanks William for using my program! See ya later!")


# call main()
main()
