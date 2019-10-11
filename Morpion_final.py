##################################
#⭐️ DECLARATION DES VARIABLES ⭐️#
##################################

grille=[".", ".", ".", #initialisation de la grille
       ".", ".", ".",
       ".", ".", "."]

gagnant = None #Gagner n'est pas encore possible

joueur_actuel= "X" # Valeur pour le joueur actuel (par exemple un prénom ou joueur 1/2), utilisé pour déterminer le gagnant

jeu_en_cours= True # On initialise la variable pour jeu_en_cours


##################################
#⭐️ DECLARATION DES FONCTIONS ⭐️#
##################################


################### 🎮 JOUER 🎮  ##############################
def jouer(): # Ajout de la fonction jouer
    afficher_grille() # Fonction afficher la grille
    while jeu_en_cours: # Tant que le jeu est en cours
        changement_de_tour(joueur_actuel) # fonction pour passer au tour suivant
        game_over() # fonction de check si game over ou non
        changement_de_joueur() #fonction changer de joueur lorsque changement de tour

    if gagnant == "O" or gagnant == "X": # Trouver le gagant
        print("Le joueur" , gagnant , "à gagné")
    elif gagnant == None: #Si aucun des deux n'a gagné
        print("Dommage vous êtes tout les deux mauvais.")
###################################################################


###################👁‍🗨 L'AFFICHAGE DE LA GRILLE 👁‍🗨##############################
def afficher_grille(): # Ajout de la fonction pour affichier la grille
  print("\n")
  print("  " + grille[6] + " | " + grille[7] + " | " + grille[8] + "     7 | 8 | 9") # A la
  print("  ~~~~~~~~~     ~~~~~~~~~")
  print("  " + grille[3] + " | " + grille[4] + " | " + grille[5] + "     4 | 5 | 6") # manière
  print("  ~~~~~~~~~     ~~~~~~~~~")
  print("  " + grille[0] + " | " + grille[1] + " | " + grille[2] + "     1 | 2 | 3") # d'un numpad
  print("\n")
##########################################################################


########################################✅ LES VERIFICATIONS ✅############################################################

def verifier_ligne(): # Ajout fonction vérification de la ligne
    global jeu_en_cours # Variable global gagnant pour changer toute les occurences partout de la var jeu_en_cours

    ligne1 = grille[6] == grille[7] == grille[8] != "."
    ligne2 = grille[3] == grille[4] == grille[5] != "." # Attribut des valeurs lignes à 3 fois la même valeur différent de "."
    ligne3 = grille[0] == grille[1] == grille[2] != "."

    if ligne1 or ligne2 or ligne3 : # Si l'une des lignes à 3 fois la même valeur différent de "."
        jeu_en_cours=False # Fin de partie

    if ligne1:
        return grille[6] #Renvoyer la premiere valeur de la premiere ligne
    elif ligne2:
        return grille[3] #Renvoyer la premiere valeur de la deuxième ligne
    elif ligne3:
        return grille[0] #Renvoyer la premiere valeur de la troisième ligne
    else:
        return None # Sinon rien retourner


def verifier_colonne():
    global jeu_en_cours # Variable global gagnant pour changer toute les occurences partout de la var jeu_en_cours

    colonne1 = grille[6] == grille[3] == grille[0] != "."
    colonne2 = grille[7] == grille[4] == grille[1] != "." # Si l'une des colonnes à 3 fois la même valeur différent de "."
    colonne3 = grille[8] == grille[5] == grille[2] != "."

    if colonne1 or colonne2 or colonne3 : # Si l'une des colonnes à 3 fois la même valeur différent de "."
        jeu_en_cours=False # Fin de partie

    if colonne1:
        return grille[6] #Renvoyer la premiere valeur de la premiere colonne
    elif colonne2:
        return grille[7] #Renvoyer la premiere valeur de la deuxième colonne
    elif colonne3:
        return grille[8] #Renvoyer la premiere valeur de la troisième colonne
    else:
        return None # Sinon rien retourner



