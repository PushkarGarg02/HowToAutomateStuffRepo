#! python3

from PyPDF2 import PdfFileReader, PdfFileWriter
import os

pdfFiles = []
for filename in os.listdir('D:\\Scripts\Pdf'):
	if filename.endswith('.pdf'):
		pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)
pdfWriter = PdfFileWriter()
print(pdfFiles)
for filename in pdfFiles:
	fileObject = open('D:\\Scripts\\Pdf\\'+filename,'rb')
	fileReader = PdfFileReader(fileObject)
	
	for pageNum in range(1,fileReader.numPages):
		pdfWriter.addPage(fileReader.getPage(pageNum))
	
	
		
outputFileObject = open('D:\\Scripts\\Pdf\\allMinutes.pdf','wb')		
pdfWriter.write(outputFileObject)
outputFileObject.close()
