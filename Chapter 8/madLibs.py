fileHandler = open('sampleFile','w')
fileHandler.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
fileHandler.close()

fileHandler = open('sampleFile','r')
newFileHandler = open('newSampleFile','w')
for words in fileHandler.read().split():
    if words in ['ADJECTIVE','ADVERB']:
        inputString = str(input('Enter an %s:' % words))
        newFileHandler.write(inputString + ' ')
    elif words in ['NOUN','VERB']:
        inputString = str(input('Enter a %s:' % words))
        newFileHandler.write(inputString + ' ')
    else:
        newFileHandler.write(words + ' ')

fileHandler.close()
newFileHandler.close()

newFileHandler = open('newSampleFile','r')
text = newFileHandler.read()
print(text)
