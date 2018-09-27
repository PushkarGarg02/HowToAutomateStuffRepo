spam = ['apples','bananas','tofu','cats']

def functionTemp(parameterList):
    str = ''
    
    for itemIndex in range(len(parameterList)):
        if itemIndex != (len(parameterList)-1):
            str = str + parameterList[itemIndex] + ', '
        else:
            str = str + 'and ' + parameterList[itemIndex] + '.'
    
    return str

print(functionTemp(spam))

