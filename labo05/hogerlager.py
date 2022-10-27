from random import randint
guess = randint(1,1000)
guess_attempts = 0
while True:
    nummer = input("raad een nummer tussen 1 en 1000: ")
    if int (nummer) > guess:
        print("te hoog")
        guess_attempts += 1
    elif int(nummer) < guess:
        print("te laag")
        guess_attempts += 1
    elif int(nummer) == guess:
        print("mooi het is juist")
        break