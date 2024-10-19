# Module pour vérifier si une phrase contient uniquement des lettres majuscules et des espaces
def verif_phrase(ch):
    i = 0
    while i < len(ch) and ("A" <= ch[i] <= "Z" or ch[i] == " "):
        i = i + 1
    return i == len(ch)

# Module pour saisir les phrases dans "message.txt"
def saisir_phrases(nom_fichier1):
    f = open(nom_fichier1, "w")
    choix = "O"
    while choix == "O":
        phrase = input("Saisir une phrase (max 50 caractères, lettres majuscules et espaces) : ")
        while not (0 < len(phrase) <= 50 and verif_phrase(phrase)):
            phrase = input("Erreur! Saisir une phrase valide (max 50 caractères, lettres majuscules et espaces) : ")
        
        f.write(phrase + "\n")
        choix = input("Voulez-vous ajouter une autre phrase ? (O/N) : ").upper()
        while not (choix == "O" or choix == "N"):
            choix = input("Veuillez répondre par 'O' pour Oui ou 'N' pour Non : ").upper()
    
    f.close()

# Module pour saisir la clé de cryptage
def saisir_cle():
    cle = input("Saisir une clé de cryptage (50 chiffres) : ")
    while not (len(cle) == 50 and cle.isdecimal()):
        cle = input("Erreur! Saisir une clé de cryptage valide (50 chiffres) : ")
    return cle

# Module pour crypter une phrase avec une clé donnée
def crypter_phrase(ch, cle):
    resultat = ""
    for i in range(len(ch)):
        if ch[i] == " ":
            resultat = resultat + " "
        else:
            k = ord(ch[i]) - 64  # Convertir la lettre en sa position dans l'alphabet (A=1, B=2, ..., Z=26)
            c = int(cle[i])  # Obtenir la valeur du chiffre de la clé
            j = k + c  # Calculer la nouvelle position
            if j > 26:  # Revenir au début de l'alphabet si nécessaire
                j = j - 26
            resultat = resultat + chr(j + 64)  # Convertir la position en lettre
    return resultat

# Module pour crypter les phrases du fichier
def crypter_fichier(nom_fichier1, nom_fichier2, cle):
    f1 = open(nom_fichier1, "r")
    f2 = open(nom_fichier2, "w")
    
    ch = f1.readline()  # Lire la première ligne
    while ch != "":  # Tant qu'il reste des lignes à lire
        ch = ch[:len(ch)-1]  # Enlever le caractère de retour à la ligne '\n'
        phrase_cryptee = crypter_phrase(ch, cle)  # Crypter la ligne
        f2.write(phrase_cryptee + "\n")  # Écrire la phrase cryptée dans le fichier de sortie
        ch = f1.readline()  # Lire la ligne suivante
    
    f1.close()
    f2.close()

# Programme principal
nom_fichier1 = "message.txt"
nom_fichier2 = "crypt.txt"
saisir_phrases(nom_fichier1)
ch_cle = saisir_cle()
crypter_fichier(nom_fichier1, nom_fichier2, ch_cle)

# Notes pédagogiques:
# - On évite les fonctionnalités non enseignées comme "with", "strip()" et les indices négatifs.
# - Le programme est conçu pour respecter les notions de base enseignées.
# A.B.N Academy