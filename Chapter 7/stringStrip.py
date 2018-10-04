import re

def customizedStrip(inputStringforStripping,whatToStrip=' '):
        stripRegex = re.compile(whatToStrip)
        inputStringforStripping = stripRegex.sub('',inputStringforStripping)
        print('Here is the stripped version: '+ inputStringforStripping + ' ends here')

if __name__ == '__main__':
    inputPasswordforStripping = str(input('Enter the string:'))
    whatToStrip = str(input('Enter the string which you want to strip:'))
    customizedStrip(inputPasswordforStripping,whatToStrip)
