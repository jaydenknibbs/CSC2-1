#function
def num_check(amount):
    while True:
        try:
            response= int(input(amount))
            return response
    
        except ValueError:
            print("please enter a number") 


#ask for the name of the meal
meal = input("What is the name of the meal you whish to create")
txt = 'Wow {} sounds nice'
print (txt.format(meal))
#ask about servings under here
while True:
    servings = int(input('How many servings in this meal? '))
    if 1 <= servings <= 120:
        break
    elif servings < 1:
        ('please Put in a reasonable amount')
        continue   
    else:
        print('That seems incorrect please retry')
        continue
print('program continues')