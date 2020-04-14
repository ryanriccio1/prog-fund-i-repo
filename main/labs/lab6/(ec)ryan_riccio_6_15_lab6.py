# this is from program 6-15 (in the spotlight)
# according to the powerpoint, i can get extra credit from this
# add_coffee_record.py
# this program adds inventory records to coffee.txt


# main function
def main():
    # default selection and prompt
    more_entries = "y"
    print("Enter the following coffee data.")
    try:
        # open file (with auto closes file)
        with open("coffee.txt", "a") as coffee_file:
            # loop until no more entries
            while more_entries == "y" or more_entries == "yes":
                # get data from the user
                description = input("Description: ")
                quantity = int(input("Quantity (in pounds): "))

                # write to file and separate by newline
                coffee_file.write(description + "\n")
                coffee_file.write(str(quantity) + "\n")

                # ask for more entries
                more_entries = input("Do you have more records? (y/n): ").lower()
                print("")

        # when there are no entries, tell the user what happened
        print("Data added to file.")
        print("Goodbye!")

    # if a bad value was entered
    except ValueError:
        print("ERROR: You did not enter a valid quantity. Exiting...")
    # if it couldn't create or find the file
    except FileNotFoundError:
        print("ERROR: The file could not be found!. Exiting...")
    # if some other file error occurred
    except IOError:
        print("ERROR: The file cannot be accessed (maybe you don't have permission?). Exiting...")
    # if something weird happened
    except:
        print("ERROR: Unknown error occurred. Exiting...")

# call main
main()
