print('My Coffee and Muffin Shop')
coffees = input('Number of coffees bought?' ) 
muffins = input('Number of muffins bought?' )

num_of_coffees = coffees
num_of_muffins = muffins

price_of_coffee = 5
price_of_muffin = 4
subtotal = price_of_coffee + price_of_muffin


print('My Coffee and Muffin Shop Receipt')
print(int(num_of_coffees), 'at $5 each:' num_of_coffees * int(price_of_coffee)
print(int(num_of_muffins), 'at $4 each:' num_of_muffins * int(price_of_muffin)
print('6% tax:') subtotal % float(.04)


