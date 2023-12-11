from package.ListePays import *
import random

def levelOne():
    score = 0
    for i in range(10):
        KeyGenerate = random.choice(list(ListPaysOne.keys()))
        countryCapital = ListPaysOne[KeyGenerate]
        guess = input(KeyGenerate)
        if guess.lower() == countryCapital.lower():
            print("BRAVOOO!!!!! vous avez reussi")
            score+=1
        else:
            print("ECHEC!! vous n'avez pas trouver la bonne reponse")
            print("La bonne reponse est",countryCapital)
    print("votre score est de : ", score)

def levelTwo():
    score = 0
    count = 0
    for i in range(10):
        KeyGenerate = random.choice(list(ListPaysTwo.keys()))
        countryCapital = ListPaysTwo[KeyGenerate]
        guess = input(KeyGenerate)
        if guess.lower() == countryCapital.lower():
            print("BRAVOOO!!!!! vous avez reussi")
            score+=1
        else:
            print("ECHEC!! vous n'avez pas trouver la bonne reponse")
            print("La bonne reponse est",countryCapital)
    print("votre score est de : ", score)


def levelthree():
    score = 0
    for i in range(10):
        KeyGenerate = random.choice(list(ListPaysThree.keys()))
        countryCapital = ListPaysThree[KeyGenerate]
        guess = input(KeyGenerate)
        if guess.lower() == countryCapital.lower():
            print("BRAVOOO!!!!! vous avez reussi")
            score+=1
        else:
            print("ECHEC!! vous n'avez pas trouver la bonne reponse")
            print("La bonne reponse est",countryCapital)
    print("votre score est de : ", score)

