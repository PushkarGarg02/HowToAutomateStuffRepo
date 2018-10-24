#! python3

import os, PyPDF2, re, sys
from PyPDF2 import PdfFileReader, PdfFileWriter

for folder, subfolders, filenames in os.walk('D:\\Scripts\\Pdf'):
	for filename in filenames:
		if filename.endswith('.pdf'):
			abspath = os.path.abspath(folder)
			pdfFileObject = open(abspath+'\\'+filename,'rb')
			pdfFileReader = PdfFileReader(pdfFileObject)
		
			if pdfFileReader.isEncrypted == False:
				pdfWriter = PdfFileWriter()
			
				for numPage in range(pdfFileReader.numPages):
					pdfWriter.addPage(pdfFileReader.getPage(numPage))
				
				pdfWriter.encrypt(sys.argv[1])
				regex = re.compile(r'^(.*?)\.pdf$')
				nameSearch = regex.search(filename)
				actualFilename = nameSearch.group(1)
				
				encryptedFilename = actualFilename + '_encrypted.pdf'
				completeFilePath = abspath+'\\'+encryptedFilename
				outputFileObject = open(completeFilePath,'wb')
				pdfWriter.write(outputFileObject)
				outputFileObject.close()
				
			pdfEncryptedFileObject = open(abspath+'\\'+encryptedFilename,'rb')
			pdfEncryptedFileReader = PdfFileReader(pdfEncryptedFileObject)
			
			if pdfEncryptedFileReader.isEncrypted == True:
				pdfFileObject.close()
				os.unlink(abspath+'\\'+filename)
				pdfEncryptedFileObject.close()
				
				
for folder, subfolders, filenames in os.walk('D:\\Scripts\\Pdf'):
	for filename in filenames:
		abspath = os.path.abspath(folder)
		pdfFileObject = open(abspath+'\\'+filename,'rb')
		pdfFileReader = PdfFileReader(pdfFileObject)
		
		if pdfFileReader.isEncrypted == True:
			pdfFileReader.decrypt(sys.argv[2])
			pdfWriter = PdfFileWriter()
			
			for numPage in range(pdfFileReader.numPages):
				pdfWriter.addPage(pdfFileReader.getPage(numPage))
				
			decryptionRegex = re.compile(r'^(.*?)_encrypted.pdf$')
			nameSearch = decryptionRegex.search(filename)
			outputFileObject = open(abspath+'\\DecryptedVersion\\'+nameSearch.group(1)+'.pdf','wb')
			pdfWriter.write(outputFileObject)
			outputFileObject.close()

			
			
