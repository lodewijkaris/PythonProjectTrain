def sinterklaas_verlanglijstje():
    verlanglijstje = []
    print("Typ je wensen voor Sinterklaas. Typ 'klaar' om te stoppen.")

    while True:
        wens = input("Voeg een wens toe: ")
        if wens.lower() == 'klaar':
            break
        verlanglijstje.append(wens)

    verlanglijstje.sort()  # Sorteer de lijst in alfabetische volgorde
    print("\nJe Sinterklaas verlanglijstje in alfabetische volgorde:")
    for wens in verlanglijstje:
        print(f"- {wens}")
