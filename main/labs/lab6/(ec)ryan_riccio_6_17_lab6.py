# this is from program 6-17 (in the spotlight)
# according to the powerpoint, i can get extra credit from this
# search_coffee_record.py
# this program searches inventory records from coffee.txt


# main function
def main():
    try:
        found = False
        # get user input for the coffee they want to find
        search = input("Enter the description to search for: ")
        # open file (with auto closes the file)
        with open("coffee.txt", "r") as coffee_file:
            # read the first line (priming read)
            description = coffee_file.readline()
            # loop while the line exists (until end of file)
            while description != "":
                # convert the str to float and get rid of \n
                quantity = float(coffee_file.readline())
                description = description.rstrip("\n")

                # if we find what they're looking for
                if description == search:
                    # display what we were looking for
                    print(f"Description: {description}")
                    print(f"Quantity: {quantity}")
                    print("")
                    found = True
                # read next line
                description = coffee_file.readline()

        # but i still haven't found what i'm looking for ~U2
        # if the search was not a success
        if not found:
            print(f"The coffee '{search}' was not found.")
    # if there was a value that could not be converted to float
    except ValueError:
        print("ERROR: An invalid value was read. Exiting...")
    # if the file could not be found
    except FileNotFoundError:
        print("ERROR: The file could not be found!. Exiting...")
    # if the file is just being weird on us and not working right
    except IOError:
        print("ERROR: The file cannot be accessed (maybe you don't have permission?). Exiting...")
    # if something else weird happens
    except:
        print("ERROR: Unknown error occurred. Exiting...")


# call main
main()
