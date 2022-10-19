"""
Un palindrome est une chaîne de caractères qui se lit de la même façon dans les deux sens
Exemple :
    "elle"
    "radar"
    "laval"

Ecrire un programme qui vérifie si un mot est un palindrome

Le programme doit afficher 1 si le mot est un palindrome et 0 sinon
"""
#declaration et initialisation
mots:str=input("Mots saisie : ")
longeur_mots=len(mots)

palindrome:bool=None


#logique
if(longeur_mots%2!=0):
    palindrome=False
else:
    for i in range(longeur_mots):
        if(mots[i]==mots[longeur_mots-1-i]):
            palindrome=True
        else:
                palindrome=False


if(palindrome==True):
    print("c'est un palindrome")
else:
    print("c'est PAS un palindrome")