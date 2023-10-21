from colorama import Fore,Back, Style
from .util import barre_chargement

""" l'enregistreur  note les matières ensuite leurs moyenne et coefficient  dans une liste
"""

def canet_matieres(n):
    """ carnet de matieres eregistres uniquement les matieres de l'utilisateur
    :param int n: represente le nombre de matieres 
    :returns: une liste contenant les matieres de l'etudiant

    """
    # on itere sur le nombre de matieres pour pouvoir les enregistrer avec un petit retour de chariot
    carnet_matieres=[]
    print(" entrez vos differentes matières une par une ")

    for _ in range(n):
            
        matieres=input(Style.BRIGHT+" >>  "+Style.RESET_ALL)
        carnet_matieres.append(matieres)
    barre_chargement()
    print(Fore.GREEN+" vos matieres on bien été enregisté"+Fore.RESET)
    return carnet_matieres

def carnet_moyennes(matieres:list):
    """ carnet des moyennes de chaque matieres
    :param list matieres: constitue les matieres de l'utilisateur retourné par la fonction carnet_matieres
    """
    moyennes=[]
    for matiere in matieres:
        contener=[]   # contener ressence la moyenne et le coefficient
        try:
            moyenne=float( input(Fore.CYAN+" entrez la moyenne pour {} ".format(matiere)+Fore.RESET))
            coeff=int(input(" entrez le coefficient "))
        except ValueError:
            print(Back.YELLOW+Fore.RED+" ERREUR: vous devez entrez une valeur numerique"+Style.RESET_ALL)
            exit()
        contener.append(moyenne)
        contener.append(coeff)
        moyennes.append(contener)
    return moyennes


