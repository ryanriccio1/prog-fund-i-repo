# import datetime to give file write a time stamp
from datetime import datetime


# custom Exception
class IncorrectEntryException(BaseException):
    # when the Exception gets thrown (can take in any number of positional
    # arguments (as tuple) or any number of keyword arguments (as dictionary)
    def __init__(self, *args, **kwargs):
        # if positional args exist
        if args:
            # the error message is the arg in the first (0th) position
            error_message = args[0]
            # if one of the kwargs is not "print_verbose"
            # print the simple error message from args[0]
            if "print_verbose" not in kwargs.keys():
                print(error_message)
        # if the key "reason" exists in kwargs
        elif "reason" in kwargs.keys():
            # error message assigned to the value of reason
            error_message = kwargs["reason"]
            # if one of the kwargs is not "print_verbose"
            # print the simple error message from "reason"
            if "print_verbose" not in kwargs.keys():
                print(error_message)
        # if no arg or kwarg that equals reason, no error message
        # has been passed, do not print, set default error
        else:
            error_message = "Incorrect information has been entered."

        # console error is what gets sent to the traceback
        self.console_error = f"IncorrectEntryException has been raised. REASON: {error_message}"
        # if it is specified to print the verbose Exception message, print the console error
        if "print_verbose" in kwargs.keys():
            if kwargs["print_verbose"] is True:
                print(self.console_error)

    # when the console needs to print a traceback or return the error message
    def __str__(self):
        # returns to traceback or when Exception is excepted to var (except Exception as err)
        return self.console_error


# custom Exception
class TooManyTriesError(BaseException):
    # when the Exception gets thrown (can only take in 1 argument)
    def __init__(self, error_str):
        # exception will always print pre-defined error message
        self.error_string = error_str
        print(self.error_string)

    # when the console needs to print a traceback or return the error message
    def __str__(self):
        return self.error_string


# main conversion function
def convert(base_unit, conversion_unit, factor, filecount):
    # print and center label using units passed from menu
    format_string_len = len(base_unit + conversion_unit) + 55
    print(f"***{base_unit.upper()} TO {conversion_unit.upper()}***".center(format_string_len))

    # set default starting values for all vars
    success = False
    count = 0

    base_string = ""
    base_value = 0
    conversion_value = 0

    # main input validation loop, ends after 3 mistakes (invalid numbers do not count)
    while not success and count < 3:
        try:
            # if the conversion is for fahrenheit, check with those rules
            if base_unit == "fahrenheit":
                # get input, store as separate string to prevent converting user data to float
                # and thus adding extra zeros the user did not enter
                base_string = input(f"(#{filecount}) William, please enter the number of degrees {base_unit}: ")
                base_value = float(base_string)
                # if user input is > 1000, add to the register, raise exception, print error, and loop again
                if base_value > 1000:
                    count += 1
                    # exception gets accepted in the loop, will print error message
                    raise IncorrectEntryException("ERROR! The value cannot be over 1000!\n")
                # if the input matches our rules
                else:
                    success = True
                    # do the math
                    conversion_value = (base_value - 32) * 5 / 9
                    # change the units to be °F & °C (° = unicode b0)
                    base_unit = "\xb0F"
                    conversion_unit = "\xb0C"
            # if it is not fahrenheit, calculate like normal using conversion_factor
            else:
                # get input, store as separate string to prevent converting user data to float
                # and thus adding extra zeros the user did not enter
                base_string = input(f"(#{filecount}) William, please enter the number of degrees {base_unit}: ")
                base_value = float(base_string)
                # if user input is negative, add to the register, raise exception, print error, and loop again
                if base_value < 0:
                    count += 1
                    # exception gets accepted in the loop, will print error message
                    raise IncorrectEntryException("ERROR! The value cannot be negative!\n")
                # if the input matches our rules
                else:
                    success = True
                    # do the math
                    conversion_value = base_value * factor

        # for when an out of range value is entered
        except IncorrectEntryException:
            success = False
        # for when a value cannot be converted to float
        except ValueError:
            success = False
            print("You entered an invalid number.\n")

    # if the count ever hits 3, the loop will stop, and success will never equal true
    if not success:
        # raise error that gets excepted from ryan_riccio_lab6a.py/main()
        raise TooManyTriesError("ERROR! You entered too many incorrect values. Exiting...")
    else:
        # print the outcome of the conversion and write it to a file
        print(f"Hey William! {base_string} {base_unit} is equal to {conversion_value:,.2f} {conversion_unit}.\n")
        save_to_file(base_value, base_unit, conversion_value, conversion_unit, filecount=filecount)

    # return true or false based on whether we did the conversion or not
    return success


# to show menu and call convert()
def show_menu(filecount):
    # dictionary to store menu options and values for convert()
    # the values are stored in a list in a dictionary
    menu_dict = {"a": ["miles", "kilometers", 1.6],
                 "b": ["fahrenheit", "celsius", 0],
                 "c": ["gallons", "liters", 3.9],
                 "d": ["pounds", "kilograms", 0.45],
                 "e": ["inches", "centimeters", 2.54]}

    # loop to print menu
    for key, value in menu_dict.items():
        print(f"{key}. {value[0].upper()} TO {value[1].upper()}")

    # input validation loop
    success = False
    while not success:
        # convert input to lowercase so the chances of it matching
        # the dictionary values are higher
        menu_selection = input("Enter your selection: ").lower()
        if menu_selection in menu_dict:
            print("")
            # pull values from dictionary based on selection
            md = menu_dict[menu_selection]
            # pull values from list based on position
            success = convert(md[0], md[1], md[2], filecount)
        # if the user enters in a value not in the dictionary keys
        else:
            # raise an error that gets accepted in ryan_riccio_lab6a.py/main()
            raise IncorrectEntryException(f"\nThe input '{menu_selection}' is not valid.")


# does what the name suggests, saves to file
def save_to_file(base_value=0, base_unit="", conversion_value=0,
                 conversion_unit="", close=False, filecount=0, reason=""):
    # assign the datetime object to a better variable name
    current_dt = datetime.now()
    # do not use "with" because file will remain open for all of program (until exit)
    save_file = open("conversions.txt", "a")

    # file will be closed via function call, not at end of write()
    if close is True:
        # print the EOF message and close
        save_file.write(f"\n\n\n[ EOF AT {current_dt.strftime('%m/%d/%Y %H:%M:%S')} "
                        f"REASON: {reason} ]\n")
        save_file.close()
    else:
        # write data from function call
        save_file.write(f"[ #{filecount} {base_unit.upper()} TO {conversion_unit.upper()} "
                        f"{current_dt.strftime('%m/%d/%Y %H:%M:%S')} ]\n")
        save_file.write(f"I:\t{base_value:,.2f}\t{base_unit}\n"
                        f"O:\t{conversion_value:,.2f}\t{conversion_unit}\n\n")
