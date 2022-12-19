
import string

print ('welkom bij dit optel program')
getal1 =int( input('getal1: '))


getal2 =int( input('getal2: '))
bewerking = ( input('de bewerking: '))
if bewerking == '+':
    print(int(getal1+getal2))
elif bewerking == '-':
    print(int(getal1-getal2))
else:
    print('Bewerking is niet ge\xefmplementeerd')

