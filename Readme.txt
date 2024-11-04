étape de traitement à avoir : exemple de json de la sortie
avoir une idée du rendu final du tirage au sort (sortie)
quel objet va contenir le resultat du tirage au sort
quel objet : liste de dictionnaire


Le tirage concerne qui ?
[
    equipe
]


1- Etape de traitement

- Chaque équipe est une clé dans l'objet JSON.
- Les valeurs sont des listes d'objets, où chaque objet représente un adversaire avec son nom et l'information sur 
le lieu (domicile ou extérieur).
- Si une équipe n'a pas pu être appariée à des adversaires (en raison des contraintes non respectées), 
la liste sera vide.

{
    "equipe" : [
        {
            "Adversaire": "",
            "Lieu": ""
        },

        {
            "Adversaire": ,
            "Lieu": 
        },

        {
            "Adversaire": ,
            "Lieu": 
        },

        {
            "Adversaire": ,
            "Lieu": 
        }
    ]
}


on tire d'abord les chapeau ensuite les équipes

get_teams
get_pots_lists

