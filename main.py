import json
from draw import Draw 

# Ouvrir et lire le fichier JSON
with open('data/teams.json', 'r') as f:
    teams = json.load(f)

# Créer une instance de la classe Draw et effectuer le tirage
draw = Draw(teams)
resultats = draw.make_draw()

# Sauvegarder les résultats du tirage dans un fichier
draw.sauvegarder_resultats(resultats, "data/resultat_tirage.json")

# Afficher les résultats
print(json.dumps(resultats, indent=4))

