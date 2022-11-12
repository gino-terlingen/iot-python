from random import randint

size = 4
trekking = []
while len(trekking) != size:
    t = randint(1, 100)
    if t in trekking:
        continue
    trekking.append(t)
print(trekking) # XXXX remove this line when the program is fully tested!

guess = []
print('Geef ' + str(size) + ' verschillende getallen van 1 tot 100')
for i in range(1, size + 1):
    guess.append(int(input('getal ' + str(i) + ': ')))

score = 0
for n in trekking:
    if n in guess:
        score = score + 1

if score == size:
    print('Je hebt gewonnen!')