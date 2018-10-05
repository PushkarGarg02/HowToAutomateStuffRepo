#Script to save the data in the file based on command line arguments
#py.exe mcb.pyw save <keyword>
#py.exe mcb.pyw <keyword>
#py.exe mcb.pyw list
#sys.argv[0] => file name (mcb.pyw)
#sys.argv[1] => save/<keyword>/list/delete
#sys.argv[2] => <keyword>
#sys.argv[2] =

import sys, pyperclip, shelve

mcbshelf = shelve.open('mcb')
if len(sys.argv) == 3: 
    if sys.argv[1].lower() == 'save':
        mcbshelf[sys.argv[2].lower()] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1].lower == 'delete':
        mcbshelf.clear()
    else:
        pyperclip.copy(mcbshelf[sys.argv[1].lower()])
else:
    print('Wrong usage of mcb file!')
    
mcbshelf.close()
