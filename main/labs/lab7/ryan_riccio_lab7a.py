# import modules and make sure they are there
try:
    from tabulate import tabulate
except ImportError:
    print("ERROR: Tabulate module not located. Future errors may occur.")
import json


# main
def main():
    try:
        # welcome message
        print('Hi William! This will convert from imperial units to the metric system.\n'
              f'{"Code by Ryan Riccio":-^69}\n')

        # assign types to lists and assign ranges
        fah_cel_list, mi_km_list, gal_lit_list, lb_kg_list, in_cm_list = [], [], [], [], []
        fah_range, norm_range = range(-10, 101, 10), range(0, 101, 10)

        # pull the data from conversion_data.json, load it to dict
        with open("conversion_data.json", "r") as f:
            conversion_dict = json.load(f)

        # will iter through 5 dictionaries from json
        for dictionary in conversion_dict.values():
            sc = simple_conversion
            d = dictionary
            # for every dict, loop based on given range
            for i in eval(d["Range"]):
                # select list from dict, append list [i of range, returned value from sc]
                # pass to sc: BaseUnit from current dict, i of range (BaseValue), factor from current dict
                eval(d["List"]).append([i, sc(d["BaseUnit"], i, d["Factor"])])
            # print list as table, pull headers from units in current dict
            print(tabulate(eval(d["List"]), headers=(d["BaseUnit"].upper(), d["ConvUnit"].upper()),
                           tablefmt="psql", numalign="right", floatfmt=".2f"))
            input("Press enter to continue...")
        # goodbye user
        print("\nThanks William for using my program! See ya later!")
    except FileNotFoundError:
        print("ERROR: conversion_data.json not found. Exiting...")
    except IOError:
        print("ERROR: File read error. Exiting...")
    except:
        print("ERROR: Unknown error occurred. Exiting...")


# for conversions
def simple_conversion(base_unit, base_value, factor=0):
    # if fah, do different conversion
    if base_unit == "fahrenheit":
        return (base_value - 32) * 5 / 9
    # else return normal conversion
    else:
        return base_value * factor


# call main
main()
