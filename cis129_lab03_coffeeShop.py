# Sebastian Preston
# CIS129 Lab 2
#This program will ask the user for the number of coffee and muffins they are purchasing. The price of a cup of coffee is $5 and the price of a muffin is $4. 
#Calculate 6% tax on the subtotal.

#This section gathers input from the customer on how many items they purchased
print("*"*39)
print("My Coffee and Muffin Shop")
print("How many coffees bought?: ")
cBought = int(input())
print("How many muffins bought?: ")
mBought = int(input()) 
print("How many doughnuts bought?: ")
dBought = int(input())
print("How many icecreams bought?: ")
iBought = int(input())

print("*"*39)

#This section itemizes and taxes the products
print("*"*39)
print("My Coffee and Muffin Shop Receipt")
cSum = cBought * 5.00 
print(str(cBought)+" Coffees bought at $5 each:",cSum)
mSum = mBought * 4.00
print(str(mBought)+" Muffins bought at $4 each:",mSum)
dSum = dBought * 3.00 
print(str(dBought)+" Doughnuts bought at $3 each:",dSum)
iSum = iBought * 2.00 
print(str(iBought)+" Icecreams bought at $2 each:",iSum)
tax = (cSum + mSum + dSum + iSum)*.06
print("6% tax: $ "+str(tax))

#This section calculates the grand total
print("-"*15)
total = cSum + mSum + dSum + iSum + tax
print("Total: "+str(total))
print("*"*39)
