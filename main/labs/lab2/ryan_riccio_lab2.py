"""
    show welcome message

    convert mi to km:
    get user input and write to a variable (mi)
    store as float to support decimal precision as input
    perform operation (*1.6) and write to new variable (km)
    remove extra decimals and truncate to a precision of 2
    print and format data while removing trailing zeros (see note)

    convert f to c:
    get user input and write to a variable (fahrenheit)
    store as float to support decimal precision as input
    perform operation ((F-32)*5/9) and write to new variable (celsius)
    remove extra decimals and truncate to a precision of 2
    print and format data while removing trailing zeros (see note)

    convert gal to L:
    get user input and write to a variable (gal)
    store as float to support decimal precision as input
    perform operation (*3.9) and write to new variable (liters)
    remove extra decimals and truncate to a precision of 2
    print and format data while removing trailing zeros (see note)

    convert lb to kg:
    get user input and write to a variable (lb)
    store as float to support decimal precision as input
    perform operation (*0.45) and write to new variable (kg)
    remove extra decimals and truncate to a precision of 2
    print and format data while removing trailing zeros (see note)

    convert in to cm:
    get user input and write to a variable (inches)
    store as float to support decimal precision as input
    perform operation (*2.54) and write to new variable (cm)
    remove extra decimals and truncate to a precision of 2
    print and format data while removing trailing zeros (see note)

    say goodbye to our amazing user

    NOTE: I noticed that when a user inputs an integer number, and it
    gets converted to a float, it adds extra trailing zeros. For example
    an input of 100 would be displayed as either 100.0 or 100.00 depending
    on the desired fixed point. To fix this while still using functions
    we learned in class, I looked up the Python documentation of the
    format() function. I then realized that one of the arguments could
    be used to get rid of trailing zeros, however it could not be used
    with fixed-point notation ('.2f'). To counter this, for all of the
    input, before I display it, I get rid of the extra precision, which
    is returned as a str, so I convert it back to a float, and then
    used format() again to get rid of any trailing, non-placeholder zeros
    if there were any. It also uses the ',' thousands separator. Here are
    the python 3 docs on the format() function:
    https://docs.python.org/3/library/string.html#format-specification-mini-language
    ALSO, I know were are not supposed to use short variable names, but
    since this is a conversion program and all of the units have universal
    abbreviations, I will try to use those instead.
"""

# display welcome message
print('Hi! This program will convert from imperial units to the metric system.\n'
      "Just put in the value that you want, and then hit enter! It's simple!\n"
      '{:-^69}\n'.format(' Code by Ryan Riccio '))

# convert mi to km
print('{:^69}'.format('***MILES TO KILOMETERS***'))

# ask for user input (use float to handle decimal precision as input), compute conversion
mi = float(input('Enter the distance in miles: '))
km = mi * 1.6

# truncate data
mi = float('{:.2f}'.format(mi))     # format() converts to str, str is converted back to float
km = float('{:.2f}'.format(km))

# print data, remove trailing zeros, and separate thousands
print('{:,g} miles is equal to {:,g} kilometers.\n'.format(mi, km))

# convert f to c
print('{:^69}'.format('***FAHRENHEIT TO CELSIUS***'))

# ask for user input (use float to handle decimal precision as input), compute conversion
fahrenheit = float(input('Enter the degrees in Fahrenheit: '))
celsius = (fahrenheit - 32) * 5 / 9

# truncate data
fahrenheit = float('{:.2f}'.format(fahrenheit))     # format() converts to str, str is converted back to float
celsius = float('{:.2f}'.format(celsius))

# print data, remove trailing zeros, and separate thousands (\xb0 is the hex value of the degree symbol)
print('{:,g}\xb0F is equal to {:,g}\xb0C.\n'.format(fahrenheit, celsius))

# convert gal to L
print('{:^69}'.format('***GALLONS TO LITERS***'))

# ask for user input (use float to handle decimal precision as input), compute conversion
gal = float(input('Enter the amount of gallons: '))
liters = gal * 3.9

# truncate data
gal = float('{:.2f}'.format(gal))     # format() converts to str, str is converted back to float
liters = float('{:.2f}'.format(liters))

# print data, remove trailing zeros, and separate thousands
print('{:,g} gallons is equal to {:,g} liters.\n'.format(gal, liters))

# convert lb to kg
print('{:^69}'.format('***POUNDS TO KILOGRAMS***'))

# ask for user input (use float to handle decimal precision as input), compute conversion
lb = float(input('Enter the weight in pounds: '))
kg = lb * 0.45

# truncate data
lb = float('{:.2f}'.format(lb))     # format() converts to str, str is converted back to float
kg = float('{:.2f}'.format(kg))

# print data, remove trailing zeros, and separate thousands
print('{:,g} pounds is equal to {:,g} kilograms.\n'.format(lb, kg))

# convert in to cm
print('{:^69}'.format('***INCHES TO CENTIMETERS***'))

# ask for user input (use float to handle decimal precision as input), compute conversion
inches = float(input('Enter the length in inches: '))
cm = inches * 2.54

# truncate data
inches = float('{:.2f}'.format(inches))     # format() converts to str, str is converted back to float
cm = float('{:.2f}'.format(cm))

# print data, remove trailing zeros, and separate thousands
print('{:,g} inches is equal to {:,g} centimeters.\n'.format(inches, cm))

