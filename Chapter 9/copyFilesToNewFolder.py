import os, shutil

print(os.listdir())

newFolderAbsolutePath = os.path.abspath('./newFolder')

for filename in os.listdir():
    if filename.endswith('.pdf') or filename.endswith('.jpg'):
        shutil.move(filename,newFolderAbsolutePath)
    else:
        continue

print(os.listdir(newFolderAbsolutePath))

#Output
#['Index.ipynb', 'environment.yml', 'apt.txt', 'newFolder', 'abc.pdf', 'test.jpg', 'Untitled.ipynb', '.ipynb_checkpoints']
#['abc.pdf', 'test.jpg']
