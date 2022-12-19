import random
import time

print("\ndit is een potje gallgje\n")
name = input("voor je naam in: ")
print("Hey " + name + " veel geluk")
time.sleep(2)
print("het potje gaat begingen\n Laten we gaan")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    woorden = open("hangman\\woorden.txt",'r') 
    woordenlijs = woorden.readlines()
    word = random.choice(woordenlijs)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("wil je nog eens? y/n \n")
    while play_game not in ["y", "n","Y","N"]:
        play_game = input("wil je nog eens? y/n\n")
    if play_game == "y":
        main()
    elif play_game == "n":
        print("bendankt voor het spelen tot de volgende keer")
        exit()

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("dit is je woord: " + display + " beging met raden: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("o jee dit is geen geldig opgaven\n")
        hangman()


    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")

    elif guess in already_guessed:
        print("probeer iets anders.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("dit was hem niet " + str(limit - count) + " kansen over\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("nope " + str(limit - count) + " kansen over\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("allee man ik hang bijna " + str(limit - count) + " kansen over\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("ellaba zo niet he nu ist alles of niet komaan laatste kans\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("miljaarde de ju toch ik ben dood\n")
            print("het woord was:",already_guessed,word)
            play_loop()

    if word == '_' * length:
        print("dankjewel om mij te redden")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()