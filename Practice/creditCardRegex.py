'''
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics: 

► It must start with a ,  or . 
► It must contain exactly  digits. 
► It must only consist of digits (-). 
► It may have digits in groups of , separated by one hyphen "-". 
► It must NOT use any other separator like ' ' , '_', etc. 
► It must NOT have  or more consecutive repeated digits.

42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

'''import re

inputString = '6\n4123456789123456\n5123-4567-8912-3456\n61234-567-8912-3456\n4123356789123456\n5133-3367-8912-3456\n5123 - 3567 - 8912 - 3456'

inputList = inputString.split('\n')
del inputList[0]
print(inputList)
for inputData in inputList:
    if len(inputData) != 16:
        if len(inputData) != 19:
            print(inputData.rjust(30) + ' Invalid')
            continue
    
    creditCardRegex = re.compile(r'(\d{4})(-)?(\d{4})(-)?(\d{4})(-)?(\d{4})')
    if creditCardRegex.search(inputData) == None:
        print(inputData.rjust(30) + ' Invalid')
        continue
    
    hyphenRegex = re.compile(r'(-)')
    tempCode = hyphenRegex.sub('',inputData)
    creditCardRegex1 = re.compile(r'(\d)\1{3,}')
    if creditCardRegex1.search(tempCode) != None:
        print(inputData.rjust(30) + ' Invalid')
        continue
        
    print(inputData.rjust(30) + ' Valid')
