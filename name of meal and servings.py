


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