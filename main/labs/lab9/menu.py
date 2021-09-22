# to print menus
def print_menu(menu_dict):
    # loop through menu keys and items
    for key, value in menu_dict.items():
        # key is menu selection letter, value[0] is the name
        print(f"{key}. {value[0].upper()}")

    # get the menu selection
    menu_selection = input("Enter your selection: ").lower()

    # if we can find the selection
    if menu_selection in menu_dict:
        print("")
        # run the method defined in menu values, loop and unpack args from list in dictionary values
        # return value from function (either True or False)
        return menu_dict[menu_selection][1](*[menu_dict[menu_selection][2][i] for i, _ in
                                              enumerate(menu_dict[menu_selection][2])])

    # if the menu option is incorrect, raise the exception
    else:
        raise RuntimeError(f"ERROR: The input '{menu_selection}' is not valid.\n")
