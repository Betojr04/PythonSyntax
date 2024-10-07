"""
TASK 1

Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic!
"""

bread, peanut_butter, jelly = 10, 15, 20
print(bread + peanut_butter + jelly)


"""
TASK 2 

If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.
"""
initial_amount = 10000
YEARLY_INTEREST_RATE = 0.07

end_of_year_amount = initial_amount + initial_amount * YEARLY_INTEREST_RATE
print(end_of_year_amount)
