#function
def num_check(amount):
    while True:
        try:
            response= int(input(amount))
            return response
    
        except ValueError:
            print("please enter a number") 


#ask for the name of the meal
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
print('program continues')
