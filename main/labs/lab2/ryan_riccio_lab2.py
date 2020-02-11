"""
    note:
    all input is stored as 2 data types, a str (*_str) and a float (*)
    this is so that after the computation is complete, the original
    exact user input can be showed when answer is displayed

    show welcome message

    convert miles to kilometers:
    print unit message and center, then new line
    get user input and write to a variable (miles_str)
    convert to float to support decimal precision as input (miles)
    perform operation (*1.6) and write to new variable (kilometers)
    print and format answer to fixed point notation of 2 points
    as well as use the thousands separator ('{:,.2f}'.format())
    print new line

    convert fahrenheit to celsius:
    print unit message and center, then new line
    get user input and write to a variable (fahrenheit_str)
    convert to float to support decimal precision as input (fahrenheit)
    perform operation ((F-32)*5/9) and write to new variable (celsius)
    print and format answer to fixed point notation of 2 points
    as well as use the thousands separator ('{:,.2f}'.format())
    print new line

    convert gallons to liters:
    print unit message and center, then new line
    get user input and write to a variable (gallons_str)
    convert to float to support decimal precision as input (gallons)
    perform operation (*3.9) and write to new variable (liters)
    print and format answer to fixed point notation of 2 points
    as well as use the thousands separator ('{:,.2f}'.format())
    print new line

    convert pounds to kilograms:
    print unit message and center, then new line
    get user input and write to a variable (pounds_str)
    convert to float to support decimal precision as input (pounds)
    perform operation (*0.45) and write to new variable (kilograms)
    print and format answer to fixed point notation of 2 points
    as well as use the thousands separator ('{:,.2f}'.format())
    print new line

    convert inches to centimeters:
    print unit message and center, then new line
    get user input and write to a variable (inches_str)
    convert to float to support decimal precision as input (inches)
    perform operation (*2.54) and write to new variable (centimeters)
    print and format answer to fixed point notation of 2 points
    as well as use the thousands separator ('{:,.2f}'.format())
    print new lines

    say goodbye to our amazing user

    Here are the python 3 docs on the format() function:
    https://docs.python.org/3/library/string.html#format-specification-mini-language
"""

# display welcome message
print('Hi! This program will convert from imperial units to the metric system.\n'
      "Just put in the value that you want, and then hit enter! It's simple!\n"
      '{:-^69}\n'.format(' Code by Ryan Riccio '))


# ***convert miles to kilometers***
print('{:^69}'.format('***MILES TO KILOMETERS***'))

# ask for user input (float handles decimal input), compute
miles_str = input('Enter the distance in miles: ')
miles = float(miles_str)
kilometers = miles * 1.6

# print data, separate thousands, convert to fixed point
print('{} miles is equal to {:,.2f} kilometers.\n'.format(miles_str, kilometers))


# ***convert f to c***
print('{:^69}'.format('***FAHRENHEIT TO CELSIUS***'))

# ask for user input (float handles decimal input), compute
fahrenheit_str = input('Enter the degrees in Fahrenheit: ')
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit - 32) * 5 / 9

# print data, separate thousands, convert to fixed point
print('{}\xb0F is equal to {:,.2f}\xb0C.\n'.format(fahrenheit_str, celsius))


# ***convert gallons to L***
print('{:^69}'.format('***GALLONS TO LITERS***'))

# ask for user input (float handles decimal input), compute
gallons_str = input('Enter the amount of gallons: ')
gallons = float(gallons_str)
liters = gallons * 3.9

# print data, separate thousands, convert to fixed point
print('{} gallons is equal to {:,.2f} liters.\n'.format(gallons_str, liters))


# ***convert pounds to kilograms***
print('{:^69}'.format('***POUNDS TO KILOGRAMS***'))

# ask for user input (float handles decimal input), compute
pounds_str = input('Enter the weight in pounds: ')
pounds = float(pounds_str)
kilograms = pounds * 0.45

# print data, separate thousands, convert to fixed point
print('{} pounds is equal to {:,.2f} kilograms.\n'.format(pounds_str, kilograms))


# ***convert in to centimeters***
print('{:^69}'.format('***INCHES TO CENTIMETERS***'))

# ask for user input (float handles decimal input), compute
inches_str = input('Enter the length in inches: ')
inches = float(inches_str)
centimeters = inches * 2.54

# print data, separate thousands, convert to fixed point
print('{} inches is equal to {:,.2f} centimeters.\n\n'.format(inches_str, centimeters))


# say goodbye
print('Thanks for using the program! Hope it worked well!\n\n')
