#naam = input('Wat is je naam:  ')
#prijs = float(input('Wat is de prijs: '))
#print(f'jouw naam is {naam}')
#print(f'de prijs is {prijs}')
#naam = input('Wat is je naam:  ')
#leeftijd = int(input('Wat is jouw leeftijd?: '))
#def leeftijd_als_100():
#    jarig_geweest = input("Ben je al jarig geweest dit jaar (True/False)?")
#ben_je_al_jarig_geweest_dit_jaar = (input(bool('Ben je al jarig geweest dit jaar (True/False):'))
#    print (jarig_geweest)
#    if jarig_geweest == "False":
#        #return False
#        leeftijd_als_100() = (99 - leeftijd) + 2024
        #print(f'jij, {naam}, wordt (of bent geworden) in {leeftijd_als_100} 100 jaar oud')
#    if jarig_geweest == "True":
        #return True
#        leeftijd_als_100() = (100-leeftijd) + 2024
#    return leeftijd_als_100

#return leeftijd_als_100()
#leeftijd_als_100()

#print(f'jij, {naam}, wordt (of bent geworden) in {leeftijd_als_100()} 100 jaar oud')

from datetime import date

# Functie om het jaar te berekenen
def jaar_100_worden(geboortejaar, is_al_jarig_geweest):
    huidige_jaar = date.today().year
    if not is_al_jarig_geweest:
        # Als je dit jaar nog niet jarig bent geweest, reken volgend jaar mee
        geboortejaar += 1
    return geboortejaar + 100

# Input: geboortejaar en of je dit jaar al jarig bent geweest
geboortejaar = int(input("Wat is je geboortejaar? "))
is_al_jarig_geweest = input("Ben je dit jaar al jarig geweest? (ja/nee) ").strip().lower() == "ja"

# Resultaat
jaar = jaar_100_worden(geboortejaar, is_al_jarig_geweest)
print(f"Je wordt 100 jaar in het jaar {jaar}.")
