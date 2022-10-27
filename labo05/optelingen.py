
from random import randint
score = 0
attempts = 0
while True:
    attempts += 1
    n1 = randint(2, 10)
    n2 = randint(2, 10)
    print('Wat is het product van volgende getallen?\n', n1, n2)
    try:
        answer = int(input('product: '))
    except ValueError:
        print('Ongeldig getal')
        continue
    product = n1 * n2
    if answer == product:
        print('joempie het is juist!')
        score += 1
    else:
        print('fout')

    if score == 2:
        print(f"jouw score is {score}\n in {attempts} pogingen")
        break