def verifier_diagonale():
    global jeu_en_cours # Variable global gagnant pour changer toute les occurences partout de la var jeu_en_cours

    diagonale1 = grille[6] == grille[4] == grille[2] != "." # Si l'une des diagonales à 3 fois la même valeur différent de "."
    diagonale2 = grille[0] == grille[4] == grille[8] != "."

    if diagonale1 or diagonale2 : # Si l'une des diagonales à 3 fois la même valeur différent de "."
        jeu_en_cours=False # Fin de partie

    if diagonale1:
        return grille[6] #Renvoyer la premiere valeur de la premiere diagonale
    if diagonale2:
        return grille[8] #Renvoyer la deuxième valeur de la premiere diagonale
    else:
        return None # Sinon rien retourner


def game_over(): # Ajout fonction Game Over
    verifier_si_egalite() # Execution fonction vérification égalité
    verifier_si_gagnant() # Execution fonction vérification gagnant


def verifier_si_egalite(): #Ajout de la fonction vérification si égalité
    global jeu_en_cours # Variable global gagnant pour changer toute les occurences partout de la var jeu_en_cours

    if "." not in grille: #Si il n'y a plus de place sur la grille
        jeu_en_cours = False # Fin de partie
        return True # la fonction retourne "true" , il y a donc égalité
    else:
        return False # Sinon la fonction retourne "false" , et il n'y a pas égalité


def verifier_si_gagnant(): # Ajout fonction vérificatin si gagnant
    global gagnant # Variable global gagnant pour changer toute les occurences partout de la var gagnant
    ligne_gagnante = verifier_ligne()
    colonne_gagnante = verifier_colonne()
    diagonale_gagnante = verifier_diagonale()
    if ligne_gagnante: # Si la ligne est gagnante
        gagnant=ligne_gagnante # La variable gagnant aura la valeur X ou O grâce au return de la fonction verif ligne
    elif colonne_gagnante: # Si la colonne est gagnante
        gagnant=colonne_gagnante # La variable gagnant aura la valeur X ou O grâce au return de la fonction verif colonne
    elif diagonale_gagnante: # Si la diagonale est gagnante
        gagnant=diagonale_gagnante # La variable gagnant aura la valeur X ou O grâce au return de la fonction verif diagonale
    else:
        gagnant=None # Sinon aucun gagnant

################################################################################################################################



########################################🔄 LES CHANGEMENTS 🔄############################################################

def changement_de_tour(joueur): # Ajout de la fonction changement de tour par rapport à un joueur
    print("C'est au tour de" , joueur) # A chaque changement de tour , afficher c'est à lui de jouer
    placer_un_pion = input("Choisissez un chiffre sur le numpad: ") # Input pour placer un pion sur la grille (numpad)

    vazy = False # On initialise la variable pour détécter si il y a une erreur de frappe ou un pion déjà présent , de base elle est négative
    while not vazy:
        while placer_un_pion not in ["1","2","3","4","5","6","7","8","9"]: # Tant qu'il ne place pas un pion de cette liste de valeurs
            placer_un_pion = input("Choisissez un chiffre sur le numpad: ") # Lui redemander de rentrer un chiffre

        placer_un_pion = int(placer_un_pion)-1 # On place un pion à la position chiffre-1 car le tableau commence à 0 et non à 1

        if grille[placer_un_pion] == ".": #Si sur la grille il y a un emplacement avec un "."
            vazy = True # Alors c'est ok on peut placer un pion
        else:
            print("Tu essayes de tricher ? Non non non ;) ") # Sinon recommencer avec un autre emplacement de pion

    grille[placer_un_pion] = joueur #Pour placer le pion X ou O en fonction du joueur
    afficher_grille() #Afficher la grille


def changement_de_joueur():
    global joueur_actuel # Variable global gagnant pour changer toute les occurences partout de la var joueur_actuel

    if joueur_actuel == "X": #Si le joueur actuel c'est "X"
        joueur_actuel = "O" # on passe au prochain joueur "O"
    elif joueur_actuel == "O": #Si le joueur actuel c'est "O"
        joueur_actuel = "X" # on passe au prochain joueur "X"

############################################################################################################################


##################################
 #⭐️ Lancement de la partie ⭐️#
##################################

jouer() #Commencement de la partie
