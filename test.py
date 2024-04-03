import csv
import tkinter as tk
from tkinter import filedialog

def lire_fichier_csv(nom_fichier):
    donnees = []  # Liste pour stocker les données
    with open(nom_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier, delimiter=';')  # Spécifier le délimiteur comme point-virgule
        # Lire chaque ligne et ajouter les valeurs des 10 premières colonnes dans la liste de données
        for ligne in lecteur_csv:
            date_heure = ligne[0].split('T')  # Séparer la première colonne en date et heure
            date_heure_formattee = f"{date_heure[0]} {date_heure[1]}"  # Formatage de la date et de l'heure
            ligne[0] = date_heure_formattee  # Remplacer la première colonne par la date formatée
            donnees.append(ligne[:10])
    return donnees

# Créer une fenêtre tkinter
root = tk.Tk()
root.withdraw()  # Cacher la fenêtre principale

# Afficher la boîte de dialogue d'ouverture de fichier
chemin_fichier = filedialog.askopenfilename(title="Veuillez sélectionner le fichier CSV à lire", filetypes=[("Fichiers CSV", "*.csv")])

# Vérifier si l'utilisateur a sélectionné un fichier
if chemin_fichier:
    # Utilisation de la fonction pour lire le fichier CSV spécifié par l'utilisateur
    donnees = lire_fichier_csv(chemin_fichier)

    # Affichage des 10 premières colonnes des données avec la première colonne séparée en date et heure
    for ligne in donnees:
        print(ligne)
else:
    print("Aucun fichier sélectionné.")