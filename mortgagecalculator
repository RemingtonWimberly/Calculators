# This program calculates the monthly payments for a monthly payment of a fixed term mortgage
# over nth terms at a given interest rate

def mortgage_calculator(L, c, n):
    payments = L*(c*(1 + c)**n)/((1 + c)**n - 1)
    return round(payments, 2)

def main():
    L = loan_amount = int(input('Enter the amount of the loan: '))
    interest = float(input('Enter the interest rate: '))
    n = months = int(input("Enter the terms or total months: "))
    c = monthly_interest = interest / 100 / 12
    payments = mortgage_calculator(L,c,n)
    total_cost = payments * n

    print('\nThe total monthly payment over {} terms is ${}'.format(n,payments))
    print('The total amount of the loan is {}'.format(total_cost))

if __name__ == '__main__':
    main()

