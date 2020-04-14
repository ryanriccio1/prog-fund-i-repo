# this is from program 6-19 (in the spotlight)
# according to the powerpoint, i can get extra credit from this
# delete_coffee_record.py
# this program deletes inventory records from coffee.txt

# this is so we can remove files and stuff
import os


# main function
def main():
    found = False
    try:
        # get input, open file (don't use with because there are multiple files)
        search = input("Which coffee do you want to delete: ")
        coffee_file = open("coffee.txt", "r")
        temp_file = open("temp.txt", "w")

        # priming read
        description = coffee_file.readline()
        # loop until the end of the file
        while description != "":
            # convert to float and remove \n
            quantity = float(coffee_file.readline())
            description = description.rstrip("\n")

            # if the we don't find it, just continue writing to temp
            if description != search:
                temp_file.write(description + '\n')
                temp_file.write(str(quantity) + "\n")
            # if we do find it, don't write anything
            # it will not be written to temp when temp gets
            # and the original file will be overwritten
            else:
                found = True

            # read next line
            description = coffee_file.readline()

        # close the files
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

    # if the value in the file cannot be converted to float
    except ValueError:
        print("ERROR: You did not enter a valid quantity. Exiting...")
    # if the file doesn't exist
    except FileNotFoundError:
        print("ERROR: The file could not be found!. Exiting...")
    # if some other file error occurs
    except IOError:
        print("ERROR: The file cannot be accessed (maybe you don't have permission?). Exiting...")
    # if something weird happens
    except:
        print("ERROR: Unknown error occurred. Exiting...")


# call main
main()
