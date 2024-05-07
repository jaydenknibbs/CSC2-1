#day 6 of being cooked
supplies = []
cost = []
# func goes here if any


#normi stuff here
while True:
    ingrediants = input(' what is an ingrediant in the dish: ')
    supplies.append(ingrediants)
    price = input('What is the price of the item?')
    cost.append(price)
    choice = input('would you like to add another ingrediant (yes or no): ')
    if choice == 'no':
        break

ingrediants_cost = zip(supplies, cost)
for i in ingrediants_cost:
    print (i)

list[cost]
