from fpdf import FPDF
import json
import os

class DrawPDF(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 12)  # Utiliser DejaVu pour Unicode
        self.cell(0, 10, 'Resultats du Tirage au Sort', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def ajouter_resultats(self, resultats: dict, logos: dict):
        """
        Ajoute les résultats du tirage au PDF avec les logos des équipes et leurs chapeaux.
        :param resultats: Dictionnaire des résultats du tirage.
        :param logos: Dictionnaire des chemins d'accès aux logos.
        """
        self.add_page()
        self.set_font('DejaVu', '', 12)
        
        for equipe, adversaires in resultats.items():
            # Ajouter le logo si disponible
            if equipe in logos and os.path.exists(logos[equipe]):
                self.image(logos[equipe], x=self.get_x(), y=self.get_y(), w=10)
                self.set_x(self.get_x() + 15)
            
            # Ajouter le nom de l'équipe
            self.cell(0, 10, f'Equipe: {equipe}'""", ln=1""")
            
            # Ajouter les adversaires avec leur lieu et leur chapeau
            for adversaire in adversaires:
                self.cell(0, 10, f'  - Adversaire: {adversaire["adversaire"]} (Chapeau {adversaire["chapeau"]}), Lieu: {adversaire["lieu"]}', ln=1)

# Charger les résultats du tirage depuis le fichier JSON
with open("data/resultat_tirage.json", "r") as file:
    resultats = json.load(file)

# Charger les logos des équipes depuis le fichier JSON
with open("data/logos.json", "r") as file:
    logos = json.load(file)

# Générer le PDF
pdf = DrawPDF() 

# Ajouter une police Unicode (DejaVuSans.ttf) dans le dossier "fonts"
pdf.add_font('DejaVu', '', 'fonts/DejaVuSans.ttf', uni=True)
pdf.add_font('DejaVu', 'B', 'fonts/DejaVuSans-Bold.ttf', uni=True)
pdf.add_font('DejaVu', 'I', 'fonts/DejaVuSans-Oblique.ttf', uni=True)

pdf.ajouter_resultats(resultats, logos)
pdf.output("resultats_tirage.pdf")

print("Fichier PDF avec les logos et les chapeaux : resultats_tirage.pdf")
