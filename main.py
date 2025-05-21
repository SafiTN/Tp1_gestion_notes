from functions.gestion_etudiants import ajouter_etudiant, supprimer_etudiant, afficher_etudiants
from functions.gestion_notes import ajouter_note, supprimer_note, afficher_notes
from functions.analyse_notes import calculer_moyenne_matiere, calculer_moyenne_generale, afficher_bulletin, trier_etudiants_par_moyenne

def afficher_menu():
    print("\n=== Système de Gestion des Étudiants et Notes ===")
    print("1. Ajouter un étudiant")
    print("2. Supprimer un étudiant")
    print("3. Afficher tous les étudiants")
    print("4. Ajouter une note")
    print("5. Supprimer une note")
    print("6. Afficher les notes d'un étudiant")
    print("7. Calculer la moyenne d'une matière")
    print("8. Calculer la moyenne générale")
    print("9. Afficher le bulletin complet")
    print("10. Trier les étudiants par moyenne générale")
    print("11. Quitter")
    return input("Choisissez une option (1-11) : ")

def main():
    while True:
        choix = afficher_menu()

        if choix == "1":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                nom = input("Entrez le nom : ")
                prenom = input("Entrez le prénom : ")
                ajouter_etudiant(id_etudiant, nom, prenom)
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")

        elif choix == "2":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant à supprimer : "))
                supprimer_etudiant(id_etudiant)
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")

        elif choix == "3":
            afficher_etudiants()

        elif choix == "4":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                matiere = input("Entrez la matière : ")
                note = float(input("Entrez la note (0-20) : "))
                ajouter_note(id_etudiant, matiere, note)
            except ValueError:
                print("Erreur : Veuillez entrer des valeurs valides (ID et note doivent être des nombres).")

        elif choix == "5":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                matiere = input("Entrez la matière : ")
                note = float(input("Entrez la note à supprimer : "))
                supprimer_note(id_etudiant, matiere, note)
            except ValueError:
                print("Erreur : Veuillez entrer des valeurs valides (ID et note doivent être des nombres).")

        elif choix == "6":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                afficher_notes(id_etudiant)
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")

        elif choix == "7":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                matiere = input("Entrez la matière : ")
                moyenne = calculer_moyenne_matiere(id_etudiant, matiere)
                print(f"Moyenne en {matiere} : {moyenne:.2f}")
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")

        elif choix == "8":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                moyenne = calculer_moyenne_generale(id_etudiant)
                print(f"Moyenne générale : {moyenne:.2f}")
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")

        elif choix == "9":
            try:
                id_etudiant = int(input("Entrez l'ID de l'étudiant : "))
                afficher_bulletin(id_etudiant)
            except ValueError:
                print("Erreur : L'ID doit être un nombre.")

        elif choix == "10":
            trier_etudiants_par_moyenne()

        elif choix == "11":
            print("Programme terminé.")
            break

        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 10.")

if __name__ == "__main__":
    main()