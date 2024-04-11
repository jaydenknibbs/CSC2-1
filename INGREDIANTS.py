#FUNC HERE
def num_check(amount):
    while True:
        try:
            response= int(input(amount))
            return response
    
        except ValueError:
            print("please enter a number") 
# the name of each item in the meal
print ('now continuing on please enter the amount of ingrediants in the meal')
ingreadint_count = num_check(input(''))
