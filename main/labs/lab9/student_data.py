# main Student class
class Student(object):
    def __init__(self, name, uid, gpa, grade, full_time=True):
        # this is not actually the initialized values,
        # we are assigning to the property, which initializes
        # the data attributes. all data attributes are protected
        # not private, in case we ever create a subclass
        # we do not need to initialize attributes because they are all
        # initialized in the setters of the properties
        self.name = name    # self.name is not an attribute, its a property
        self.uid = uid      # same here and below too
        self.gpa = gpa
        self.grade = grade
        self.full_time = full_time

    # basically just __str__ but it returns a dict of data
    def data(self):
        # separate first and last name
        split_name = self._name.split(maxsplit=1)
        first_name = split_name[0]
        last_name = split_name[1]

        # create a dict for data and the identity
        student_name = {
            'First': first_name,
            'Last': last_name,
        }
        student_data = {
            'Id': self._uid,
            'GPA': self._gpa,
            'Grade': self._grade + '%',
            'Full Time': self._full_time
        }
        return student_name, student_data

    # here we define all of the properties for the protected attributes. _ = protected __ = private
    # everything with the property decorator is a getter. This is where all the attributes are defined
    @property
    def name(self):
        return self._name

    @property
    def uid(self):
        return self._uid

    @property
    def gpa(self):
        return self._gpa

    @property
    def grade(self):
        return self._grade

    @property
    def full_time(self):
        return self._full_time

    # setters to match all the getters.
    @name.setter
    def name(self, name):
        self._name = name

    @uid.setter
    def uid(self, uid):
        # make sure uid is a string
        self._uid = str(uid)

    @gpa.setter
    def gpa(self, gpa):
        try:
            # convert to float
            gpa = float(gpa)
            # validate and convert to 2-point string
            if 0 < gpa < 5:
                self._gpa = f'{gpa:.2f}'
            else:
                raise RuntimeError("ERROR: GPA not valid. Must be between 0 and 5.\n")
        # if we have an issue converting to float, raise a RuntimeError instead
        except ValueError:
            raise RuntimeError("ERROR: GPA input not valid.\n")

    @grade.setter
    def grade(self, grade):
        # validation loop
        success = False
        while not success:
            try:
                # convert to float and validate
                grade = float(grade)
                if grade > 100:
                    # 2nd input validation loop
                    valid = False
                    while not valid:
                        # maybe the student got about 100? Let's double check that.
                        is_extra_credit = input(
                            "You entered a value greater than 100. Is that correct? (y/n): ").lower()
                        # if it wasn't a typo, convert to 2-point string and exit both loops
                        # (get option from first char of input)
                        if is_extra_credit[0] == "y":
                            self._grade = f'{grade:.2f}'
                            valid = True
                            success = True
                        # if it was a typo, get the grade again (get option from first char of input)
                        elif is_extra_credit[0] == "n":
                            grade = float(input("Enter your new expected grade: "))
                            valid = True
                        # if the user didn't give a good input, try again
                        else:
                            print("You did not enter a valid input. Try again.\n")
                # there's no possible way to get < 0
                elif grade < 0:
                    raise RuntimeError("ERROR: Expected grade not valid.\n")
                # if its all good, convert to 2-point float and store as string, leave loop
                else:
                    self._grade = f'{grade:.2f}'
                    success = True
            # only raise runtime errors, not value errors
            except ValueError:
                raise RuntimeError("ERROR: Expected grade input not valid.\n")

    @full_time.setter
    def full_time(self, full_time):
        # make sure we're getting a bool and assign it
        if type(full_time) is bool:
            self._full_time = full_time
        else:
            raise RuntimeError("ERROR: Full time is not a boolean.\n")


# to hold student objects
class Roster(object):
    def __init__(self):
        # declare list to hold objects
        self._students = []

    # decorator to declare students as getter
    @property
    def students(self):
        return self._students

    # this is how we create Student objects
    def add_student_entry(self, name, uid, gpa, grade, full_time=True):
        # make sure that the name and ID doesn't exist already
        if self.find_student(name) is not None:
            raise RuntimeError("ERROR: Student name already exists.\n")
        elif self.find_student(str(uid)) is not None:
            raise RuntimeError("ERROR: Student id already exists.\n")
        # if it's unique, add a new Student object to the list of student
        else:
            self._students.append(Student(name, str(uid), gpa, grade, full_time))

    # this is how we look up students in the roster
    def find_student(self, name_or_id):
        # loop through each object in the list
        for student in self._students:
            # if the name or id is found in the current Student, return it
            if name_or_id.lower() == student.name.lower() or name_or_id.lower() == student.uid.lower():
                return student
        # if we don't find anything, return None
        return None
