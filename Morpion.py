#######################
#DECLARATION VARIABLES#
#######################
grid =[["", "", ""], #initialisation de la grille
       ["", "", ""],
       ["", "", ""]]

pions = "X"

premier_commence = 0

#######################
#DECLARATION FONCTIONS#
#######################

def joli_tableau(): #creer le tableau
    print(grid[0])
    print(grid[1])
    print(grid[2])


def mode_de_jeu(MDJ):
    if MDJ == "1":
        print("Lancement du mode Humain VS Humain")
    elif MDJ == "2":
        print("Lancement du mode Humain VS IA")
    elif MDJ == "3":
        print("Rage Quit") #rajoutez fonction ou l'on quitte le programme



def victoire(joueur):
    if alignement == True:
        print("Bravo", joueur , " tu a gagné ")



###########################################PROGRAMME############################################


print("Bienvenu dans le jeu de morpion")
print("")

######Mode de Jeu##########

print("Comment voulez-vous jouez? \n [1] Humain VS Humain. \n [2] Humain VS IA. \n [3] en fait... Non.")

MDJ = input("Que voulez vous faire ? [1/2/3] : ") #demande au joueur

while "-" in MDJ or "," in MDJ :
    MDJ = input("Que voulez vous faire ? [1/2/3] : ") # redemande si - ou .

print("")

mode_de_jeu(MDJ)

#######qui commence#########

choix_commence = input("Qui commence ? \n [1] joueur 1 \n [2] joueur 2 \n ---> ") #demande au joueur

while "-" in MDJ or "," in MDJ :
    choix_commence = input("Qui commence ? \n [1] joueur 1 \n [2] joueur 2 \n ---> ") # redemande si - ou .

if choix_commence == "1":
    premier_commence = 1
    print("le joueur qui commence est le joueur 1")
elif choix_commence == "2":
    premier_commence = 2
    print("le joueur qui commence est le joueur 2")


#######Affectation Pion#####

print("")
print("le joueur 1 a le pions X, le joueur 2 a le pions O")
print("")


for idx in range(0, 5): #Commencement de la partie
    if premier_commence==1 :
        pion = "O"
        print("Au tour du joueur 2 , placez un pion: ")
    if premier_commence==2 :
        pion = "X"
        print("Au tour du joueur 1 , placez un pion: ")

    joli_tableau()
    choix_colonne=input("Colonne (1,2 ou 3): ")
    choix_ligne=input("Ligne (1,2 ou 3): ")

    while "." in choix_ligne or "." in choix_colonne or "," in choix_ligne or "," in choix_colonne or "-" in choix_ligne or "-" in choix_colonne:
        choix_colonne=input("Colonne (1,2 ou 3): ")
        choix_ligne=input("Ligne (1,2 ou 3): ")

    if premier_commence=1 and choix_colonne == 1 and choix_ligne == 1:
        grid[0][0]==
    if premier_commence==2 and choix_colonne == 1 and choix_ligne == 1:
        grid[0][0]==
