personnages = {
    "perso_1":{
        "nom" : "dym",
        "sexe": "homme",
        "race": "gobelin",
        "classe": "guerrier",
        "caracteristique": "atq"
    },
    "perso_2":{
        "nom" : "Alex",
        "sexe": "Autre",
        "race": "Humain",
        "classe": "mage",
        "caracteristique": "def"
    }
}

print(personnages)

check_perso = int(input("Entrez le perso que vous voulez supprimer:"))

if check_perso == 1:
    del personnages["perso_1"]
elif check_perso == 2:
    del personnages["perso_2"]

print(personnages)