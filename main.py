from package.ListePays import *
from package.fonctions import *

def main():
    rep = input("Voulez vous faire une partie oui/non: ")
    while rep.lower() == "oui":
        while True:
            levelChoice = int(input("Choississez votre niveau : "))
            if levelChoice == 1:
                levelOne()
            elif levelChoice == 2:
                levelTwo()
            elif levelChoice == 3:
                levelthree()
            else:
                print("Vous avez entre un mauvais choix de niveau")
            break
        rep = input("Voulez vous faire une autre partie oui/non : ")

        print("MERCI D'AVOIR JOUER")
main()