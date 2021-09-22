# import modules
from tabulate import tabulate
from time import sleep
import student_data
import menu


# main function
def main():
    print('Welcome to the Student Manager!\n')
    # to stop menu loop
    is_running = True

    # roster to contain student objects
    roster = student_data.Roster()

    # dict with menu options, menu option title, menu option method, and args
    menu_dict = {
        "a": ["look up student", display_one_student, [roster]],
        "b": ["add student", add_student, [roster]],
        "c": ["edit student gpa", edit_gpa, [roster]],
        "d": ["edit expected grade", edit_grade, [roster]],
        "e": ["print student data", display_all_students, [roster]],
        "f": ["quit", exit_sequence, [roster]]
    }

    # add 5 default students (don't you just love random name generator?)
    # roster.add_student_entry creates a new Student object and stores it in the Roster class
    roster.add_student_entry("Ryan Riccio", 2059123, 3.98, 100.0)
    roster.add_student_entry("John Smith", 2089325, 4.00, 99.8)
    roster.add_student_entry("Davis Reinert", 2172349, 3.01, 97.6)
    roster.add_student_entry("Dave Larmon", 2781234, 2.99, 86.5, full_time=False)
    roster.add_student_entry("Bryce Mease", 2824322, 4.21, 96.21)

    # main loop
    while is_running:
        try:
            # all menu methods return True except for exit_sequence
            # print the menu based off the dict we created earlier
            is_running = menu.print_menu(menu_dict)
        # if there's an error, display it and tell us why it's and error
        except RuntimeError as err:
            print(err)


# takes in the roster object, searches Student objects
def search_student(roster):
    # get name or id to search for
    name_or_id = input("Enter a name or id: ")
    # find_student method
    student = roster.find_student(name_or_id)
    # if the student isn't found
    if student is None:
        print("No student was found.")
    # return either student or None
    return student


# will print the data of an individual student
def print_student(student):
    # data() returns a dict of first and last names, and the rest of the student data
    name, data = student.data()
    # print table - headers are the first dict, data.items() is the data
    print(tabulate(data.items(), headers=('First\nLast', f'{name["First"]}\n{name["Last"]}'), tablefmt='psql',
                   floatfmt='.2f', colalign=('left', 'right'), disable_numparse=True))


# display single student
def display_one_student(roster):
    # find the student, print the student in tabular format
    student = search_student(roster)
    if student is not None:
        print_student(student)
    # return True (to continue menu loop)
    return True


# loop through and display all students
def display_all_students(roster):
    # loop through each Student object
    for student in roster.students:
        # print each student
        print_student(student)
        sleep(.3)
        print("")
    # return True (to continue menu loop)
    return True


# add single student to roster
def add_student(roster):
    # input validation loop
    valid = False
    while not valid:
        try:
            # when creating a new student, get the new info
            name = input("Enter the student name: ")
            uid = input("Enter the student id: ")
            gpa = input("Enter the student's GPA: ")
            grade = input("Enter the student's expected grade: ")
            full_time = input("Is the student full time? (t/f): ")
            # get the first char as lower()
            if full_time[0].lower() == 't':
                full_time = True
            elif full_time[0].lower() == 'f':
                full_time = False
            else:
                raise RuntimeError('ERROR: T/F for full time not valid.\n')
            # add new student to roster
            roster.add_student_entry(name, uid, gpa, grade, full_time)
            valid = True
        except RuntimeError as err:
            print(err)
    # return True (to continue menu loop)
    return True


def edit_gpa(roster):
    # find student
    student = search_student(roster)

    # if the student exists
    if student is not None:
        valid = False
        while not valid:
            # set the gpa
            try:
                student.gpa = input(f"Enter a new gpa for {student.name} (current={student.gpa}): ")
                valid = True
            except RuntimeError as err:
                print(err)
    # return True (to continue menu loop)
    return True


def edit_grade(roster):
    # find student
    student = search_student(roster)

    # if student exists
    if student is not None:
        valid = False
        while not valid:
            # set the grade
            try:
                student.grade = input(f"Enter a new grade for {student.name} (current={student.grade}%): ")
                valid = True
            except RuntimeError as err:
                print(err)
    # return True (to continue menu loop)
    return True


# tasks to complete before we finish
def exit_sequence(roster):
    # write to a log for debugging and records
    with open('students.log', 'w') as f:
        for student in roster.students:
            f.write(str(student.data()))
            f.write('\n')
    # say bye
    print('Thank you! Goodbye!')
    # return False (to end menu loop)
    return False


# make sure we are main
if __name__ == '__main__':
    main()
