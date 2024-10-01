# Module 5 Lab-5
# Sebastian Preston
# 9/30/2024
# This program calculates a store's monthly sales and calculates the amount the store receives, while also calculating an employee's bonus amount based on the sales increase.

monthlySales = float(input('Enter monthly sales amount: '))
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

salesIncrease = float(input("Enter percent of sales increase"))
salesIncrease = salesIncrease/100
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

print('The store bonus amount is $', storeAmount)
print('The employee bonus amount is $', empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')
