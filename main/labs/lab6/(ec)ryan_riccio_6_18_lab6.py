# this is from program 6-18 (in the spotlight)
# according to the powerpoint, i can get extra credit from this
# modify_coffee_record.py
# this program modifies inventory records from coffee.txt

# import this to access operating system commands
import os


# main function
def main():
    found = False
    try:
        # get the input for var search for
        search = input("Enter the description to search for: ")
        # if the search succeeds, what shall we overwrite it with
        new_quantity = int(input("Enter the new quantity: "))

        # open files
        # do not use "with" because there are multiple files open
        coffee_file = open("coffee.txt", "r")
        temp_file = open("temp.txt", "w")

        # priming read
        description = coffee_file.readline()
        # if a description is still there (we haven't reached the end)
        while description != "":
            # convert the quantity read to float and get rid of \n
            quantity = float(coffee_file.readline())
            description = description.rstrip("\n")

            # if our search is successful
            if description == search:
                # write the description and new quantity
                temp_file.write(description + '\n')
                temp_file.write(str(new_quantity) + "\n")

                found = True
            else:
                # if not found, write the old data
                # this will write all of the data
                # to temp file, no matter what it is
                # if will only update it if the search
                # is successful. If the search is not
                # successful temp_file == coffee_file
                temp_file.write(description + "\n")
                temp_file.write(str(quantity) + "\n")

            # read next record
            description = coffee_file.readline()

        # close both of the files after were done working with them
        coffee_file.close()
        temp_file.close()

        # remove and replace
        os.remove("coffee.txt")
        os.rename("temp.txt", "coffee.txt")

        # print the message depending on whether or not we found it
        if found:
            print("The file has been updated.")
        else:
            print(f"The coffee '{search}' was not found.")

    # if a bad value is inputted or conversion fails
    except ValueError:
        print("ERROR: You did not enter a valid quantity. Exiting...")
    # if the file doesn't exist
    except FileNotFoundError:
        print("ERROR: The file could not be found!. Exiting...")
    # if some other file error occurs
    except IOError:
        print("ERROR: The file cannot be accessed (maybe you don't have permission?). Exiting...")
    # if something weird happened
    except:
        print("ERROR: Unknown error occurred. Exiting...")


# call main
main()
