import random

symbol = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]

def test():
    test =  random.choice(symbol)
    return test

playAgain = '0'
balance = input("Avec combien commencez-vous à jouer ? ")

while playAgain.lower() != 'n':

    symb1 = test()
    symb2 = test()
    symb3 =  test()

    print("Votre balance est désormais : ", balance)
    mise = input("Quelle est votre mise ? ")
    while int(mise) > int(balance):
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ")

    balance = int(balance) - int(mise)

    print("Les symboles sont : " + str(symb1) + " / " + str(symb2) + " / " + str(symb3) )

    if symb1 == symb2 == symb3:
        print("Bien joué, vous avez gagné !")
        if symb1 == 1:
            mise = int(mise) * 2
            balance = int(balance) + int(mise)
        if symb1 == 2:
            mise = int(mise) * 3
            balance = int(balance) + int(mise)
        if symb1 == 3:
            mise = int(mise) * 5
            balance = int(balance) + int(mise)
        if symb2 == 4:
            mise = int(mise) * 10
            balance = int(balance) + int(mise)
        if symb2 == 5:
            mise = int(mise) * 20
            balance = int(balance) + int(mise)
        if symb2 == 6:
            mise = int(mise) * 50
            balance = int(balance) + int(mise)
    else:
        print("Vous avez perdu, dommage !")

    playAgain = input("Play Again ( Yes (press Y) or No (press N) ) : ")