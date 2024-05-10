#main
supplies = []
cost = []

def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return "yes"
        elif response == 'no' or response == 'n':
            return "no"
        else:
            print("Please enter yes or no")

def num_check(amount):
    while True:
        try:
            response = int(amount)
            if response < 1:
                print("Please enter a reasonable number")
                continue
            return response
        except ValueError:
            print("Please enter a number")

# Ask if instructions are needed
instructions = yes_no("Do you need instructions? ")
if instructions == 'yes':
    print("This code is designed to help you:")
    print("- Enter the name of the meal")
    print("- Enter the amount of servings")
    print("- Enter the number of ingredients")
    print("- Enter the ingredients")
    print("- Enter the cost")
    print("It will then calculate how much each meal will cost you and how much it costs per serving.")
    print("")

# Ask for the name of the meal
while True:
    meal = input("What is the name of the meal you wish to create: ")
    if not any(char.isdigit() for char in meal):
        break
    else:
        print("Meal name cannot contain numbers. Please enter again.")
txt = 'Wow {} sounds nice'
print(txt.format(meal))

# Ask about servings
while True:
    servings = num_check(input('How many servings in this meal? '))
    if servings <= 120:
        break
    else:
        print('That seems excessive, please enter a reasonable amount')

# Loop for ingredients and their costs
while True:
    ingredient = input('What is an ingredient in the dish: ')
    supplies.append(ingredient)
    price = input('What is the price of the item? ')
    cost.append(price)
    choice = yes_no('Would you like to add another ingredient (yes or no): ')
    if choice == 'no':
        break

# Printing ingredient-cost pairs
print("Ingredients and their costs:")
for item, price in zip(supplies, cost):
    print(f'{item}: ${price}')
