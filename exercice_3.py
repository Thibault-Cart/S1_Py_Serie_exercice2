"""
Étant donné une séquence d'ADN et une mutation,
on demande de créer un programme pour tester si la séquence d'ADN contient la mutation
    a. si oui, l'algorithme doit afficher la position de la mutation dans la séquence
    b. si non, l'algorithme affiche l'indice -1


Tester votre programme avec les mutations 1, 2, 3 et 4:

MUTATION_1: str = "ctgg"
MUTATION_2: str = "tggu"
MUTATION_3: str = "agct"
MUTATION_4: str = "accg"

"""

""" programme: recherche_mutation
données: séquence d'ADN, mutation
résultat: affiche la position de la mutation
"""

### déclaration et initialisation des variables
SEQ_ADN: str = "ctggtctcacgaccctcgggggaagcttccgctgatttaacctcttggcggggcaaccg"
mutation = ["ctgg","tggu","agct","accg"]
nbmutation:int=0
sortie_text:str=""
### à coder ###
for i in mutation:
    for x in range(len(SEQ_ADN)):
        if(i==SEQ_ADN[x:x+4]):
            nbmutation+=1
            sortie_text+=f"mutation {i} dans l'interval  {x} , {x+4} c'est la {nbmutation} mutation de cette chaine d'adn\n"

print(sortie_text)

