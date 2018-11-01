#! python3

import time, pyperclip

print('Press Enter to begin. Afterwards, press Enter to "click" the stopwatch and Ctrl C to quit')
input()
print('Started....')
starttime = time.time()
lasttime = starttime
lapNum = 1
stringtext = ''
copiedtext = ''
try:
	while True:
		input()
		laptime = round(time.time() - lasttime,2)
		totaltime = round(time.time() - starttime,2)
		stringtext = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totaltime).rjust(8), str(laptime).rjust(8))
		print(stringtext,end='')
		copiedtext = '\n' + copiedtext + stringtext 
		lapNum += 1
		lasttime = time.time()
except KeyboardInterrupt:
	pyperclip.copy(copiedtext)
	print('\nDone')
	

