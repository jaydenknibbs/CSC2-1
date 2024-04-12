#ask for the name of the meal
while True:
    meal = input("What is the name of the meal you wish to create: ")
    if not any(char.isdigit() for char in meal):
        break
    else:
        print("Meal name cannot contain numbers. Please enter again.")

txt = 'Wow {} sounds nice'
print(txt.format(meal))
    
    