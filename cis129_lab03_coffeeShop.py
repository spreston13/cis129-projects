# Author: Sebastian P.
# My second Python lab in my CIS129 course
# Prints a receipt with added tax

print('*' * 40)
print('My Coffee and Muffin Shop')
#Declare integer numOfCoffees
print('Number of coffees bought?')
numOfCoffees = input()
#Declare integer numOfMuffins
print('Number of muffins bought?')
numOfMuffins = input()
#Declare integer numOfTeas
print('Number of teas bought?')
numOfTeas = input()
#Declare integer numOfSandwiches
print('Number of sandwiches bought?')
numOfSandwiches = input()
print('*' * 40)
#Price number of items bought by sale price
cPrice = int(numOfCoffees) * 5
mPrice = int(numOfMuffins) * 4
tPrice = int(numOfTeas) * 3
sPrice = int(numOfSandwiches) * 6
#Display the receipt with added tax
print('My Coffee and Muffin Shop Receipt')
cBought = str(numOfCoffees)
mBought = str(numOfMuffins)
tBought = str(numOfTeas)
sBought = str(numOfSandwiches)
print(cBought + ' coffees at $5 each: $ '+ str(cPrice))
print(mBought + ' muffins at $4 each: $ '+ str(mPrice))
print(tBought + ' teas at $3 each: $ '+ str(tPrice))
print(sBought + ' sandwiches at $6 each: $ '+ str(sPrice))
#Get the subtotal 
subTotal = cPrice + mPrice + tPrice + sPrice
tax = subTotal * .06
print('6% tax: $' + str(tax))
print('─' * 30)
finalTotal = subTotal + tax
print('Total: $'+ str(finalTotal))
print('*' * 40)
