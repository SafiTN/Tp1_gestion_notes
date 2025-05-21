import json
import os

def calculer_moyenne_matiere(id_etudiant, matiere):
    notes_file = os.path.join("data", "notes.json")

    try:
        with open(notes_file, 'r') as f:
            content = f.read().strip()
            notes = json.loads(content) if content else {}
    except FileNotFoundError:
        return 0.0
    except json.JSONDecodeError:
        return 0.0

    if str(id_etudiant) not in notes or matiere not in notes[str(id_etudiant)]:
        return 0.0

    notes_liste = notes[str(id_etudiant)][matiere]
    return sum(notes_liste) / len(notes_liste) if notes_liste else 0.0

def calculer_moyenne_generale(id_etudiant):
    notes_file = os.path.join("data", "notes.json")

    try:
        with open(notes_file, 'r') as f:
            content = f.read().strip()
            notes = json.loads(content) if content else {}
    except FileNotFoundError:
        return 0.0
    except json.JSONDecodeError:
        return 0.0

    if str(id_etudiant) not in notes or not notes[str(id_etudiant)]:
        return 0.0

    total_notes = []
    for matiere_notes in notes[str(id_etudiant)].values():
        total_notes.extend(matiere_notes)
    return sum(total_notes) / len(total_notes) if total_notes else 0.0

def afficher_bulletin(id_etudiant):
    notes_file = os.path.join("data", "etudiants.json")
    notes_data_file = os.path.join("data", "notes.json")

    with open(notes_file, 'r') as f:
        etudiants = json.load(f)

    try:
        with open(notes_data_file, 'r') as f:
            content = f.read().strip()
            notes = json.loads(content) if content else {}
    except FileNotFoundError:
        notes = {}
    except json.JSONDecodeError:
        notes = {}

    etudiant = next((e for e in etudiants if e["id"] == id_etudiant), None)
    if not etudiant:
        print(f"Erreur : L'étudiant avec l'ID {id_etudiant} n'existe pas.")
        return

    print(f"\nBulletin de {etudiant['prenom']} {etudiant['nom']} (ID: {id_etudiant})")
    if str(id_etudiant) not in notes or not notes[str(id_etudiant)]:
        print("Aucune note enregistrée.")
        return

    for matiere, notes_liste in notes[str(id_etudiant)].items():
        moyenne = calculer_moyenne_matiere(id_etudiant, matiere)
        print(f"{matiere} : Notes = {notes_liste}, Moyenne = {moyenne:.2f}")
    moyenne_generale = calculer_moyenne_generale(id_etudiant)
    print(f"Moyenne générale : {moyenne_generale:.2f}")

def trier_etudiants_par_moyenne():
    etudiants_file = os.path.join("data", "etudiants.json")
    notes_file = os.path.join("data", "notes.json")

    with open(etudiants_file, 'r') as f:
        etudiants = json.load(f)

    try:
        with open(notes_file, 'r') as f:
            content = f.read().strip()
            notes = json.loads(content) if content else {}
    except FileNotFoundError:
        notes = {}
    except json.JSONDecodeError:
        notes = {}

    # Calculer la moyenne générale pour chaque étudiant
    etudiants_avec_moyennes = []
    for etudiant in etudiants:
        id_etudiant = etudiant["id"]
        moyenne = calculer_moyenne_generale(id_etudiant)
        etudiants_avec_moyennes.append((etudiant["prenom"], etudiant["nom"], moyenne))

    # Trier par moyenne générale (descendant)
    etudiants_avec_moyennes.sort(key=lambda x: x[2], reverse=True)

    # Afficher le classement
    print("\nClassement des étudiants par moyenne générale :")
    for prenom, nom, moyenne in etudiants_avec_moyennes:
        print(f"{prenom} {nom} : Moyenne = {moyenne:.2f}")