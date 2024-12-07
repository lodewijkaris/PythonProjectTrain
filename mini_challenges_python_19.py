from collections import Counter

def verkiezingen():
    gekozen_kandidaat = []
    print("Typ je gekozen kandidaat. Typ 'UITSLAG!' om te stoppen.")

    while True:
        keuze = input("Voeg een kandidaat toe: ")
        gekozen_kandidaat.append(keuze)
        list = gekozen_kandidaat
        def most_frequent(list):
            freq = Counter(list)
            return max (freq, key=freq.get)
        if keuze.lower() == 'uitslag!':
            break


        print(list)

#    def most_frequent(list):
#        freq = Counter(list)
#        return max (freq, key=freq.get)
    print(f"De meest verkozen kandidaat is: {most_frequent(list)}")
# Start het script
verkiezingen()
#def meest_verkozen_kandidaat():
#    meest_verkozen_kandidaat = max(set(list), key = list.count)
#print(meest_verkozen_kandidaat())

#    list = gekozkozen_kandidaat = max(set(gekozen_kandidaat), key=gekozen_kandidaat.count)  # Sorteer de lijst in alfabetische volgorde
#def most_frequent
#    meest_frequent(Lijst):
#    return max(set(Lijst), sleutel=Lijst.aantal)​
#   Lijst = [2, 1, 2, 2, 1, 3]
#    afdrukken(meest_frequent(Lijst))

#def max_occurrences(gekozen_kandidaat):
#    return max(set(gekozen_kandidaat), key = gekozen_kandidaat.count)  # Sorteer de lijst in alfabetische volgorde

#def max_occurrences(gekozen_kandidaat):

#print (meest_gekozen_kandidaat)
    #
#
#    print(f"{max_occurrences(gekozen_kandidaat)}")
#    List =
#    return max(set(gek))
#    print("\nJe gekozen kandidaat in alfabetische volgorde:")
#    for keuze in gekozen_kandidaat:
#        print(f"- {keuze}")
# Start het script
#verkiezingen()

#def sinterklaas_verlanglijstje():
#    verlanglijstje = []
#    print("Typ je wensen voor Sinterklaas. Typ 'klaar' om te stoppen.")

#:
#        wens = input("Voeg een wens toe: ")
#        if wens.lower() == 'klaar':
#            break
#        verlanglijstje.append(wens)

#    verlanglijstje.sort()  # Sorteer de lijst in alfabetische volgorde
#    print("\nJe Sinterklaas verlanglijstje in alfabetische volgorde:")
#    for wens in verlanglijstje:
#        print(f"- {wens}")
# Start het script
#sinterklaas_verlanglijstje()