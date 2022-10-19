"""
Le chiffrement de César

Ce code de chiffrement est un des plus anciens, dans la mesure où Jules César l'aurait utilisé.

Le principe de codage repose sur l'ajout d'une valeur constante à l'ensemble des caractères du message,
ou plus exactement à leur code ASCII (pour une version "informatique" de ce codage).

Il s'agit donc simplement de décaler l'ensemble des valeurs des caractères du message d'un certain
nombre de positions, c'est-à-dire en quelque sorte de substituer chaque lettre par une autre.

Par exemple, en décalant le message "comment ca marche" de 3 positions, on obtient "frpphqw fd pdufkh".

On appelle "clé" de cryptage ou chiffrement la valeur que l'on ajoute au message pour effectuer le cryptage,
c.-a-d., le nombre de positions à decaler, dans notre cas la clé est 3.

a. Mettre en place un programme qui reçoit une phrase et une clé de cryptage et qui crypte la phrase.
   Regardez les instructions de chr et ord
   Ex : chr(65) et ord("A")

b. Modifiez le programme de manière à ce qu'il soit capable de décrypter un message crypté à l'aide d'une clé de cryptage.
   Saisissez le type d'action à effectuer (chiffrer / déchiffrer)

c. Lorsque l'addition de la valeur donne une lettre dépassant la lettre "z" (ou "a" pour un déplacement négatif),
   continuez simplement à partir de "a" (ou z)
   L'operateur % peux vous être utile
"""


phrase_saisie: str = ""
cle: int = None
phrase_crypter: str = ""
reponse_final: str = ""


def Cryptage(text, key):
    text_return = ""
    for i in text:

        text_return += chr(int(ord(i))+key)

    return text_return


def Decryptage(text, key):
    text_return = ""
    for i in text:
        text_return += chr(int(ord(i))-key)
    return text_return


while True:

    reponse_final = ""
    print("###########################################################################\n\n")
    rep = input(
        "voulez vous quitter l'application (q) crypter (c) ou decrypter (d) ?  : ")

    if (rep == "q"):
        break

    elif (rep == "c"):
        phrase_saisie = input("saisir un phrase a coder en ceasar: ")
        cle = int(input("saisir un clé: "))
        reponse_final = Cryptage(phrase_saisie, cle)
        phrase_crypter = reponse_final
    elif (rep == "d"):
        cle = int(input("saisir un clé: "))
        reponse_final = Decryptage(phrase_crypter, cle)

    print(f"\n\nvotre texte est {reponse_final}")
