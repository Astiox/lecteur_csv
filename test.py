import csv
import tkinter as tk
from tkinter import filedialog

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

root = tk.Tk()
root.withdraw()  

chemin_fichier = filedialog.askopenfilename(title="Veuillez sélectionner le fichier CSV à lire", filetypes=[("Fichiers CSV", "*.csv")])

if chemin_fichier:
    donnees = lire_fichier_csv(chemin_fichier)
    for ligne in donnees:
        print(ligne)
else:
    print("Aucun fichier sélectionné.")