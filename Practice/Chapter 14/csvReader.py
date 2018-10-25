#! python3

import csv

#Read the csv file and print the content
exampleFile = open('D:\\Scripts\\example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)  #list data can be accessed by script notation

for row in exampleReader:
	print(str(exampleReader.line_num)+' '+str(row))

#Lets write a new csv file
outputFile = open('D:\\Scripts\\output.tsv','w')
outputWriter = csv.writer(outputFile, delimiter='\t',lineterminator='\n\n')

outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['Hello, World','eggs','bacon','ham'])
outputWriter.writerow([1,2,3.14,4])
outputFile.close()


