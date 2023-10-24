import sys
import os
sys.path.append("/data/data/com.termux/files/home/storage/shared/Nylock~Dev/dev/projet_moyenne/")
from app import (barre_chargement,
                 calculatrice,
                 canet_matieres,
                 carnet_moyennes
                 ,clear,
                 create_file,
                 data,
                 enregisteur,
                 enregisteur,
                 Etudiant,
                 menu,
                 barre_chargement,
                 information,
                 afficher_heure,
                 play_sound,
                 barre_chargement_advanced



        )
from colorama import Fore, Back, Style
from time import sleep
#------&&utilitaire---------
def complet(path):
    os.path.abspath(path)


art=("""
 █▀▀ █░░█ █▀▀█ █▀▀█ █▀▀▀ █▀▀ █▀▄▀█ █▀▀ █▀▀▄ ▀▀█▀▀  
 █░░ █▀▀█ █▄▄█ █▄▄▀ █░▀█ █▀▀ █░▀░█ █▀▀ █░░█ ░░█░░  
 ▀▀▀ ▀░░▀ ▀░░▀ ▀░▀▀ ▀▀▀▀ ▀▀▀ ▀░░░▀ ▀▀▀ ▀░░▀ ░░▀░░ ........... 
 """)
print(art)
sleep(0.7)

print()
#play_sound(os.path.abspath("./sound/introduction.mp3"))
barre_chargement_advanced()

#sleep(19)
art=("""
╭╮╱╱╱╭━━━╮   ╭━━━╮╭━━━╮╭╮╱╱╱╭━━━╮╭╮╱╭╮╭╮╱╱╱╭━━━╮╭╮╱╭╮╭━━━╮
┃┃╱╱╱┃╭━━╯   ┃╭━╮┃┃╭━╮┃┃┃╱╱╱┃╭━╮┃┃┃╱┃┃┃┃╱╱╱┃╭━━╯┃┃╱┃┃┃╭━╮┃
┃┃╱╱╱┃╰━━╮   ┃┃╱╰╯┃┃╱┃┃┃┃╱╱╱┃┃╱╰╯┃┃╱┃┃┃┃╱╱╱┃╰━━╮┃┃╱┃┃┃╰━╯┃
┃┃╱╭╮┃╭━━╯   ┃┃╱╭╮┃╰━╯┃┃┃╱╭╮┃┃╱╭╮┃┃╱┃┃┃┃╱╭╮┃╭━━╯┃┃╱┃┃┃╭╮╭╯
┃╰━╯┃┃╰━━╮   ┃╰━╯┃┃╭━╮┃┃╰━╯┃┃╰━╯┃┃╰━╯┃┃╰━╯┃┃╰━━╮┃╰━╯┃┃┃┃╰╮
╰━━━╯╰━━━╯   ╰━━━╯╰╯╱╰╯╰━━━╯╰━━━╯╰━━━╯╰━━━╯╰━━━╯╰━━━╯╰╯╰━╯
╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱   ╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱Auteur: TOUSSAINT ╱╱╱╱╱╱╱╱╱╱╱╱╱
""")
print(art)
afficher_heure()
print(Fore.BLUE+" CE PROGRAMME CALCULE TES MOYENNES LISEZ LE FICHIER README POUR PLUS D'INFO")
print(Fore.RESET)

print(" tapez enter pour continuer")
input()
clear()

#play_sound(os.path.abspath("./sound/demander_nom.mp3"))
#sleep(7)
print(Fore.CYAN+" BRO, soit patient avec le programme sinon taura tous plein d'ereur")
print(Fore.RESET)
etudiant=input(Fore.CYAN+" Entrez votre prenom ex (Martial) ")
prenom=etudiant
nom,classe=information()
print(Fore.RESET)
etudiant=Etudiant(nom,classe)
print(Back.CYAN+Fore.GREEN+ " OK "+Style.RESET_ALL)
#play_sound(os.path.abspath("./sound/cycle.mp3"))
#sleep(27)
print(Fore.LIGHTCYAN_EX+" quel est votre cycle scolaire ?\n1) trimestre\n2) semestre")
print(Fore.RESET)


choix=int(input(" quel est votre choix 1 ou 2? "))

if choix == 1:
   choix= menu.menu2()

    
elif choix== 2:
   choix= menu.menu1()
