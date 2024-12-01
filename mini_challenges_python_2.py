getal1 = float(input('geef getal 1:  '))
getal2 = float(input('geef getal 2:  '))
#print(type(getal1))
#print(type(getal2))
#str1 = {getal1}
#if str1.isdigit()==True:
#    print("getal1 is een digit")
#else:
#    print ('getal1 is geen digitaal getal')
#val = {getal1}
#print({getal1}.isdigit())
#print(val.isnumeric())
#print('')
if isinstance(getal1, (int, float)):
    print(f"{getal1} is een echt getal")
else:
    print(f"{getal1} is geen echt getal")
if isinstance(getal2, (int, float)):
    print(f"{getal2} is een echt getal")
else:
    print(f"{getal2} is geen echt getal")
