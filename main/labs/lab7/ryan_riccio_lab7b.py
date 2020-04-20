# main function
def main():
    try:
        # welcome message
        print("Hello Professor Polanco, please enter the names of your students to keep"
              "track of them.\n")

        # main variables
        amount_students = 12
        instructor = "Professor Polanco"
        my_name = "Ryan Riccio"
        file_name = "names.txt"

        # get list of students
        student_list = get_names(amount_students)

        # alphabetize and reverse order
        student_list.sort()
        student_list.reverse()

        # add values to list
        student_list.append(instructor)
        student_list.insert(0, my_name)

        # save to file, and display
        save_file(student_list, file_name)
        input("Press enter to view contents of names.txt...")
        display_file(file_name)

        # convert to tuple
        new_tuple = tuple(student_list)
    except FileNotFoundError:
        print("ERROR: names.txt not found. Exiting...")
    except IOError:
        print("ERROR: File error occurred. Exiting...")
    except ValueError:
        print("ERROR: There was an invalid value parsed. Exiting...")
    except IndexError:
        print("ERROR: There was an error with the list. Exiting...")


# to get names
def get_names(num=12):
    # create list
    student_list = []
    for i in range(num):
        # get name and append for each loop
        current_name = input(f"({i+1}) Enter the student's name: ")
        student_list.append(current_name)
    # return list
    return student_list


# to save list to file
def save_file(src_list, file_name):
    # open file
    with open(file_name, "w") as file:
        # append \n with each iteration while writing each index as line
        file.writelines("\n".join(src_list))


# to display list from file
def display_file(file_name):
    # open file
    with open(file_name, "r") as file:
        # for each iteration, strip and print line
        [print("#{0}: {1}".format(i+1, record.rstrip('\n'))) for i, record in enumerate(file)]


# call main
main()
