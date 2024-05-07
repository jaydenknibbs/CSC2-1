supplies = []
cost = []

def yes_no(question):
    """
    Function to prompt user for a yes/no response.
    """
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return "yes"
        elif response == 'no' or response == 'n':
            return "no"
        else:
            print("Please enter yes or no")

def num_check(amount):
    """
    Function to check if input is a valid number.
    """
    while True:
        try:
            response = int(input(amount))
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
#ask about servings under here
while True:
    servings = num_check(input('How many servings in this meal? '))
    if 1 <= servings <= 120:
        break
    elif servings < 1:
        ('please Put in a reasonable amount')
        continue   
    else:
        print('That seems incorrect please retry')
        continue
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
