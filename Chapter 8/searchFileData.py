##Below is sample data which will be created to test this code
fileHandle = open('test1.txt','w')
fileHandle.write('This is the sample file.')
fileHandle.close()

fileHandle = open('test2.txt','w')
fileHandle.write('This is the sample file and this would be second file which was created.')
fileHandle.close()

fileHandle = open('test3.text','w')
fileHandle.write('Hello Friend, We are please to inform you that this would be the third file in this test code.')
fileHandle.close()

import os
print(' '.join(os.listdir()))

#Main code to search for a regular expression in all the .txt file is starting here
import re

#inputRegularExpression = str(input('Enter your regular expresion to search for string:'))

fileFormatRegex = re.compile('[a-zA-Z0-9]+\.txt$')
for files in fileFormatRegex.findall(' '.join(os.listdir())):
   print(files)
