import requests
import csv
from datetime import datetime

def recuperer_fichier_csv(url, nom_fichier):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nom_fichier, 'wb') as f:
            f.write(response.content)
        print("Fichier CSV récupéré avec succès.")
        return True
    else:
        print("Erreur lors de la récupération du fichier CSV.")
        return False

def lire_fichier_csv(nom_fichier):
    donnees = []  
    with open(nom_fichier, 'r') as fichier:
        lecteur_csv = csv.reader(fichier, delimiter=';')
        for ligne in lecteur_csv:
            date_heure = ligne[0].split('T') 
            date_heure_formattee = f"{date_heure[0]} {date_heure[1]}" 
            ligne[0] = date_heure_formattee 
            donnees.append(ligne[:10])
    return donnees

# URL du routeur où se trouve le fichier CSV
url_routeur = 'http://adresse_du_routeur/fichier.csv'

# Nom du fichier où vous souhaitez enregistrer le fichier CSV récupéré
nom_fichier_csv = 'fichier_recupere.csv'

# Appeler la fonction pour récupérer le fichier CSV
if recuperer_fichier_csv(url_routeur, nom_fichier_csv):
    # Si la récupération est réussie, lire le fichier CSV
    donnees = lire_fichier_csv(nom_fichier_csv)
    for ligne in donnees:
        print(ligne)
else:
    print("Impossible de récupérer le fichier CSV.")