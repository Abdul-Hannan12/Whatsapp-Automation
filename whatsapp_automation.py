import pywhatkit as pwk

try:
    number = input('enter whatsapp number (in proper format with country code) \nExample: +92 332 1234567 \n >> ')
    msg = input('enter the message >> ')
    print('Enter time (hh:mm) :')
    hrs = int(input('hours (hh) >> '))
    mins = int(input('minutes (mm) >> '))
except:
    print('Invalid Input')

pwk.sendwhatmsg(number, msg, hrs, mins)

print('your message has been scheduled! Do not stop this program before the message has been sent.')