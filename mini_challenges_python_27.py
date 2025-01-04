import random

# definieer spel en inzet
def roulette_spel():
    Saldo =100
    print('Je beginsaldo is:', Saldo)
    while Saldo>0:
        inzet = int(input('Hoeveel fiches wil je inzetten?:  '))
        # kies een getal
        gekozen_getal = int(input('Op welke getal ga je gokken?:  '))
        print('Je saldo is:', Saldo)
        if inzet > Saldo:
            print("Je kan niet meer fiches inleggen dan je hebt!")
            continue

        #Geef random getal 0 to 36, zoals op de Roulette
        random_getal = random.randint(0, 36)
        print('Het gevallen getal op de roulette is:', random_getal)

        #definieer de winst
        if gekozen_getal == random_getal:
            Winst = (35*inzet)
            Saldo += Winst
            print('Gefeliciteerd, je hebt deze ronde Gewonnen!!!')
        else:
            Saldo -= inzet
            print('Helaas je hebt niet gewonnen')
        # definieer nieuwe saldo na ronde roullette
#        Saldo =  Winst - inzet
        print("je nieuwe saldo is:", Saldo)

        if Saldo ==0:
            print("Helaas, je kunt niet meer spelen")
            break

        nieuwe_ronde = input("Wil je een nieuwe ronde spelen? (ja/nee): ").lower()
        if nieuwe_ronde != 'ja':
            break

    print("Spel is uit, dank voor het spelen")

# Start the game
roulette_spel()