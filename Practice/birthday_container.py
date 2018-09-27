birthdayContainer = {'Pushkar': '9-Sep', 'Richa': '7-July'}

while True:
    print('Please enter the name (blank to exit)')
    name = input()
    if name == '':
        break
    
    if name in birthdayContainer:
        print(birthdayContainer[name] + ' is the birthday of ' + name)
    else:
        print('There is no birthday information for '+ name)
        print('What is their birthday (DD-Month)? ')
        bday = input()
        birthdayContainer[name] = bday
        print('Birthday Database updated successfully')
