# display welcome message
print('Hi William! This will convert from imperial units to the metric system.\n'
      "Just put in the value that you want, and then hit enter! It's simple!\n"
      f'{"Code by Ryan Riccio":-^69}\n')

# ***convert miles to kilometers***
print(f'{"***MILES TO KILOMETERS***":^69}')

# ask for user input (float handles decimal input)
miles_str = input('William, please enter the distance in miles: ')
miles = float(miles_str)

# check to make sure it is not negative
if miles > 0:
    # compute
    kilometers = miles * 1.6

    # print data, separate thousands, convert to fixed point
    print(f'Hey William! {miles_str} miles is equal to {kilometers:,.2f} kilometers. Nice!\n')

    # ***convert f to c***
    print(f'{"***FAHRENHEIT TO CELSIUS***":^69}')

    # ask for user input (float handles decimal input)
    fahrenheit_str = input('William, please enter the degrees in Fahrenheit: ')
    fahrenheit = float(fahrenheit_str)
    # check to make sure it is not over 1000
    if fahrenheit <= 1000:
        # compute
        celsius = (fahrenheit - 32) * 5 / 9

        # print data, separate thousands, convert to fixed point
        print(f"Hey William! {fahrenheit_str}\xb0F is equal to {celsius:,.2f}\xb0C. Awesome!\n")

        # ***convert gallons to L***
        print(f'{"***GALLONS TO LITERS***":^69}')

        # ask for user input (float handles decimal input)
        gallons_str = input('William, please enter the amount of gallons: ')
        gallons = float(gallons_str)
        # check to make sure it is not negative
        if gallons > 0:
            # compute
            liters = gallons * 3.9

            # print data, separate thousands, convert to fixed point
            print(f'Hey William! {gallons_str} gallons is equal to {liters:,.2f} liters. Rad!\n')

            # ***convert pounds to kilograms***
            print(f'{"***POUNDS TO KILOGRAMS***":^69}')

            # ask for user input (float handles decimal input)
            pounds_str = input('William, please enter the weight in pounds: ')
            pounds = float(pounds_str)
            # check to make sure it is not negative
            if pounds > 0:
                # compute
                kilograms = pounds * 0.45

                # print data, separate thousands, convert to fixed point
                print(f'Hey William! {pounds_str} pounds is equal to {kilograms:,.2f} kilograms. Sweet!\n')

                # ***convert in to centimeters***
                print(f'{"***INCHES TO CENTIMETERS***":^69}')

                # ask for user input (float handles decimal input)
                inches_str = input('William, please enter the length in inches: ')
                inches = float(inches_str)
                # check to make sure it is not negative
                if inches > 0:
                    # compute
                    centimeters = inches * 2.54

                    # print data, separate thousands, convert to fixed point
                    print(f'Hey William! {inches_str} inches is equal to {centimeters:,.2f} centimeters. Cool!\n\n')

                    # say goodbye
                    print('Thanks for using the program! Hope it worked well!\n\n')

                # if inches is negative
                else:
                    print('Error! You entered a negative value! Exiting...')

            # if pounds is negative
            else:
                print('Error! You entered a negative value! Exiting...')

        # if gallons is negative
        else:
            print('Error! You entered a negative value! Exiting...')

    # if fahrenheit is greater than 1000
    else:
        print('Error! You entered a value over 1000\xb0F! Exiting...')

# if miles is negative
else:
    print('Error! You entered a negative value! Exiting...')
