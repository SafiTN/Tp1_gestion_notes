import json
import os

def ajouter_etudiant(id_etudiant, nom, prenom):
    # Chemin du fichier
    etudiants_file = os.path.join("data", "etudiants.json")

    # Charger les données existantes
    with open(etudiants_file, 'r') as f:
        etudiants = json.load(f)

    # Vérifier si l'ID existe déjà
    if any(etudiant["id"] == id_etudiant for etudiant in etudiants):
        print(f"Erreur : L'ID {id_etudiant} est déjà utilisé.")
        return

    # Ajouter le nouvel étudiant
    nouvel_etudiant = {"id": id_etudiant, "nom": nom, "prenom": prenom}
    etudiants.append(nouvel_etudiant)

    # Sauvegarder les modifications
    with open(etudiants_file, 'w') as f:
        json.dump(etudiants, f, indent=4)
    print(f"Étudiant {nom} {prenom} (ID: {id_etudiant}) ajouté avec succès.")

def supprimer_etudiant(id_etudiant):
    # Chemin du fichier
    etudiants_file = os.path.join("data", "etudiants.json")

    # Charger les données existantes
    with open(etudiants_file, 'r') as f:
        etudiants = json.load(f)

    # Vérifier si l'étudiant existe
    etudiant_a_supprimer = next((etudiant for etudiant in etudiants if etudiant["id"] == id_etudiant), None)
    if etudiant_a_supprimer is None:
        print(f"Erreur : L'étudiant avec l'ID {id_etudiant} n'existe pas.")
        return

    # Supprimer l'étudiant
    etudiants.remove(etudiant_a_supprimer)

    # Sauvegarder les modifications
    with open(etudiants_file, 'w') as f:
        json.dump(etudiants, f, indent=4)
    print(f"Étudiant avec l'ID {id_etudiant} supprimé avec succès.")

def afficher_etudiants():
    # Chemin du fichier
    etudiants_file = os.path.join("data", "etudiants.json")

    # Charger les données existantes
    with open(etudiants_file, 'r') as f:
        etudiants = json.load(f)

    # Afficher la liste des étudiants
    if not etudiants:
        print("Aucun étudiant trouvé.")
    else:
        for etudiant in etudiants:
            print(f"ID: {etudiant['id']}, Nom: {etudiant['nom']}, Prénom: {etudiant['prenom']}")