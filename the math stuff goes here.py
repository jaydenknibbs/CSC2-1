#the math stuff goes here
weight = [] 
supplies = []
cost = []
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

ingrdiant_amount_requirement = ('How much of each ingrediant do you need?  please answer in the order of the list being displayed. ')
print (supplies)
while True:
    amount = input(' how much of the first item do you need: ')
    weight.append(amount)
    choice = input('Did you need to add any more amounts y/n: ')
    if choice == 'no':
        break

# Calculate the total cost of ingredients
total_cost = 0
for item_cost in cost:
    total_cost += float(item_cost)

# Calculate the cost per serving
cost_per_serving = total_cost / servings

# Output the total cost and cost per serving
print(f"\nThe total cost of '{meal}' recipe is: ${total_cost:.2f}")
print(f"The cost per serving is: ${cost_per_serving:.2f}")
