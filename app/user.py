from colorama import Back, Fore, Style
from .util import barre_chargement
from time import sleep
class Etudiant:
    """ la class etudiànt es un objet c'es a dire un etudiant ou un eleve qui utilise l'appication pour calculer ses moyennes scolaire on stocke les info de l'utilisateur ici 
    nom: naturellement le nom de l'etudiant
    class: sa classe frequenter 
    pour pouvoir l'ecrire dans son bulletin a l'entête"""


    def __init__(self,nom,classe):
        self.nom=nom.capitalize()
        self.classe=classe.upper()
    def SePresenter(self):
        """ ici l'etudiant ou l'eleve se presente avec son nom et sa classe"""
        print(Fore.CYAN+f" Nom:{self.nom}\nClasse:{self.classe} "+Fore.RESET)
    
    
def information():
    """ ici cette methode renseigne les information de l'utilisateur"""
    #! le nom de l'uilisateur
    nom=input(Fore.LIGHTBLUE_EX+" Hello 😎 quelle est ton nom? ")
    print(Fore.RESET)
    #! la classe de l'utilisateur
    classe=input(Fore.CYAN+" Quelle est ta classe ?"+ Back.BLACK+Fore.WHITE+" ")
    print(Style.RESET_ALL)
    barre_chargement()
    print(Fore.GREEN+"✓"+Fore.CYAN+"ok",nom,"comme ça vous etes en",classe+" tres bien 😁😁")
    print(Style.RESET_ALL)
    sleep(0.7)

    return nom, classe

