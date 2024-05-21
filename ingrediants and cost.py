#day 6 of being cooked
supplies = []
cost = []

#normi stuff here
while True:
    ingredient = input('What is an ingredient in the dish: ')
    supplies.append(ingredient)
    price = input('What is the price of the item? ')
    cost.append(price)
    choice = input('Would you like to add another ingredient (yes or no): ')
    if choice.lower() == 'no':
        break

ingredients_cost = zip(supplies, cost)
for item, price in ingredients_cost:
    print(f'{item}: ${price}')

# Assuming you wanted to print the list of costs, not access an index of the list
print(cost)
