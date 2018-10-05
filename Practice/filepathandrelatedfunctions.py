import os
print('os.getcwd(): ' + os.getcwd())
print('os.listdir(os.getcwd()): ' + str(os.listdir(os.getcwd())))
print('os.path.getsize(os.getcwd()): ' + str(os.path.getsize(os.getcwd())))
print('os.path.split(os.getcwd()): '+ str(os.path.split(os.getcwd())))
print('os.path.basename(os.getcwd()): '+ str(os.path.basename(os.getcwd())))
print('os.path.dirname(os.getcwd()): '+ str(os.path.dirname(os.getcwd())))
print('os.path.isabs(os.getcwd()): '+ str(os.path.isabs(os.getcwd())))
print('os.path.abspath(binder): '+ str(os.path.abspath('binder')))
print('os.path.relpath(os.getcwd,/home/): '+ str(os.path.relpath(os.getcwd(),'/binder/')))
print('os.path.exists(os.getcwd): '+ str(os.path.exists(os.getcwd())))
print('os.path.isfile(/home/jovyan/binder): '+ str(os.path.isfile('/home/jovyan/binder')))
print('os.path.isfile(/home/jovyan/binder/Index.ipynb): '+ str(os.path.isfile('/home/jovyan/binder/Index.ipynb')))
print('os.path.isdir(/home/jovyan/binder): '+ str(os.path.isdir('/home/jovyan/binder')))
print('os.path.isdir(/home/jovyan/binder/Index.ipynb): '+ str(os.path.isdir('/home/jovyan/binder/Index.ipynb')))


#os.getcwd(): /home/jovyan/binder
#os.listdir(os.getcwd()): ['Index.ipynb', 'environment.yml', 'apt.txt', 'Untitled.ipynb', 'Untitled1.ipynb', '.ipynb_checkpoints']
#os.path.getsize(os.getcwd()): 4096
#os.path.split(os.getcwd()): ('/home/jovyan', 'binder')
#os.path.basename(os.getcwd()): binder
#os.path.dirname(os.getcwd()): /home/jovyan
#os.path.isabs(os.getcwd()): True
#os.path.abspath(binder): /home/jovyan/binder/binder
#os.path.relpath(os.getcwd,/home/): ../home/jovyan/binder
#os.path.exists(os.getcwd): True
#os.path.isfile(/home/jovyan/binder): False
#os.path.isfile(/home/jovyan/binder/Index.ipynb): True
#os.path.isdir(/home/jovyan/binder): True
#os.path.isdir(/home/jovyan/binder/Index.ipynb): False
