#Sebastian Preston
#10/6/2024  
#CIS129  
#Lab 5: Return Bottle Program
#This program takes input from the user to calculate the payout for the sum of bottles turned in

totalBottles = 0
counter = 1
todayBottles = 0
keepGoing = "y"

# Step 2: Loop to run program again
while counter <= 7:
  # ask how many bottles for the day
  # print statement for formatting leave as is
  print('Enter number of bottles returned for day', counter, ':')
  # store blank input in the todayBottles variable. remember you need to turn it into a integer. 
  #ok how do we add all the bottles now?? totalBottles += todayBottles
  todayBottles = int(input())
  totalBottles += todayBottles
  counter = counter + 1
# i dont understand how it works with counter but not the totalBottles okay. this is the long way
# totalBottles = totalBottles + todayBottles

# code to set value of variable totalPayout
PAYOUT_PER_BOTTLE = .10
totalPayout = 0
# I am trying to multiply an integer by a decimal and that is a no no for any programming language
# they need to be of the same type
# ok hold up! why isnt it adding my other part tho? the totalBottles part, they are all the same type??
totalPayout = float(totalBottles) * PAYOUT_PER_BOTTLE

print('The total number of bottles returned was', totalBottles) # I didn't include totalBottles inside the print statement
print('The total payout for the bottles is $', totalPayout)
# NIIIICEEEEEE
print("Do you want to enter another week’s worth of data?")
print("Enter y or n")
# it helps to lay out the instructions
#i want it to have the days for each input, see how it works now???
