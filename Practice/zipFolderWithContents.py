import zipfile, os

#Below is the code to create the directories and files for testing zipping file code
os.makedirs('/Users/pushkar/Desktop/JupyterNotebook/delicious')
os.makedirs('/Users/pushkar/Desktop/JupyterNotebook/delicious/cats')
os.makedirs('/Users/pushkar/Desktop/JupyterNotebook/delicious/walnut')
os.makedirs('/Users/pushkar/Desktop/JupyterNotebook/delicious/walnut/waffles')
open('/Users/pushkar/Desktop/JupyterNotebook/delicious/spam.txt','a').close()
open('/Users/pushkar/Desktop/JupyterNotebook/delicious/cats/catnames.txt','a').close()
open('/Users/pushkar/Desktop/JupyterNotebook/delicious/cats/zophie.jpg','a').close()
open('/Users/pushkar/Desktop/JupyterNotebook/delicious/walnut/waffles/butter.txt','a').close()

def backupToZip(folder):

    folderAbsPath = os.path.abspath(folder)

    number = 1
    while True:
        zipFileName = os.path.basename(folderAbsPath) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break

        number = number + 1

    backupZip = zipfile.ZipFile(zipFileName,'w')

    for folderName, subFolders, fileNames in os.walk(folder):
        backupZip.write(folderName)
        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            if fileName.startswith(newBase) and fileName.endswith('zip'):
                continue
            backupZip.write(os.path.join(folderName,fileName))
    backupZip.close()
        
backupToZip('/Users/pushkar/Desktop/JupyterNotebook/delicious')
    
            
