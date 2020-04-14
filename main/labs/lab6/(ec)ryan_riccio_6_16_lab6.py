# this is from program 6-16 (in the spotlight)
# according to the powerpoint, i can get extra credit from this
# show_coffee_record.py
# this program displays inventory records from coffee.txt


# main function
def main():
    try:
        # open file (with auto closes file)
        with open("coffee.txt", "r") as coffee_file:
            # read the first line (priming read)
            description = coffee_file.readline()
            # loop while the line still exists
            while description != "":
                # get rid of the newline
                description = description.rstrip("\n")

                # read and remove newline
                quantity = coffee_file.readline()
                quantity = quantity.rstrip("\n")

                # print the data that was just read
                print("Description:", description)
                print("Quantity:", quantity, "\n")

                # read the next line
                description = coffee_file.readline()

    # if file is no where to be seen
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
