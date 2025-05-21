import json
import os

def ajouter_note(id_etudiant, matiere, note):
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
        with open(notes_file, 'w') as f:
            json.dump(notes, f)
    except json.JSONDecodeError:
        notes = {}
        with open(notes_file, 'w') as f:
            json.dump(notes, f)

    if not any(etudiant["id"] == id_etudiant for etudiant in etudiants):
        print(f"Erreur : L'étudiant avec l'ID {id_etudiant} n'existe pas.")
        return

    if not (0 <= note <= 20):
        print("Erreur : La note doit être entre 0 et 20.")
        return

    if str(id_etudiant) not in notes:
        notes[str(id_etudiant)] = {}
    if matiere not in notes[str(id_etudiant)]:
        notes[str(id_etudiant)][matiere] = []
    if float(note) not in notes[str(id_etudiant)][matiere]:
        notes[str(id_etudiant)][matiere].append(float(note))

    with open(notes_file, 'w') as f:
        json.dump(notes, f, indent=4)

    print(f"Note {note} ajoutée pour l'étudiant {id_etudiant} en {matiere}.")

def supprimer_note(id_etudiant, matiere, note):
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
        with open(notes_file, 'w') as f:
            json.dump(notes, f)
    except json.JSONDecodeError:
        notes = {}
        with open(notes_file, 'w') as f:
            json.dump(notes, f)

    if not any(etudiant["id"] == id_etudiant for etudiant in etudiants):
        print(f"Erreur : L'étudiant avec l'ID {id_etudiant} n'existe pas.")
        return

    if str(id_etudiant) not in notes or matiere not in notes[str(id_etudiant)]:
        print(f"Erreur : Aucune note trouvée pour l'étudiant {id_etudiant} en {matiere}.")
        return

    if float(note) not in notes[str(id_etudiant)][matiere]:
        print(f"Erreur : La note {note} n'existe pas pour l'étudiant {id_etudiant} en {matiere}.")
        return

    notes[str(id_etudiant)][matiere].remove(float(note))

    if not notes[str(id_etudiant)][matiere]:
        del notes[str(id_etudiant)][matiere]
        if not notes[str(id_etudiant)]:
            del notes[str(id_etudiant)]

    with open(notes_file, 'w') as f:
        json.dump(notes, f, indent=4)

    print(f"Note {note} supprimée pour l'étudiant {id_etudiant} en {matiere}.")

def afficher_notes(id_etudiant):
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

    if not any(etudiant["id"] == id_etudiant for etudiant in etudiants):
        print(f"Erreur : L'étudiant avec l'ID {id_etudiant} n'existe pas.")
        return

    if str(id_etudiant) not in notes or not notes[str(id_etudiant)]:
        print(f"Aucune note trouvée pour l'étudiant avec l'ID {id_etudiant}.")
        return

    print(f"Notes de l'étudiant ID {id_etudiant} :")
    for matiere, notes_liste in notes[str(id_etudiant)].items():
        print(f"{matiere} : {notes_liste}")