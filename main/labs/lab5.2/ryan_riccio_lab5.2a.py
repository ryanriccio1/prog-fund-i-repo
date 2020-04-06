import metric_conversion


# display welcome message
print('Hi William! This will convert from imperial units to the metric system.\n'
      "Just put in the value that you want, and then hit enter! It's simple!\n"
      f'{"Code by Ryan Riccio":-^69}\n')


# main
def main():
    # all functions return bool. if they return false, do not continue
    # this also passes in the label and type of unit
    if metric_conversion.miles_to_km('miles', 'kilometers'):
        if metric_conversion.fah_to_cel('degrees fahrenheit', 'celsius'):
            if metric_conversion.gal_to_lit('gallons', 'liters'):
                if metric_conversion.pounds_to_kg('pounds', 'kilograms'):
                    if metric_conversion.inches_to_cm('inches', 'centimeters'):
                        print('\nThanks William for using the program! Exiting...')


# call main()
main()
