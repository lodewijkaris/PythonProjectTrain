from datetime import datetime

#geboortedatum = int(input('Wat is je geboortedatum?:  '))

print("Aan de hand van uw leeftijd gaan we kijken of u mag motorrijden")
def get_valid_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Ongedeldige datumformaat ingevoerd. Gebruik aub JJJJ-MM-DD.")

# Function to calculate age
def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Ask the user for their birthdate
birthdate = get_valid_date("Voeg (daarom) uw geboortedatum in (JJJJ-MM-DD): ")
age = calculate_age(birthdate)

print(f"Je leeftijd is: {age}")

if age >= 18:
    print("Je mag motorrijden indien je een motorrijbewijs hebt en verzekerd bent")
else:
    print("Je mag nog geen motorrijden")