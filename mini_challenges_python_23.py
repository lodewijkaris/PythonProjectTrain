# Define a dictionary to store names and scores
scores = {}

# Function to add a new score
def add_score(name, score):
    scores[name] = score

# Function to display all scores
def display_scores():
    for name, score in scores.items():
        sorted_by_score = max(scores.items(), key=lambda name: name[1]) #, reverse=True)
#        sorted(score)
#        sorted(score,reverse=True) #, key =lambda x: x[1])
#        score.sort(reverse=True)
#        print(f"{name}: {score}", sorted_by_score)
        print(f"De hoogste score is bereikt door ", sorted_by_score)

# Vraag de gebruiker om het aantal personen dat hij wil invoeren
aantal_personen = int(input("Hoeveel personen wil je invoeren? "))

# Adding some scores
for i in range(aantal_personen):
    name = input(f"Voer persoon {i+1} in: ")
    score = input(f"Voer score van persoon {i+1} in: ")
    float_score = float(score)
    add_score(name,float_score)

# Displaying the scores
#sorted_data =

display_scores()


# Maak een lege lijst om de personen en scores op te slaan
#class persoon:
#    def __init__(self, name):
#        self.persoon = persoon
#      self.score = 0

#    def voegscore_toe(self,punten):
#        self.score += punten

#    def reset_score(self):
#        self.score = 0

#personen = []
#scores = []

# Vraag de gebruiker om het aantal personen dat hij wil invoeren
#aantal_personen = int(input("Hoeveel personen wil je invoeren? "))

# Gebruik een for-lus om de personen in te voeren
#for i in range(aantal_personen):
#    persoon = input(f"Voer persoon {i+1} in: ")
#    score = input(f"Voer score van persoon {i+1} in: ")
#    persoon.append(persoon)
#    score.append(score)
# Print de lijst met ingevoerde personen
# print("De ingevoerde personen zijn:")
#for persoon in personen:
#    print((persoon) + (score))

# Define a dictionary to store names and scores
#scores = {}