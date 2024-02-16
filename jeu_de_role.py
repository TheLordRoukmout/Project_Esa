"""
Créer un jeu de rôle,

Définir un personne:
    1. Noms
    2. Sexe
    3. Race ( Humain, Elfe, Nain ou Gnome)
    4. Classe ( Guerrier PV10, Prètre PV8, Voleur PV6, Magicien PV4)
    5. Caractéristique (Attaque et Défense)

    Le programme devra aumoins créer deux personnages ou plus et en choisir 2 au hasards et les faire combattre jusqu'à ce que les pv tombe à zéro.
"""


# Dictionnaire des personnages.
personnages = {

}



# Fonction selection sexe
def selection_sexe():
    choix_sexe = int(input("Liste des sexes : \n\t 1. Masculin \n\t 2. Féminin \n\t 3. Autres \nVotre choix : "))

    match choix_sexe:
        case 1:
            return "Masculin"
        case 2 :
            return "Féminin"
        case 3 :
            return "Autres"
        case _:
            return "Autres"
        
        

# Fonction selection race
def selection_race():
    choix_race = int(input("Liste des races : \n\t 1. Humain \n\t 2. Elfe \n\t 3. Nain \n\t 4. Gnome \nVotre choix : "))

    match choix_race:
        case 1:
            return "Humain"
        case 2:
            return "Elfe"
        case 3:
            return "Nain"
        case 4:
            return "Gnome"
        case _:
            return "Humain"
    


# Fonction selection classe
def selection_classe():
    choix_classe = int(input("Liste des classes : \n\t 1. Guerrier \n\t 2. Prètre \n\t 3. Voleur \n\t 4. Magicien \nVotre choix : "))
    
    match choix_classe:
        case 1:
            return "Guerrier"
        case 2:
            return "Prètre"
        case 3:
            return "Voleur"
        case 4:
            return "Magicien"
        case _:
            return "Guerrier"


        
# Fonction selection caracteristique
def selection_caracteristique():
    choix_caracteristique = int(input("Liste des caracteristiques : \n\t 1. Attaque \n\t 2. Défense \nVotre choix : "))
    
    match choix_caracteristique:
        case 1:
            return "Attaque"
        case 2:
            return "Défense"
        case _:
            return "Attaque"


    
# Fonction générale création de personnage
def création_personnage():
    nom = input("Nommez votre personnage : ")
    sexe = selection_sexe()
    race = selection_race()
    classe = selection_classe()
    caracteristique = selection_caracteristique()
    
    # Modèle dictionnaire des personnages
    nouveau_personnage = {
        "nom" : nom,
        "sexe": sexe,
        "race": race,
        "classe": classe,
        "caracteristique": caracteristique
    }
        
    personnages["personnage " + str(len(personnages)+1)] = nouveau_personnage

def supprimer_personnage(choix_nom):
    del personnages[personnage]
    

def menu_principal():
    choix_menu = int(input("Menu : \n\t 1. Combattre \n\t 2. Créer un personnage \n\t 3. Supprimer un personnage \n\t 4. Quitter \n Votre choix : "))
    
    match choix_menu:
        case 1:
            return print("Combattre")
        case 2:
            création_personnage()
        case 3:
            choix = input("Personnage à supprimer: ")
            supprimer_personnage(choix)
        case 4:
            exit()
        case _:
            exit()



print("Bievenue dans notre Jeux de role")

while True:
    menu_principal()
    print(personnages)