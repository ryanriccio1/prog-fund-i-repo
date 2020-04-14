# module to format tables (module is included in directory)
# !!!NOT A CUSTOM MODULE!!! just one I use all the time
# and I wanted the data to look nice...
# if you want to install it "pip install tabulate"
# tabulate is an MIT Licensed module, meaning it is open source
# so I feel like I should be able to use it for this homework
# but if whoever is grading this disagrees, I'd totally be willing
# to remove it, it just wouldn't look as pretty.
from tabulate import tabulate


# main function
def main():
    try:
        # the dictionary written to the file on initialization
        default_dict = {"Blonde Roast": 15,
                        "Medium Roast": 21,
                        "Flavored Roast": 10,
                        "Dark Roast": 12,
                        "Costa Rica Tarrazu": 18}
        # the entries that need to be added after first time data is displayed
        addfile_dict = {"Guatemala Antigua": 22,
                        "House Blend": 25,
                        "Decaf House Blend": 16}

        # write the default dictionary to a file, read them back, and store to dict
        access_coffee_inventory("w", dictionary=default_dict)
        dict_from_file = access_coffee_inventory()

        # display dictionary that was read from file
        print(tabulate(dict_from_file.items(), headers=["Type", "Pounds"], tablefmt="psql"))

        input("\nPress enter to add new entries...")

        # add the new entries to the dictionary and write
        dict_from_file.update(addfile_dict)
        access_coffee_inventory("w", dictionary=dict_from_file)

        # print the dictionary with the new entries from addfile_dict
        print(tabulate(dict_from_file.items(), headers=["Type", "Pounds"], tablefmt="psql"))

        # input validation loop to remove entries
        looping = True
        while looping:
            # get the input and convert to title() (xxxxx xxxx -> Xxxxx Xxxx)
            file_to_remove = input("\nPlease enter the type of the coffee you "
                                   "want to remove (or enter to exit): ").title()
            # if the user didn't enter anything, assume they want to leave
            if file_to_remove == "":
                looping = False
            # if we find the input in the dict
            elif file_to_remove in dict_from_file.keys():
                # remove coffee from dict, re-compute total, write to file
                dict_from_file.pop(file_to_remove)
                dict_from_file = add_total(dict_from_file)
                access_coffee_inventory("w", dict_from_file)
                print("\nRemoving Coffee...\n")
                # get the new key
                key_to_add = input("Please enter the type of coffee you "
                                   "want to add (or enter to exit): ").title()
                # if the user didn't enter anything, assume they want to leave
                if key_to_add == "":
                    looping = False
                else:
                    # get the weight in pounds and write it to dict
                    value_to_add = int(input("Please enter the quantity in pounds of that coffee: "))
                    dict_from_file[key_to_add] = value_to_add
                    # compute new total, write to file
                    dict_from_file = add_total(dict_from_file)
                    access_coffee_inventory("w", dict_from_file)
                    # print updated table
                    print(tabulate(dict_from_file.items(), headers=["Type", "Pounds"], tablefmt="psql"))
            # if we cannot find the user's input in the dict
            else:
                print("ERROR: That item was not found in the file.. Exiting...")
                looping = False
        # no matter what happens, thank the user for being a good user (hopefully)
        print("Thanks for using the program! Goodbye!")

    # if the file isn't found
    except FileNotFoundError:
        print("ERROR: The file has not been found. Exiting...")
    # if a bad value is inputted and cannot be parsed
    except ValueError:
        print("ERROR: You entered an invalid value. Exiting...")
    # if some weird file error happens that doesn't include the file not existing
    except IOError:
        print("ERROR: File read/write error (maybe you don't have permission). Exiting...")
    # and if something weird happens
    except RuntimeError:
        print("ERROR: Runtime Error. Exiting...")
    # and if something weirder happens
    except:
        print("ERROR: Unknown error. Exiting...")


# function that adds the total of all of the coffee entries
def add_total(dictionary):
    # the base longest string length
    longest_str = 0
    # loop through all the dict keys
    for key in dictionary.keys():
        # find the length of the longest key
        str_len = len(key)
        if str_len > longest_str:
            longest_str = str_len
    # use list otherwise error will occur when key gets popped mid iteration
    # python does not like the dict size to change during a for loop
    for keys in list(dictionary):
        # remove the old total
        if "Total" in keys:
            dictionary.pop(keys)
    # add the new total centered between dashes
    # the number of dashed is based on the longest string
    total_text_key = 'Total'.center(longest_str, "-")
    # sum all of the values
    total = sum(dictionary.values())
    # add to dict and return
    dictionary[total_text_key] = total
    return dictionary


def access_coffee_inventory(func="r", dictionary=None):
    # just in case someone forgets
    # to specify a dictionary (which should never happen)
    if dictionary is None:
        dictionary = {}
    # to read data
    if func == "r":
        # open in read mode ("with" will automatically close after)
        with open("coffeeInventory.txt", "r") as file:
            # eval will try to infer the data type (it will be a dictionary)
            dictionary = eval(file.read())
            # send it back
            return dictionary
    # to write data
    elif func == "w":
        # open in write mode ("with" will automatically close after)
        with open("coffeeInventory.txt", "w") as file:
            # add the total and append to dict
            dictionary = add_total(dictionary)
            # convert dict to string and write
            file.write(str(dictionary))


# call main
main()
