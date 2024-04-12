#FUNCTIONS HERE
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
            response= int(input(amount))
            return response
    
        except ValueError:
            print("please enter a number") 

#OTHER INPORTANT STUFF HERE



#LEFT OVER STUFF HERE
instructions = yes_no("Do you need instructions?")
if instructions =='yes':
    print ('This code is desigend to help you')
    print ('first you will enter the name of the meal')
    print ('followed by the amount of servings ')
    print ('after you will be asked how many ingrediants there are')
    print ('then you will be asked what the ingrediants are')
    print ('after this has happened you will be asked to enter the cost')
    print ('it will then work out how much each meal will cost you ')
    print ('and how much it is each servin')
    print ('')
    print ('')
    print ('')
    
else:

#ask for the name of the meal
    meal = input("What is the name of the meal you whish to create")
    txt = 'Wow {} sounds nice'
    print (txt.format(meal))
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