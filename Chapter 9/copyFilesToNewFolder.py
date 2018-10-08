import os, shutil

print('Before adding files:' +os.listdir())

open('test.jpg','a').close()
open('abc.pdf','a').close()
os.makedirs('newFolder')

newFolderAbsolutePath = os.path.abspath('newFolder')

for filename in os.listdir():
    if filename.endswith('.pdf') or filename.endswith('.jpg'):
        shutil.move(filename,newFolderAbsolutePath)
    else:
        countine

print('After adding files:' +os.listdir(newFolderAbsolutePath))
