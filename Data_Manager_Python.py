# Declaration des variables

nom_boutique = "Boutique Informatique"
admin_mot_de_passe = "admin123"
employe_mot_de_passe = "employe123"

nombre_ordinateurs = 0
nombre_cartes_graphiques = 0

ordinateurs = []
cartes_graphiques = []

# Definition des structures

class Ordinateur:
    def __init__(self, nom, marque, stock, claviers, souris, ecran):
        self.nom = nom
        self.marque = marque
        self.stock = stock
        self.claviers = claviers
        self.souris = souris
        self.ecran = ecran

class CarteGraphique:
    def __init__(self, nom, marque, stock):
        self.nom = nom
        self.marque = marque
        self.stock = stock

class Clavier:
    def __init__(self, nom, marque):
        self.nom = nom
        self.marque = marque

class Souris:
    def __init__(self, nom, marque):
        self.nom = nom
        self.marque = marque

class Ecran:
    def __init__(self, nom, marque):
        self.nom = nom
        self.marque = marque

# Fonctions de l'application

def ajouter_ordinateur(nom, marque, stock, claviers, souris, ecran):
    global nombre_ordinateurs
    ordinateur = Ordinateur(nom, marque, stock, claviers, souris, ecran)
    ordinateurs.append(ordinateur)
    nombre_ordinateurs += 1
    print("L'ordinateur", nom, "a ete ajoute a la boutique.")

def afficher_ordinateurs():
    print("Liste des ordinateurs disponibles :")
    for ordinateur in ordinateurs:
        print("Nom :", ordinateur.nom)
        print("Marque :", ordinateur.marque)
        print("Stock :", ordinateur.stock)
        print("-----------------------------")

def afficher_stock_ordinateurs():
    print("Stock des ordinateurs :")
    for ordinateur in ordinateurs:
        print("Ordinateur :", ordinateur.nom)
        print("Stock :", ordinateur.stock)
        print("-----------------------------")

def consulter_ordinateur(nom):
    for ordinateur in ordinateurs:
        if ordinateur.nom == nom:
            print("Details de l'ordinateur", nom)
            print("Marque :", ordinateur.marque)
            print("Stock :", ordinateur.stock)
            return
    print("L'ordinateur", nom, "n'existe pas dans la boutique.")

def mettre_a_jour_stock_ordinateur(nom, stock):
    for ordinateur in ordinateurs:
        if ordinateur.nom == nom:
            ordinateur.stock = stock
            print("Stock de l'ordinateur", nom, "mis a jour :", stock)
            return
    print("L'ordinateur", nom, "n'existe pas dans la boutique.")

def ajouter_carte_graphique(nom, marque, stock):
    global nombre_cartes_graphiques
    carte_graphique = CarteGraphique(nom, marque, stock)
    cartes_graphiques.append(carte_graphique)
    nombre_cartes_graphiques += 1
    print("La carte graphique", nom, "a ete ajoutee a la boutique.")

def afficher_stock_cartes_graphiques():
    print("Stock des cartes graphiques :")
    for carte_graphique in cartes_graphiques:
        print("Carte graphique :", carte_graphique.nom)
        print("Stock :", carte_graphique.stock)
        print("-----------------------------")

def ajouter_clavier(nom, marque):
    clavier = Clavier(nom, marque)
    return clavier

def ajouter_souris(nom, marque):
    souris = Souris(nom, marque)
    return souris

def ajouter_ecran(nom, marque):
    ecran = Ecran(nom, marque)
    return ecran

# Fonction principale

def main():
    print("Bienvenue dans", nom_boutique)
    while True:
        print("-----------------------------")
        print("1. Se connecter en tant qu'administrateur")
        print("2. Se connecter en tant qu'employe")
        print("3. Quitter l'application")
        choix = input("Choisissez une option : ")

        if choix == "1":
            mot_de_passe = input("Mot de passe administrateur : ")
            if mot_de_passe == admin_mot_de_passe:
                administrateur()
            else:
                print("Mot de passe incorrect.")
        elif choix == "2":
            mot_de_passe = input("Mot de passe employe : ")
            if mot_de_passe == employe_mot_de_passe:
                employe()
            else:
                print("Mot de passe incorrect.")
        elif choix == "3":
            print("Merci d'avoir utilise", nom_boutique)
            break
        else:
            print("Choix invalide.")

# Fonctions de l'administrateur

def administrateur():
    while True:
        print("-----------------------------")
        print("1. Ajouter un nouvel ordinateur")
        print("2. Mettre a jour le stock d'un ordinateur")
        print("3. Ajouter une nouvelle carte graphique")
        print("4. Afficher le stock des ordinateurs")
        print("5. Afficher le stock des cartes graphiques")
        print("6. Deconnexion")
        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom de l'ordinateur : ")
            marque = input("Marque de l'ordinateur : ")
            stock = int(input("Stock initial de l'ordinateur : "))

            clavier_nom = input("Nom du clavier : ")
            clavier_marque = input("Marque du clavier : ")
            clavier = ajouter_clavier(clavier_nom, clavier_marque)

            souris_nom = input("Nom de la souris : ")
            souris_marque = input("Marque de la souris : ")
            souris = ajouter_souris(souris_nom, souris_marque)

            ecran_nom = input("Nom de l'ecran : ")
            ecran_marque = input("Marque de l'ecran : ")
            ecran = ajouter_ecran(ecran_nom, ecran_marque)

            ajouter_ordinateur(nom, marque, stock, clavier, souris, ecran)
        elif choix == "2":
            nom = input("Nom de l'ordinateur : ")
            stock = int(input("Nouveau stock de l'ordinateur : "))
            mettre_a_jour_stock_ordinateur(nom, stock)
        elif choix == "3":
            nom = input("Nom de la carte graphique : ")
            marque = input("Marque de la carte graphique : ")
            stock = int(input("Stock initial de la carte graphique : "))
            ajouter_carte_graphique(nom, marque, stock)
        elif choix == "4":
            afficher_stock_ordinateurs()
        elif choix == "5":
            afficher_stock_cartes_graphiques()
        elif choix == "6":
            print("Deconnexion de l'administrateur.")
            break
        else:
            print("Choix invalide.")

# Fonctions de l'employe

def employe():
    while True:
        print("-----------------------------")
        print("1. Afficher le stock des ordinateurs")
        print("2. Afficher le stock des cartes graphiques")
        print("3. Consulter les details d'un ordinateur")
        print("4. Deconnexion")
        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_stock_ordinateurs()
        elif choix == "2":
            afficher_stock_cartes_graphiques()
        elif choix == "3":
            nom = input("Nom de l'ordinateur : ")
            consulter_ordinateur(nom)
        elif choix == "4":
            print("Deconnexion de l'employe.")
            break
        else:
            print("Choix invalide.")

# Appel de la fonction principale
main()
