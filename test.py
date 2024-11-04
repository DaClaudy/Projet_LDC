import json
import random
from draw import Draw 

# Ouvrir et lire le fichier JSON
with open('teams.json', 'r') as f:
    teams = json.load(f)

# Organiser les équipes par chapeau
chapeaux = {1: [], 2: [], 3: [], 4: []}
for team in teams:
    chapeaux[team['chapeau']].append(team)

# Fonction simple de tirage au sort sans condition, en sélectionnant deux équipes au hasard dans chaque chapeau
def simple_tirage(chapeaux):
    resultats = {}
    for chapeau_num in chapeaux:
        for equipe in chapeaux[chapeau_num]:
            adversaires = random.sample(teams, 2)  # Sélectionner deux adversaires aléatoirement
            resultats[equipe['nom']] = [
                #"chapeau" : equipe['chapeau'],
                {"adversaire": adversaires[0]['nom'], "lieu": "domicile", "chapeau" : adversaires[0]['chapeau']},
                {"adversaire": adversaires[1]['nom'], "lieu": "exterieur", "chapeau" : adversaires[1]['chapeau']}
            ]
    return resultats

# Réaliser le tirage
resultat_tirage_simple = simple_tirage(chapeaux)
with open('tirage.json', 'w') as f:
   json.dump(resultat_tirage_simple, f, indent=4)

# Afficher le résultat sous forme de JSON formaté
print(json.dumps(resultat_tirage_simple, indent=4))