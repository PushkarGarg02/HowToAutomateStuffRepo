#First create some files where we can do out testing
import os

fileHandler = open('test10-06-2018.txt','w')
fileHandler.write('This is test file.')
fileHandler.close()

fileHandler = open('test14-12-1918.txt','w')
fileHandler.write('This is another file.')
fileHandler.close()

fileHandler = open('test23-05-2018.txt','w')
fileHandler.write('This is another file.')
fileHandler.close()

#Let see what all files are present which can be converted
print(os.listdir())

#Lets import few other modules which will be used to copy the files between folders and regex creation
import re, shutil

#Lets create a regex for fiding out the files having MM-DD-YY (American) pattern
fileNameRegex = re.compile(r'''^(.*?)  #any pattern before date
((0|1)?(0|1|2))-  #month pattern
((0|1|2|3)?\d)- #day pattern
((19|20)\d\d) #year pattern
(.*?)$ #any pattern at the end of file
''',re.VERBOSE)

for filenames in os.listdir():
    fileSearch = fileNameRegex.search(filenames)
    
    if fileSearch == None:
        continue
        
    beforePattern = fileSearch.group(1)
    monthPattern = fileSearch.group(2)
    dayPattern = fileSearch.group(5)
    yearPattern = fileSearch.group(7)
    afterPattern = fileSearch.group(9)
    
    americanFileName = filenames
    europeanFileName = beforePattern + dayPattern + '-' + monthPattern + '-' + yearPattern + afterPattern
    
    absolutePath = os.path.abspath('.')
    americanFileAbsPath = absolutePath + '/' + americanFileName
    europeanFileAbsPath = absolutePath + '/' + europeanFileName
    print('File %s moved to %s'%(americanFileAbsPath,europeanFileAbsPath))
    shutil.move(americanFileAbsPath,europeanFileAbsPath)
    

print(os.listdir())

