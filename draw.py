# Ce module contient la classe de tirage au sort.
import random
import json

class Draw:
    def __init__(self, teams: list[dict]) -> None:
        # Définissez les attributs dont vous aurez besoin
        #Constructeur de la classe Draw ; param teams: fichier JSON contenant les équipes.
 
        self.teams = teams
        self.chapeaux = {}
        self.matchs_realises = set()
        self.get_chapeaux()

    # Définissez les méthodes dont vous aurez besoin
    #méthode pour répartir les équipes en chapeau

    def get_chapeaux(self) -> None:
        # Organiser les équipes par chapeau
        #chapeaux = {1: [], 2: [], 3: [], 4: []}
        # Parcourir les équipes et ajouter chaque équipe dans le chapeau correspondant
        for team in self.teams:
            chapeau_num = team['chapeau']
            if chapeau_num not in self.chapeaux:
                self.chapeaux[chapeau_num] = []  # Créer une nouvelle liste pour chaque nouveau chapeau
            self.chapeaux[chapeau_num].append(team)

    def tirer_adversaires(self, equipe: dict) -> list[dict]:

        #Effectuer un tirage aléatoire d'adversaires pour une équipe donnée.
        
        adversaires = []
        championnat = equipe['championnat']

        for chapeau_num in self.chapeaux:
            if chapeau_num == equipe['chapeau']:  # On ne tire pas d'équipes du même chapeau
                continue
            
            # Filtrer les équipes du même chapeau qui ne sont pas du même championnat et qui n'ont pas été tirées
            possibles_adversaires = [t for t in self.chapeaux[chapeau_num]
                                     if t['championnat'] != championnat and t['nom'] not in self.matchs_realises]

            if len(possibles_adversaires) >= 2:
                # Tirage de deux équipes : une pour domicile et une pour extérieur
                adversaire_dom = random.choice(possibles_adversaires)
                possibles_adversaires.remove(adversaire_dom)
                adversaire_ext = random.choice(possibles_adversaires)

                #adversaires.append({"adversaire": adversaire_dom['nom'], "lieu": "domicile", "chapeau" : adversaire_dom['chapeau']})
                adversaires.append({
                    "adversaire": adversaire_dom['nom'],
                    "chapeau": adversaire_dom['chapeau'],
                    "lieu": "domicile"
                })
                #adversaires.append({"adversaire": adversaire_ext['nom'], "lieu": "extérieur", "chapeau" : adversaire_ext['chapeau']})
                adversaires.append({
                    "adversaire": adversaire_ext['nom'],
                    "chapeau": adversaire_ext['chapeau'],
                    "lieu": "exterieur"
                })

                # Marquer les adversaires comme ayant déjà été tirés
                self.matchs_realises.add(adversaire_dom['nom'])
                self.matchs_realises.add(adversaire_ext['nom'])

        return adversaires

    def make_draw(self) -> dict:
        # Cette méthode sera celle appelée pour effectuer votre tirage au sort.
        resultats = {}

        for chapeau_num in self.chapeaux:
            for equipe in self.chapeaux[chapeau_num]:
                adversaires = self.tirer_adversaires(equipe)
                resultats[equipe['nom']] = adversaires
        
        return resultats
    print("Tirage au sort effectué")

    def sauvegarder_resultats(self, resultats: dict, tirage: str) -> None:
        #Sauvegarde les résultats dans un fichier JSON.
        #param resultats: Dictionnaire des résultats du tirage.
        #param tirage: fichier de sortie.
        with open(tirage, 'w') as file:
            json.dump(resultats, file, indent=4, ensure_ascii=False)
        print(f"Résultats sauvegardés dans {tirage}")
