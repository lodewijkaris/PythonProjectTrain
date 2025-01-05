#Nachtjes slapen

import datetime
import calendar

# Current date and time
now = datetime.datetime.now()

# Formateer de datum
formatted_date = now.strftime("%Y-%m-%d")
print("Het is nu:", formatted_date)

# Voer jaar, maand en dag in en vraag opnieuw indien ongeldig
def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer. Probeer het opnieuw.")

def datum_input():
    jaar = input_int('Voer een jaar in jjjj:  ')
    maand = input_int('Voer een maand in mm, formaat is een getal tussen 1 en 12 :  ')
    dag = input_int('Voer een dag in dd, formaat een getal tussen 1 tot en met 31:  ')
    return jaar, maand, dag

jaar, maand, dag = datum_input()
print(f"Ingevoerde Jaar: {jaar}, Maand: {maand}, Dag: {dag}")

if 0 <= jaar and 0 < maand < 13 and 0 < dag < 32:  #Check data is binnen range.
    if maand == 1 or maand == 3 or maand == 5 or maand == 7 or maand == 8 or maand == 10 or maand == 12:
        print("Maand met 31 dagen")
    elif maand == 4 or maand == 6 or maand == 9 or maand == 11:
        print("Maand met 30 dagen")
    elif maand == 2:
        print("Maand februari heeft 28 of 29 dagen")
else:
    print("Verkeerde input, stop programma en probeer opnieuw")

if 12 < maand < 1:
    print("Verkeede maand ingevoerd")
else:
    print("Ingevoerde maand is:", maand)
if 32 < dag < 1:
    print("Verkeede dag ingevoerd")
if maand == 2 and dag > 29:
    print("Verkeede dag ingevoerd")
elif dag == 31 and maand == (4 or 6 or 9 or 11):
    print("Verkeede dag ingevoerd")

datum = datetime.datetime(jaar, maand, dag)
print("De samengestelde ingevoerde datum is:", datum.strftime("%Y-%m-%d"))
print("datum is:", datum)

#dagen_verschil = now.strftime("%Y-%m-%d") - datum.strftime("%Y-%m-%d")
dagen_verschil = (now - datum).days

print("het verschil in dagen tussen vandaag en de opgegeven datum is:", dagen_verschil)
if now > datum:
    print(f"De opgegeven datum lag in het verleden, dus -{dagen_verschil} dagen verschil tussen nu en de opgegeven datum")

else:
    print(f"De opgegeven datum ligt in de toekomst, dus +{dagen_verschil} dagen verschil tussen nu en de opgegeven datum")


## oude code

#if maand in list(range(1,13))[::2]:
#    print("Geldige maand met meer dan 30 dagen")
#    num=31
#elif maand in list(range(1,13))[1::2][1:]:
#    print("Geldige maand met 30 dagen")
#    num=30
#elif maand == 2:
#    if calendar.isleap(jaar):
#       print("Month has only 29 days")
#       num=29
#    else:
#       print("Month has only 28 days")
#       num=28
#else:
#    print("Ongeldige maand")
#dag = int(input('Voer een dag in dd, formaat een getal tussen 1 tot en met 31:  '))
#if 0 < dag < num:
#    print("Geldige dag")
#else:
#    print("Ongeldige dag")


#if 12 < maand < 1:
#    print("Verkeede maand ingevoerd")
#else:
#    print("Ingevoerde maand is:", maand)
#dag = int(input('Voer een dag in dd, formaat een getal tussen 1 tot en met 31:  '))
#if 32 < dag < 1:
#    print("Verkeede dag ingevoerd")
#if maand == 2 and dag > 29:
#    print("Verkeede dag ingevoerd")
#elif dag == 31 and maand == (4 or 6 or 9 or 11):
#    print("Verkeede dag ingevoerd")

#def get_valid_date(prompt):
#    while True:
#        date_str = input(jaar,maand,dag)
#        try:
#            return datetime.strptime(date_str, "%Y-%m-%d")
#        except ValueError:
#            print("Ongedeldige datumformaat ingevoerd. Gebruik aub JJJJ-MM-DD.")

#def input_date():
#    year = input_int("Voer het jaar in: ")
#    month = input_int("Voer de maand in (1-12): ")
#    day = input_int("Voer de dag in (1-31): ")
#    return year, month, day

#year, month, day = input_date()
#print(f"Jaar: {year}, Maand: {month}, Dag: {day}")

#jaar = int(input('Voer een jaar in jjjj:  '))
#maand = int(input('Voer een maand in mm, formaat is een getal tussen 1 en 12 :  '))
#dag = int(input('Voer een dag in dd, formaat een getal tussen 1 tot en met 31:  '))

#while True:
#    try:
#        age = int(input("Please enter your age: "))
#    except ValueError:
#        print("Sorry, I didn't understand that.")
#        continue
#    else:
#        break
#    elif jaar % 4 == 0: # Every 4 year "Leap" year occurs so checking...
#        if maand == 2: # In "Leap" year February has 29 days
#            if dag < 30:
#                print("<Correct>")
#            else:
#                print("<Wrong>")
#    elif maand == 2: # But if it's not "Leap" year February will have 28 days
#        if dag < 29:
#            print("<Correct>")
#        else:
#            print("<Wrong>")
#    elif jaar % 4 != 0 and maand != 2: # Otherwise print "Correct"
#        print("<Correct>")

#formatted_date_dag = dagen_verschil.strftime("-%d")
#print("het verschil in dagen tussen vandaag en de opgegeven datum is:", formatted_date_dag)
