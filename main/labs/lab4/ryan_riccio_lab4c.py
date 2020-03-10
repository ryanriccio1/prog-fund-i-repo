def get_letter_grade(score):
    # returns letter grade based on score
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def main():
    # print welcome message and instructions
    print('This program will calculate grades for the class'
          '\nEnter -1 in the score field to continue to next student'
          '\nAfter any input, please press enter.\n')

    # declare initial variables
    num_of_students = 0
    score = 0
    class_score = 0
    class_tests = 0

    # input validation loop to prevent bad data
    valid = False
    while not valid:
        try:
            # exit if conversion is good
            num_of_students = int(input('How many students are in the class: '))
            valid = True
        # a ValueError is thrown if the str cannot become float
        except ValueError:
            print('ERROR! Please enter a numeric value')

    # loop based on number of students
    for student in range(num_of_students):
        print(f'\nStudent {student + 1}\n'
              '---------')

        # reset student variable
        more_tests = True
        student_score = 0
        student_tests = 0
        average_student_score = 0

        # keep looping as long as there are more tests
        while more_tests:
            # validate input to prevent letters and erroring out
            test_score_valid = False
            while not test_score_valid:
                try:
                    score = float(input(f'Score for test {student_tests+1}: '))
                    test_score_valid = True
                except ValueError:
                    print('ERROR! Please enter a numeric value')

            # if they put a negative number in, exit loop, go to next student
            if score < 0:
                # if they enter no data, if gives a ZeroDivisionError
                try:
                    average_student_score = student_score / student_tests
                except ZeroDivisionError:
                    average_student_score = 0
                more_tests = False
            else:
                # add total student score, and divide by number of student tests to find
                # average score for student
                student_score += score
                student_tests += 1
                average_student_score = student_score / student_tests

                # print percent and letter grade for current test
                print(f'{score}% = {get_letter_grade(score)}')

                # increase class index and class total score for average
                class_score += score
                class_tests += 1

        # when there are more tests, if the user entered any
        if student_tests > 0:
            # get letter grade, and show student average
            letter_grade = get_letter_grade(average_student_score)
            print(f'\nYour average score is {average_student_score:.2f}% = {letter_grade}')
            # display message based on letter grade
            if letter_grade == 'A' or letter_grade == 'B':
                print('Great job! You did really well!\n')
            elif letter_grade == 'C' or letter_grade == 'D':
                print('Maybe you want to study a bit more next time...\n')
            else:
                print("That wasn't that good! Pay attention next time!\n")
        # if the user did not enter any tests for this student
        else:
            print('You did not enter any values. Continuing to next student...')

    # if user did not enter any tests for any students
    if class_tests == 0:
        print('\nYou did not enter any scores! Exiting...')
    # if there are any tests, find average score and letter grade, display
    else:
        average_class_score = class_score / class_tests
        print(f'\nThe class average score was {average_class_score:.2f}%'
              f'\nThe average letter grade = {get_letter_grade(average_class_score)}')
        print('\nThanks for using the program! Exiting...')


# call main()
main()
