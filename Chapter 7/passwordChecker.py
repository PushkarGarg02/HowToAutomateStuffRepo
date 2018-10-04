import re

inputPasswordforValidation = str(input())

lowerCaseRegex = re.compile(r'[a-z]+')
upperCaseRegex = re.compile(r'[A-Z]+')
digitRegex = re.compile(r'\d+')

if len(inputPasswordforValidation) <8:
    print('Password must be at least 8 characters.')
elif lowerCaseRegex.search(inputPasswordforValidation) == None:
    print('Password must contain at least one lower case letter.')
elif upperCaseRegex.search(inputPasswordforValidation) == None:
    print('Password must contain at least one upper case letter.')
elif digitRegex.search(inputPasswordforValidation) == None:
    print('Password must contain at least one digit.')
else:
    print('Wonderful! Your password is strong.')
