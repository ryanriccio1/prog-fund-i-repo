# declare constants
BASE_HOURS = 40
OT_MULTIPLIER = 1.5


def main():
    # get input
    wage = float(input('Enter your hourly wage (xx.xx): '))
    hours_worked = float(input('Enter the number of hours worked this week(xx.x): '))

    # if greater than base hours add ot
    if hours_worked > BASE_HOURS:
        ot_hours = hours_worked - BASE_HOURS
        ot_pay = ot_hours * wage * OT_MULTIPLIER

        total_pay = ot_pay + wage * BASE_HOURS

        # display data
        print(f'You worked a total of {hours_worked}h this week, with {ot_hours}h\n'
              f'being overtime. You earned {OT_MULTIPLIER} times your wage of\n'
              f'${wage:,.2f}/hr wage for your overtime hours. Your total pay is\n'
              f'${total_pay:,.2f}')
    # otherwise do normal pay
    else:
        total_pay = wage * BASE_HOURS

        # display data
        print(f'You worked a total of {hours_worked}h this week.\n'
              f'with a wage of ${wage:,.2f}/hr wage. Your total pay is\n'
              f'${total_pay:,.2f}')


main()
