#! python3

'''
Input Files: meetingminutes.pdf, encrypted.pdf, meetingminutes2.pdf, beforeRotation.pdf, watermark.pdf
Output Files: combinedminutes.pdf, afterRotation.pdf, waterMarkedBankFile.pdf, encryptedBankFile.pdf
'''
from PyPDF2 import PdfFileReader, PdfFileWriter

'''Here we will work on seeingnumber of pages and its text in pdf'''
#Creating PDF Reader object 
pdfObject = open('D:\\Scripts\\meetingminutes.pdf','rb') 
pdfReader = PdfFileReader(pdfObject)
print(pdfReader.numPages) #Number of pages in PDF

#Getting first page and extract the text
pageObject = pdfReader.getPage(0)
print(pageObject.extractText())
pdfObject.close()

'''Here we will see file decryption'''
#Decrypting the PDF
encryptedFileObject = open('D:\\Scripts\\encrypted.pdf','rb')
encryptedPdfReader = PdfFileReader(encryptedFileObject)
print('Is encrypted.pdf file really encrypted? ' + str(encryptedPdfReader.isEncrypted))
encryptedPdfReader.decrypt('rosebud')
print('Is encrypted.pdf file really encrypted after decrypting? ' + str(encryptedPdfReader.isEncrypted))
encryptedFileObject.close()

'''Here we will see how to combine 2 pdfs by copying the pages'''
#Copying pdf pages to create a new pdf
pdf1FileObject = open('D:\\Scripts\\meetingminutes.pdf','rb')
pdf2FileObject = open('D:\\Scripts\\meetingminutes2.pdf','rb')
pdf1Reader = PdfFileReader(pdf1FileObject)
pdf2Reader = PdfFileReader(pdf2FileObject)
pdfWriter = PdfFileWriter()

for numPages in range(pdf1Reader.numPages):
	pdfWriter.addPage(pdf1Reader.getPage(numPages))
	
for numPages in range(pdf2Reader.numPages):
	pdfWriter.addPage(pdf2Reader.getPage(numPages))

pdfOutputFile = open('D:\\Scripts\\combinedminutes.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1FileObject.close()
pdf2FileObject.close()

'''Here we will see the page rotation'''
beforeRotationFileObject = open('D:\\Scripts\\beforeRotation.pdf','rb')
beforeRotationFileReader = PdfFileReader(beforeRotationFileObject)
pageObject = beforeRotationFileReader.getPage(0)
pageObject.rotateClockwise(90)

afterRotationFileObject = open('D:\\Scripts\\afterRotation.pdf','wb')
pdfWriter = PdfFileWriter()
pdfWriter.addPage(pageObject)
pdfWriter.write(afterRotationFileObject)
afterRotationFileObject.close()
beforeRotationFileObject.close()


'''Here we will learn page overlapping'''
bankFileObject = open('D:\\Scripts\\beforeRotation.pdf','rb')
bankFilePdfReader = PdfFileReader(bankFileObject)
bankFileFirstPageObject = bankFilePdfReader.getPage(0)
bankFileFirstPageObject.mergePage(PdfFileReader('D:\\Scripts\\watermark.pdf','rb').getPage(0))

bankFileWatermarkedObject = open('D:\\Scripts\\waterMarkedBankFile.pdf','wb')
pdfWriter = PdfFileWriter()
pdfWriter.addPage(bankFileFirstPageObject)

for numPage in range(1,bankFilePdfReader.numPages):
	pdfWriter.addPage(bankFilePdfReader.getPage(numPage))

pdfWriter.write(bankFileWatermarkedObject)
bankFileObject.close()
bankFileWatermarkedObject.close()


'''Here we will learn how to encrypt the pdf file'''
watermarkedBankFileObject = open('D:\\Scripts\\waterMarkedBankFile.pdf','rb')
watermarkedBankFilePdfReader = PdfFileReader(watermarkedBankFileObject)
pdfWriter = PdfFileWriter()

for numPage in range(watermarkedBankFilePdfReader.numPages):
	pdfWriter.addPage(watermarkedBankFilePdfReader.getPage(numPage))
	
pdfWriter.encrypt('pushkargarg')
encryptedBankFileObject = open('D:\\Scripts\\encryptedBankFile.pdf','wb')
pdfWriter.write(encryptedBankFileObject)
encryptedBankFileObject.close()
watermarkedBankFileObject.close()

'''Here comes the end of basic functions'''
