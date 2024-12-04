from tokenize import endpats

leeftijd = int(input('Wat is je leeftijd?:  '))
if leeftijd < 18:
    print(f'Je mag nog niet alleen autorijden' )
    if leeftijd < 16:
        print(f'Helaas, je mag nog geen auto rijden')
    else:
        print(f'Met een rijbewijs mag je onder begeleing auto rijden')

else:
    print(f'Je mag auto rijden als je in bezig bent van een rijbewijs')
