def convert(base_unit, conversion_unit, factor, name):
    # boolean to determine if the loop is complete
    # and if the input was valid
    success = False

    # register to see if too many errors were made
    count = 0

    # give values to the variables to prevent
    # issues when they have not been declared yet
    base_string = ''
    base_value = 0

    # loop as long as the loop isn't successful or the
    # number of errors is less than 3
    while not success and count < 3:
        # valid bool to validate user input
        valid = False
        # if the interpreter returns an error in the conversion to float
        # try to get the data again
        while not valid:
            try:
                # store as base string and base value to avoid formatting the user input
                base_string = input(f'{name[0]}, please enter the number of {base_unit}: ')
                base_value = float(base_string)

                # exit loop
                valid = True
            # ValueError is thrown when base_string cannot be converted to float
            except ValueError:
                print('ERROR! Please enter a numerical value!\n')

        # if the conversion is for fahrenheit, check with those rules
        if base_unit == 'degrees fahrenheit':
            # if it is > 1000, add to the register, print error, and loop again
            if base_value > 1000:
                count += 1
                print('ERROR! The value cannot be over 1000!\n')
            else:
                success = True
                conversion_value = (base_value - 32) * 5 / 9
                print(f'Hey {name[0]}! {base_string}\xb0F is equal to {conversion_value:,.2f}\xb0C.\n')
        # if it is not fahrenheit, calculate like normal
        else:
            # if it is negative, add to the register, print error, and loop again
            if base_value < 0:
                count += 1
                print('ERROR! The value cannot be negative!\n')
            else:
                # success! we can exit the loop and convert the units then display
                success = True
                conversion_value = base_value * factor
                print(f'Hey {name[0]}! {base_string} {base_unit} is equal to {conversion_value:,.2f} '
                      f'{conversion_unit}.\n')

    # if the count ever hits 3, the loop will stop, and success will never equal true
    if not success:
        print('ERROR! You entered too many incorrect values. Exiting...')

    # return true or false based on whether we did the conversion or not
    return success


# functions to pass in, conversion factor, and to call from main
# it also prints the label
def miles_to_km(miles, kilometers, name):
    print(f'{"***MILES TO KILOMETERS***":^69}')
    return convert(miles, kilometers, 1.6, name)


def fah_to_cel(fah, cel, name):
    print(f'{"***FAHRENHEIT TO CELSIUS***":^69}')
    return convert(fah, cel, 0, name)


def gal_to_lit(gallons, liters, name):
    print(f'{"***GALLONS TO LITERS***":^69}')
    return convert(gallons, liters, 3.9, name)


def pounds_to_kg(pounds, kilograms, name):
    print(f'{"***POUNDS TO KILOGRAMS***":^69}')
    return convert(pounds, kilograms, 0.45, name)


def inches_to_cm(inches, centimeters, name):
    print(f'{"***INCHES TO CENTIMETERS***":^69}')
    return convert(inches, centimeters, 2.54, name)


# display welcome message
print('Hello! This will convert from imperial units to the metric system.\n'
      "Just put in the value that you want, and then hit enter! It's simple!\n"
      f'{"Code by Ryan Riccio":-^69}\n')


# main
def main():
    # all functions return bool. if they return false, do not continue
    # this also passes in the label and type of unit
    name, email = get_name_and_email()
    print("")
    if miles_to_km('miles', 'kilometers', name):
        if fah_to_cel('degrees fahrenheit', 'celsius', name):
            if gal_to_lit('gallons', 'liters', name):
                if pounds_to_kg('pounds', 'kilograms', name):
                    if inches_to_cm('inches', 'centimeters', name):
                        print(f'\nThanks for using the program {" ".join(name)}! Goodbye...')


def get_name_and_email():
    # get name and convert to format "Xxxxxx Xxxxxx"
    name = input("Enter your name: ").title()
    # split first name and last name
    split_name = name.split()
    valid = False
    # loop until valid email, then return
    while not valid:
        email = input("Enter your email: ")
        if "@" not in email:
            print(f"{split_name[0]}, you did not enter a valid email address.")
        else:
            return split_name, email


# call main()
main()
