import metric_conversion as mc


# display welcome message
print('Hi William! This will convert from imperial units to the metric system.\n'
      "Just put in the value that you want, and then hit enter! It's simple!\n"
      f'{"Code by Ryan Riccio":-^69}\n')


# main
def main():
    # all functions return bool. if they return false, do not continue
    # this also passes in the label and type of unit
    if mc.miles_to_km('miles', 'kilometers'):
        if mc.fah_to_cel('degrees fahrenheit', 'celsius'):
            if mc.gal_to_lit('gallons', 'liters'):
                if mc.pounds_to_kg('pounds', 'kilograms'):
                    if mc.inches_to_cm('inches', 'centimeters'):
                        print('\nThanks William for using the program! Exiting...')


# call main()
main()
