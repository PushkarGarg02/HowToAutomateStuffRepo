import os, shutil

print(os.listdir())
currentDirectoryPath = os.path.abspath('.')
for folderName, subfolders, filenames in os.walk(currentDirectoryPath):
    print('Inside folder %s...' % (folderName))
    
    for filename in filenames:
        fileNameAbsPath = os.path.abspath(filename)
        fileSize = os.path.getsize(fileNameAbsPath)
        if fileSize >= 0:
            print((' '*5) + '%s having %s size' %(fileNameAbsPath,fileSize))
