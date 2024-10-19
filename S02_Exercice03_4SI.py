#4SI : Série N°2 Exercice03 : Création d'un coffre-fort de mots de passe
from pickle import load, dump
from numpy import array
T = array([dict()]*100)

# Crypte un mot de passe passé en paramètre
def CrypterMotDePasse(mdp, cle):
    mdp_chiffre = ""
    for i in range(len(mdp)):
        mdp_chiffre = mdp_chiffre + chr(ord(mdp[i]) + cle)

    return mdp_chiffre

# Vérifie si un libellé existe déjà
def existe(chemin,Libelle):
    f = open(chemin, "rb")
    trouve = False
    eof = False
    while not eof and not trouve:
        try:
            e = load(f)
            if e['libelle'] == Libelle:
                trouve = True
        except:
            eof = True  # Fin de fichier atteinte
    f.close()
    return trouve

# Ajoute un mot de passe dans le fichier
def Ajouter_MDP(chemin, e):
    if not existe(chemin,e['libelle']):
        f = open(chemin, "ab")
        dump(e, f)
        f.close()
    else:
        print(f"Le libellé {e['libelle']} existe déjà.")

# Décrypte un mot de passe passé en paramètre avec la clé de cryptage.
def DecrypterMotDePasse(mdp_chiffre, cle_de_cryptage):
    mdp = ""
    for i in range(len(mdp_chiffre)):
        mdp = mdp + chr(ord(mdp_chiffre[i]) - cle_de_cryptage)

    return mdp

# Affiche un mot de passe en fonction du libellé
def Afficher_MDP(chemin, Libelle):
    if not existe(chemin,Libelle):
        print(f"Le libellé {'Libelle'} existe déjà.")
    else:
        f = open(chemin, "rb")
        eof = False
        while not eof:
            try:
                e = load(f)
                if e['libelle'] == Libelle:
                    print(e['libelle'], ":", DecrypterMotDePasse(e['mot_de_passe'], len(Libelle)))
                    eof = True
            except:
                eof = True      # Fin de fichier atteinte
        f.close()


# Supprime un mot de passe du fichier
def Supprimer_MDP(chemin, Libelle):
    if not(existe(chemin,Libelle)):
        print(f"Le libellé {Libelle} n'existe pas dans le fichier.")
    else:
        f = open(chemin, "rb")
        n = 0
        eof = False
        while not eof:
            try:
                e = load(f)
                if e['libelle'] != Libelle:
                    T[n] = e 
                    n = n + 1
            except:
                eof = True      # Fin de fichier atteinte
        f.close()

        # Réécriture du fichier sans le mot de passe supprimé
        f = open(chemin, "wb")
        for i in range(n):
            dump(T[i],f)
        f.close()

# Trie le fichier de mots de passe
def trier_fichier(chemin):
    T = array([dict()]*100)
    f = open(chemin, "rb")
    n = 0
    eof = False
    while not eof:
        try:
            T[n] = load(f)
            n = n + 1
        except:
            eof = True
    f.close()

    tri_insertion(T,n)

    f = open(chemin, "wb")
    for i in range(n):
        dump(T[i],f)
    f.close()

# Tri par insertion
def tri_insertion(t,n):
    for i in range(1,n):
        aux = t[i]
        j = i 
        while (j>0) and (t[j-1]['libelle']>aux['libelle']):
            t[j] = t[j-1]
            j = j - 1 
        t[j] = aux

# Affiche le contenu du fichier
def afficher_fichier(chemin):
    print("Le contenu du Coffre-fort : ")
    f = open(chemin, "rb")
    eof = False
    while not eof:
        try:
            e = load(f)
            print(e['libelle'], ":", DecrypterMotDePasse(
                e['mot_de_passe'], len(e['libelle'])))
        except:
            eof = True
    f.close()


# Menu pour l'utilisateur
def menu():
    print("\n********* Menu *************")
    print("1 : Ajout d'un mot de passe ")
    print("2 : Récupération d'un mot de passe ")
    print("3 : Suppression d'un mot de passe")
    print("4 : Trier le contenu de coffre-fort")
    print("5 : Afficher le contenu de coffre-fort")
    print("6 : Quittez")
    choix = int(input("Entrez votre choix : "))
    while not(choix in range(1,7)):
        choix = int(input("Entrez un choix entre 1 et 6 : "))
    return choix



#Programme Principal
chemin_fichier =  "coffreFort.dat"
choix = menu()
while not(choix==6):
    match choix:
        case 1: 
            e = dict()
            libelle = input("Entrez le service ou nom d'utilisateur : ")
            mdp = input("Entrez le mot de passe : ")
            e["libelle"]=libelle
            e["mot_de_passe"]=CrypterMotDePasse(mdp, len(libelle))
            Ajouter_MDP(chemin_fichier, e)
        case 2 : 
            Libelle = input("Entrez le service ou nom d'utilisateur à afficher: ")
            Afficher_MDP(chemin_fichier, Libelle)
        case 3 :
            Libelle = input("Entrez le service ou nom d'utilisateur à supprimer : ")
            Supprimer_MDP(chemin_fichier,Libelle)
        case 4 : 
            trier_fichier(chemin_fichier)
        case 5 :
            afficher_fichier(chemin_fichier)
        case 5:
            print("Merci pour votre visite.")
    input("\nAppuez sur une touche Entrée pour revenir au Menu")
    choix = menu()
        

# Notes pédagogiques:
# - Ce code respecte les directives éducatives officielles.
# - Ce code suit les pratiques recommandées pour des raisons d'enseignement.
# A.B.N Academy
