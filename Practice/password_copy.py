import sys
import pyperclip

passwords = {'facebook': 'xxxxxx'
             'hotmail' : 'yyyyyy'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' is copied to clipboard.')
else:
    print('There is no account named - ' + account)
