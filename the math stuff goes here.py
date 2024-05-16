#the math stuff goes here
weight = [] 
ingrdiant_amount_requirement = ('How much of each ingrediant do you need?  please answer in the order of the list being displayed. ')
print (supplies)
while True:
    amount = input(' how much of the first item do you need: ')
    weight.append(amount)
    choice = input('Did you need to add any more amounts y/n: ')
    if choice == 'no':
        break