else:
 #   sleep(1.2)
#    play_sound("./sound/erreur.mp3")
    print(Fore.RED+" ERREUR: VEILLEZ TAPEZ 1 OU 2 je vous l'avais dit 😝😝 😎"+Fore.RESET)
    exit()
nbre_matiere_int=0
while nbre_matiere_int==0:

    nbre_matiere=input(Fore.LIGHTCYAN_EX+" Entrez le nombre de matiere "+Fore.RESET)
    try:
        nbre_matiere_int=int(nbre_matiere)
    except ValueError:
        sleep(1.2)
        play_sound(complet("./sound/erreur.mp3"))
        print(Fore.RED+ " ERRUEUR VEILLEZ ENTREZ UNE VALEUR NUMERIQUE PAS DE VIRGULE")
# on recupere les matieres de l'utilisateur 
#play_sound("./sound/carnet_matieres.mp3")
#sleep(19)
matieres=canet_matieres(nbre_matiere_int)
# on recupere les moyennes de chaque matieres
#play_sound("./sound/carnet_moyenne.mp3")
#sleep(18)
liste_moyennes=carnet_moyennes(matieres)

pondere=[]
coefficient=[]
for i in range(len(liste_moyennes)):
    moy= liste_moyennes[i][0]
    coeff=liste_moyennes[i][1]
    coefficient.append(coeff)
    moyennes_pondere=moy*coeff
    pondere.append(moyennes_pondere)  # pondere contient les moyennes ponderes

total,moyenne_general=calculatrice(pondere,coefficient)
fichier=create_file(etudiant.nom)
f=fichier.open(mode="a")
print()
sys.stdout=f
art=("""
╭━━╮╱╭╮╱╭╮╭╮╱╱╱╭╮╱╱╱╭━━━╮╭━━━━╮╭━━╮╭━╮╱╭╮
┃╭╮┃╱┃┃╱┃┃┃┃╱╱╱┃┃╱╱╱┃╭━━╯┃╭╮╭╮┃╰┫┣╯┃┃╰╮┃┃
┃╰╯╰╮┃┃╱┃┃┃┃╱╱╱┃┃╱╱╱┃╰━━╮╰╯┃┃╰╯╱┃┃╱┃╭╮╰╯┃
┃╭━╮┃┃┃╱┃┃┃┃╱╭╮┃┃╱╭╮┃╭━━╯╱╱┃┃╱╱╱┃┃╱┃┃╰╮┃┃
┃╰━╯┃┃╰━╯┃┃╰━╯┃┃╰━╯┃┃╰━━╮╱╱┃┃╱╱╭┫┣╮┃┃╱┃┃┃
╰━━━╯╰━━━╯╰━━━╯╰━━━╯╰━━━╯╱╱╰╯╱╱╰━━╯╰╯╱╰━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
""")
print(art)
print(f"""
                      Nom: {etudiant.nom.upper()} {prenom}
                      classe:{etudiant.classe}
                 \n  """)
for i in range(len(matieres)):
        print(f"{matieres[i]}: {liste_moyennes[i][0]} × {liste_moyennes[i][1]}= {pondere[i]}\n")
print(f"Total:{total}\nMoyenne {choix}:{moyenne_general}")
print()
if moyenne_general ==10:
     print(" ta eu la moyenne c'est deja bon oub :)")
elif moyenne_general == 12:
    print(" wê c'est pas mal bro ")
elif moyenne_general  == 14 or moyenne_general == 15:
    print(" mes felicitations bro tu mange pas riz du chao pour rien")
elif moyenne_general >=16:
    print(" mon vieux toi tes un genie pouahhh mes felicitations")
else:
    print(" ca va allez!!")
print()
afficher_heure()
sys.stdout=sys.__stdout__
print(Fore.LIGHTBLUE_EX+f"OK BRO VA VOIR TON BULLETIN DU {choix} dans {fichier} a bientôt")
print(Fore.RESET)
#play_sound("./sound/fin.mp3")
sleep(1)
clear()
#play_sound("./sound/remerciements.mp3")
#sleep(28)
art=("""
 ⊂ヽ
　 ＼＼  Λ＿Λ
　　 ＼(  ˘ω˘  )
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
  ノ )      Lﾉ
(_／
""")
print(art)
sys.exit("👋👋👋")

