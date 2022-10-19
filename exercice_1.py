"""
Créer un programme pour tester si une chaîne de caractére contient un caractère

Toujours utiliser uniquement les structures et les méthodes vues dans le cours.

Exemple:
chaîne: "algo I", caractère: "a", réponse: True
chaîne: "algo I", caractère: "i", réponse: True
chaîne: "algo I", caractère: "u", réponse: False
"""
""" programme : recherche
données: chaîne de caractères -> str, clé -> str
résultat: affiche True si le caractère est dans la chaîne
"""


# declaration et initialisation variable

caractere_rechercher: int = ""
chaine_fourni: int = ""
caractere_est_dans_chaine: bool = False
chaine_fourni: str = input("Saisir la chaine de caractere :")
caractere_rechercher: str = input("Saisir le caractere recherché :")
# logique

for i in chaine_fourni:
    if (caractere_rechercher == i):
        caractere_est_dans_chaine = True

print(caractere_est_dans_chaine)
