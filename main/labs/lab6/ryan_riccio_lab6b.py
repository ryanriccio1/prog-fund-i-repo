# to add wait times
from time import sleep


# main function
def main():
    print("This program will store the average grade for a given student.\n")
    # create empty dictionary
    student_grades = {}
    # if a duplicate name is given, keep a count of how many times
    duplicate_counter = 2
    # main loop to get 12 students' information
    for x in range(12):
        student_grades, duplicate_counter = get_student_info(student_grades, x, duplicate_counter)
        print("")

    try:
        # after all data is gained, write to a file ("with" automatically handles scope
        # and will close the file automatically)
        with open("grades.txt", "w") as file:
            # convert dictionary to string
            file.write(str(student_grades))

        # when the user is ready, read the file
        input("\nPress enter to read data...")

        # open the file in read mode ("with" automatically handles scope
        # and will close the file automatically)
        with open("grades.txt", "r") as file:
            # eval will try to infer the data type (it will be a dictionary)
            new_student_grades = eval(file.read())
            # to loop through dictionary
            for name, grade in new_student_grades.items():
                # go through each character in the string
                # if one of the characters is a digit
                # this assumes that it was a duplicate
                for character in name:
                    if character.isdigit():
                        # remove all appended digits
                        # after the "." (appended in get_student_info())
                        name = name.split(".", 1)
                        name = name[0]
                # print data and wait .25 seconds before showing the next one
                print(f"Name: {name}\nGrade: {grade:,.2f}%\n")
                # give the user a bit of time to read data
                sleep(.25)
    # except file errors
    except FileNotFoundError:
        print("ERROR: File is no where to be seen!")
    # FileNotFoundError is a subclass of IOError, so if the file is not found,
    # IOError will never have to be excepted
    except IOError:
        print("ERROR: An unknown file error has occurred!")

    # wait for user input to quit
    input("\nPress enter to quit...")


# main function to get student info
def get_student_info(student_dict, iteration, duplicate_counter):
    # print the index number and as for student name
    student_name = input(f"(#{iteration+1}) Student Name: ")
    # if there's any extra spaces at the end, get rid of it
    student_name = student_name.rstrip(" ")
    # default value for grade
    student_grade = 0

    # input validation loop
    valid = False
    while not valid:
        try:
            # get grade
            student_grade = float(input("Average Grade: "))
            # if not a valid input, raise error
            if not 0 <= student_grade <= 100.0:
                raise ValueError()
            else:
                valid = True
        # if the grade cannot be converted to float,
        # or it is not in range, except and print message
        except ValueError:
            print("\nPlease enter a valid grade.")
            valid = False
    # if the given name is already in the dictionary
    if student_name in student_dict:
        # add a "." and then a number to prevent data from being
        # overwritten (gets removed when data is read back)
        # the value of duplicate counter does not matter
        # as long as it is different from the last identical name
        student_name = student_name + f".{duplicate_counter}"
        duplicate_counter += 1
    # assign the grade to the name
    student_dict[student_name] = student_grade
    return student_dict, duplicate_counter


# call main
main()
