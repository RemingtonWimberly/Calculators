'''
    File name: change_calculator.py
    Author: Remington Wimberly
    Date created: 9/10/2019
    Date last modified: 9/11/2019
    Python Version: 3.7.3
'''

def float_to_int(num):
    # convert to pennies
    return int(float(num) * 100)

# this method calculates the change in each denomination 
def make_change(cost, moneygiven):
    # convert float to int
    cost = float_to_int(cost)
    # convert float to int
    moneygiven = float_to_int(moneygiven)
    # calculate remainder
    cents = moneygiven - cost
    # find quarters
    returnedtuple = divmod(cents, 25)
    quarters = returnedtuple[0]
    # find dimes
    cents_remaining = returnedtuple[1]
    returnedtuple = divmod(cents_remaining, 10)
    dimes = returnedtuple[0]
    # find the nickles
    cents_remaining = returnedtuple[1]
    returnedtuple = divmod(cents_remaining, 5)
    nickels = returnedtuple[0]
    # returns the pennies
    cents_remaining = returnedtuple[1]

    return (quarters, dimes, nickels, cents_remaining)

# This program calculates the change owed in the appropriate denomination
def main():
    print('Welcome to the change calculator!')
    # get input
    cost = float(input('How much is the item?: '))
    moneygiven = float(input('How much money was given?: '))
    # take returned value and assign to a new list
    changelist = make_change(cost, moneygiven)
    # print final result in a sentence format
    print(f'Please give the customer: {changelist[0]} quarters, {changelist[1]} dimes, {changelist[2]} nickels, '
          f'{changelist[3]} pennies.')

   # print as table
    print('Change')
    print('Quarters:', changelist[0])
    print('Dimes:', changelist[1])
    print('Nickles:', changelist[2])
    print('Pennies:', changelist[3])


if __name__ == '__main__':
    # change(cost,money_given)
    main()
