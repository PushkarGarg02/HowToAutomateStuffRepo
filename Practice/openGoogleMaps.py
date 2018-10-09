'''
Open a browser with copied location in google maps
'''

#! python3

import webbrowser, pyperclip, sys
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
webbrowser.open('https://www.google.com/maps/place/' + address)

'''
Run it using below command for example in Windows (Command Prompt)
D:\Users\703224500\AppData\Local\Programs\Python\Python37-32\Scripts>python.exe
D:\Scripts\openGoogleMaps.py

copied content is '3190 Homestead Rd Santa Clara, CA 95051 USA'
'''
