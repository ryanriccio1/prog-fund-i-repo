# import regular expression
import re


# main function
def main():
    # list of months
    month_index_list = ['January',
                        'February',
                        'March',
                        'April',
                        'May',
                        'June',
                        'July',
                        'August',
                        'September',
                        'October',
                        'November',
                        'December']
    # list of months with 31 days
    months_with_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']

    # create vars
    month = ""
    day = ""
    year = ""
    ending = ""

    # validation loop
    valid = False
    while not valid:
        try:
            # get date as string
            raw_date = input("Please enter the date (mm/dd/yy): ")

            # search for correct group and assign matches to groups
            # (***) specifies a group of the search object
            # \d? = zero or one of any digit
            # \d = any digit
            # / = matches "/" literally
            regex_match = re.search(r"(\d?\d)/(\d?\d)/(\d\d)", raw_date)
            # if no match raise exception
            if not regex_match:
                raise RuntimeError("You did not enter a valid date format. Try again.")
            else:
                # assign vars to match groups
                month = regex_match[1]
                day = regex_match[2]
                year = regex_match[3]

            # assign ending to date (1st, 2nd, 3rd, 4th, etc)
            # digits in the 10s always end with "th"
            if not day.startswith("1"):
                if day.endswith("1"):
                    ending = "st"
                elif day.endswith("2"):
                    ending = "nd"
                elif day.endswith("3"):
                    ending = "rd"
            else:
                ending = "th"

            # convert vars to ints
            month = int(month)
            day = int(day)
            year = int(year)

            # validation
            if month > 12 or month < 1:
                raise RuntimeError("The month is not valid. Try again.")
            if day > 31 or day < 1:
                raise RuntimeError("The day is not valid. Try again.")
            if year != 13:
                raise RuntimeError("The year is not valid. Must be 13. Try again.")

            # some months don't have 31 days, make sure to tell the user that
            if month_index_list[month-1] == "February" and day > 28 and year % 4 != 0:
                raise RuntimeError(f"Since 20{year} was not a leap year, the month of February "
                                   f"does not have {day} days.")
            if month_index_list[month-1] not in months_with_31 and day == 31:
                raise RuntimeError(f"There are not {day} days in the month of {month_index_list[month-1]}.")

            # if we get to this point, we are valid, exit the loop
            valid = True
        except RuntimeError as err:
            print(err)
        except ValueError:
            print("You did not enter a valid value")
    # print the date
    print("\nThe date in long string format is:\n"
          f"{month_index_list[month-1]} {day}{ending}, 20{year}")


# just in case we need to put this in a module
if __name__ == '__main__':
    main()
