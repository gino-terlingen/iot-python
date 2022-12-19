import random

print("dit is een spelletje hangman")
naam = input("voor je naam in: ")
print("Hey " + naam + " veel geluk")
print("het potje gaat begingen")
print("dit is je woord")

with open('woorden.txt', 'r') as readme:
    readmetxt = readme.readlines()

woord = random.choice(readmetxt)
woord = woord.strip('\n')
length = len(woord)
display = '_' * length
pogingen = 0

letters = []
fouteLetters = []

while True:
    for x in woord:
        if x in letters:
            print(x, end = ' ')
        else:
            print('_', end = ' ')
    letter = input("\nGeef een letter: ")
    if len(letter) == 1:
        if letter in woord:
            print("dit was juist")
            letters.append(letter)
        else:
            if letter not in fouteLetters:
                pogingen += 1
                print(6 - pogingen, "pogingen over")
                fouteLetters.append(letter)            
            else:
                print("dit heb je al gegokt")
            print(fouteLetters)
    else:
        print("dit is geen geldige opgaven")
        print("probeer het opnieuw")
        
    if pogingen == 6:
        print('game over probeer het nog eens')
        print("wil je nog een keer proberen ja/nee")
        janee = input()
        if janee == "ja":
            pogingen = 0
            letters.clear()
            fouteLetters.clear()
            
            print("veel speel plezier")
            continue
        print("tot de volgende keer")
        exit()



