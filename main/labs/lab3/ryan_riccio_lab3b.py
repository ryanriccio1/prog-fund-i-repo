# this program will calculate the gross pay for a given employee and return
# it as a pay stub

# declare constants
BASE_SALARY = 2000
MAX_VACATION_DAYS = 3
MAX_VACATION_DEDUCTION = 200
BONUS_THRESH = 3
BONUS_0 = 0.0
BONUS_1 = 0.0
BONUS_2 = 1000.0
BONUS_3 = 5000.0
GREATER_3_BONUS = 100000.0
LONG_TIME_MONTH = 60
LONG_TIME_BONUS = 1000
LONG_TIME_THRESH = 100000
RANGE_0_MAX = 10000
RANGE_1_MAX = 100000
RANGE_2_MAX = 500000
RANGE_3_MAX = 1000000
RANGE_0_COMMISSION = 0.0
RANGE_1_COMMISSION = 0.02
RANGE_2_COMMISSION = 0.15
RANGE_3_COMMISSION = 0.28
GREATER_3_COMMISSION = 0.35


# create class to store data from user
class PaycheckData(object):
    # initialize and compute
    def __init__(self, name, months_worked, vacation_days, sales):
        self._name = name
        self._months_worked = months_worked
        self._vacation_days = vacation_days
        self._sales = sales

        # will assign _commission (%) and _bonus ($) based on range
        # if it is in range 0 (between 0 and less than RANGE_0_MAX)
        if self._sales < RANGE_0_MAX:
            self._commission = RANGE_0_COMMISSION
            self._bonus = BONUS_0
        # if it is in range 1
        elif RANGE_0_MAX <= self._sales <= RANGE_1_MAX:
            self._commission = RANGE_1_COMMISSION
            self._bonus = BONUS_1
        # if it is in range 2
        elif RANGE_1_MAX < self._sales <= RANGE_2_MAX:
            self._commission = RANGE_2_COMMISSION
            self._bonus = BONUS_2
        # if it is in range 3
        elif RANGE_2_MAX < self._sales <= RANGE_3_MAX:
            self._commission = RANGE_3_COMMISSION
            self._bonus = BONUS_3
        # if not in other ranges it is > range 3 (> GREATER_3_MAX )
        else:
            self._commission = GREATER_3_COMMISSION
            self._bonus = GREATER_3_BONUS

        # if not worked for set amount of time, no bonus
        if self._months_worked < BONUS_THRESH:
            self._bonus = 0.0

        # if they are over their vacation days, deduction is assigned
        if self._vacation_days > MAX_VACATION_DAYS:
            self._deduction = MAX_VACATION_DEDUCTION
        # if not, deduction is zero
        else:
            self._deduction = 0.0

        # if worked for set amount of time and sales hit threshold, add bonus
        if self._months_worked >= LONG_TIME_MONTH and self._sales > LONG_TIME_THRESH:
            self._additional_bonus = LONG_TIME_BONUS
        # if not, no add. bonus
        else:
            self._additional_bonus = 0.0

        # calculate commission as money
        self._commission = self._sales * self._commission

        # add commission, bonus, add. bonus, salary, subtract deduction
        self._gross_pay = (self._commission + self._bonus + self._additional_bonus -
                           self._deduction + BASE_SALARY)

    # function to print data
    def print_paycheck(self):
        print('\n', PaycheckData.stub_format('NAME', self._name, 'l'),

              # add label at end before calculating len()
              PaycheckData.stub_format('TIME', f'{self._months_worked}' + 'm', 'l'),

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('SALARY', f'${BASE_SALARY:,.2f}', 'l'), '\n',
              PaycheckData.stub_format('NAME', self._name, 'v'),

              # add label at end before calculating len()
              PaycheckData.stub_format('TIME', f'{self._months_worked}' + 'm', 'v'),

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('SALARY', f'${BASE_SALARY:,.2f}', 'v'), '\n\n',

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('COMMISSION', f'${self._commission:,.2f}', 'l'),

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('BONUS', f'${self._bonus:,.2f}', 'l'), '\n',

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('COMMISSION', f'${self._commission:,.2f}', 'v'),

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('BONUS', f'${self._bonus:,.2f}', 'v'), '\n\n',

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('ADD. BONUS', f'${self._additional_bonus:,.2f}', 'l'),

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('DEDUCTIONS', f'-${self._deduction:,.2f}', 'l'), '\n',

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('ADD. BONUS', f'${self._additional_bonus:,.2f}', 'v'),

              # format as money with 2 floating points before calculating len()
              PaycheckData.stub_format('DEDUCTIONS', f'-${self._deduction:,.2f}', 'v'), '\n\n',

              # display gross pay (no need to format to table as only 1 line)
              f'GROSS PAY\n${self._gross_pay:,.2f}\n', sep='')

    # static function to add consistent spaces to format pay stub
    # 3 strings are passed in, the difference of the string lengths
    # is evaluated to make sure that there is 4 spaces after the
    # longest string. Extra spaces are added to shorter one to make
    # it line up. option is to decide whether to return the label
    # or the variable
    @staticmethod
    def stub_format(label, variable, option):
        # convert var to str
        variable = str(variable)

        # get length of variables
        label_length = len(label)
        var_length = len(variable)

        # see which option was selected
        if option == 'l':
            # see which is the longest, if var is less,
            # set it to 4 (min amount of spaces)
            if var_length < label_length:
                spaces = 4
            # if var is longer, find the difference, add
            # 4 spaces
            else:
                spaces = var_length - label_length + 4
            formatted_label = label + (' ' * spaces)
            return formatted_label
        # see which option was selected
        elif option == 'v':
            # see which is the longest, if label is less,
            # set it to 4 (min amount of spaces)
            if var_length > label_length:
                spaces = 4
            # if label is longer, find the difference, add
            # 4 spaces
            else:
                spaces = label_length - var_length + 4
            formatted_label = variable + (' ' * spaces)
            return formatted_label
        # if no option selected, return nothing
        else:
            pass
       

def main():
    # so that user can repeat if wanted
    keep_going = 'y'
    while keep_going == 'y':
        # get name of employee
        name = input('Enter name of employee: ')

        # get time worked at company (years, months)
        years_worked = int(input('Enter years worked (do not include months): '))
        months_worked = int(input('Enter months worked (do not include years): '))

        # calculate total months
        months_worked = years_worked * 12 + months_worked

        # get vacation days taken this month
        vacation_days = int(input('Enter number of days taken off this month: '))

        # get sales for month
        sales = float(input('Enter sales for the month: '))

        # write data to class
        paycheck_data = PaycheckData(name, months_worked, vacation_days, sales)

        # print data
        paycheck_data.print_paycheck()

        # check to make sure following input is valid, if not repeat prompt
        valid = False
        while not valid:
            keep_going = input('Do you want to do another (y/n): ').lower()
            # if not valid, tell user and repeat
            if keep_going != 'y' and keep_going != 'n':
                print('That was not a valid input')
                valid = False
            # if y, restart program
            elif keep_going == 'y':
                valid = True
                print('\n')
                main()
            # if valid, and !=y, thank the user and exit
            else:
                print('\nThank you, goodbye!')
                valid = True


main()
