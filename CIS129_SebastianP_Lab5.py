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
  print('Enter number of bottles returned for day #', counter, ':')
  counter = counter + 1
  input() 
  totalBottles += todayBottles

# code to set value of variable totalPayout
PAYOUT_PER_BOTTLE = .10
totalPayout = 0
totalPayout = totalBottles * PAYOUT_PER_BOTTLE

print('The total number of bottles returned was'), totalBottles
print('The total payout for the bottles is $'), totalPayout
		
print("Do you want to enter another week’s worth of data?")
print("Enter y or n")
