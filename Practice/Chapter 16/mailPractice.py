#! python3

import smtplib, imapclient, pyzmail, impalib, pprint

#If using TLS connection
smtpTLSobj = smtplib.SMTP('smtp.live.com',25)
smtpTLSobj.ehlo()
smtpTLSobj.starttls() #Should return 220 for successful message
TLSPassword = input('Enter your TLS password for account pushkargarg02@gmail.com')
smtpTLSobj.login('pushkargarg02@gmail.com',TLSPassword) #Should return 235 for successful message
smtpTLSobj.sendmail('pushkargarg02@gmail.com','jn.richa7@gmail.com','Subject: First email.\nHello, This is my first email from TLS SMTP Object.') #Should return an empty dictionary
smtpTLSobj.quit() #Should return 221 for successful message

#If using SSL connection
smtpSSLobj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpSSLobj.ehlo() 
SSLPassword = input('Enter your SSL password for account pushkargarg02@gmail.com')
smtpSSLobj.login('pushkargarg02@gmail.com',SSLPassword) #Should return 235 for successful message
smtpSSLobj.sendmail('pushkargarg02@gmail.com','jn.richa7@gmail.com','Subject: First email.\nHello, This is my first email from SSL SMTP Object.') #Should return an empty dictionary
smtpSSLobj.quit() #Should return 221 for successful message

print('There is no error')

#Here we go for retrieving and deleting the mails
imapObject = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObject.login('pushkargarg02@gmail.com',SSLPassword)
imapObject.list_folders()
'''
[(('\\HasNoChildren',), '/', 'Drafts'),
(('\\HasNoChildren',), '/', 'Filler'),
(('\\HasNoChildren',), '/', 'INBOX'),
(('\\HasNoChildren',), '/', 'Sent'),
--snip--
(('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
(('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]
'''
#Select the folder #readonly True means it will not be marked as read. else pass readoly=False
imapObject.select_folder('INBOX',readonly=True) #imaplib.error if not successful

#Change the size limit if search will return large number of messages
imaplib._MAXLINE = 10000000

#search the keywords which will return unique IDs
allUIDs = imapObject.search(['ALL'])
on5jul2015UIDs = imapObject.search(['ON 05-Jul-2015'])
testUIDs = imapObject.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015','UNSEEN'])
orUIDs = imapObject.search(['OR FROM alice@example.com FROM alicewonderland@example.com'])
'''
Sample Output of search: [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
'''

#We can use gmail_search method which will do fuzzy search
UIDs = imapObject.gmail_search('meaning of life')

rawmessages = imapObject.fetch(UIDs,['BODY[]'])
pprint.pprint(rawmessages)
'''
####Below raw message is in RFC 822 format which is unintelligible. so pyzmail is used for formatting
{40040: {'BODY[]': 'Delivered-To: my_email_address@gmail.com\r\n'
'Received: by 10.76.71.167 with SMTP id '
--snip--
'\r\n'
'------=_Part_6000970_707736290.1404819487066--\r\n',
'SEQ': 5430}}
'''

#actualmessage is a PyzMessage object which has several methods
actualmessage = pyzmail.PyzMessage.factory(rawmessages[40040]['BODY[]'])
print(actualmessage.get_subject())
print(actualmessage.get_addresses('from')) #Return a list of tuples
print(actualmessage.get_addresses('to')) #Return a list of tuples
print(actualmessage.get_addresses('cc')) #Return a list tuples

if actualmessage.text_part != None:
	print(actualmessage.text_part.get_payload().decode(actualmessage.text_part.charset))
	'''
	'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
	'''
if actualmessage.html_part != None:
	print(actualmessage.html_part.get_payload().decode(actualmessage.html_part.charset))
	'''
	'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al
	<br></div>\r\n'
	'''

#How to delete the mails by using the UIDs
imapObject.delete_messages(UIDs)
'''
{40066: ('\\Seen', '\\Deleted')}
'''

#Below command will delete the deleted messages permanently and for gmail it is automatically done when above command is executed
imapObject.expunge()
'''
('Success', [(5452, 'EXISTS')])
'''

#Disconnecting from the IMAP Server
imapObject.logout()

