#Sebastian Preston
#10/6/2024  
#CIS129  
#Lab 5: Return Bottle Program
#This program takes input from the user to calculate the payout for the sum of bottles turned in

totalBottles = 0
counter = 1	
keepGoing = "y"

# Step 2: Loop to run program again
while counter <= 7:
  print('Enter number of bottles returned for day #', counter, ':')
  todayBottles = int(input())
  totalBottles += todayBottles
  counter = counter + 1

# code to set value of variable totalPayout
PAYOUT_PER_BOTTLE = .10
totalPayout = 0
totalPayout = totalBottles * PAYOUT_PER_BOTTLE	

# code to print the number of total bottles and total payout
print('The total number of bottles returned was'), str(totalBottles)
print('The total payout for the bottles is $'), totalPayout
		
print("Do you want to enter another week’s worth of data?")
print("Enter y or n")
