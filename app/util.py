from time import sleep
import os
from colorama import Fore, Style
import time
import subprocess

def afficher_heure():
    # Utilisez Fore.GREEN pour définir la couleur du texte en vert
    heure_actuelle = time.strftime("%H:%M:%S")
    texte_colore = f"{Fore.GREEN}{heure_actuelle}{Style.RESET_ALL}"

    # Affichez l'heure actuelle en vert
    print(texte_colore)

# Appel de la fonction pour afficher l'heure verte

def barre_chargement():
    """ cette fonction fournir une barre de chargement personalisé"""
    frames=["/","-","\\"]
    for _ in range(2):
        for frame in frames:
            print(frame,end="\r")
            sleep(0.2)
#barre_chargement()       

def clear():
    # Déterminez le système d'exploitation
    systeme = os.name

    # Efface le terminal en fonction du système d'exploitation
    if systeme == "posix":  # Pour les systèmes Unix/Linux/Mac
        os.system("clear")
    elif systeme == "nt":   # Pour les systèmes Windows
        os.system("cls")
    else:
        print("Système d'exploitation non pris en charge : Impossible d'effacer le terminal.")

# Appel de la fonction pour effacer le terminal
#effacer_terminal() 

def barre_chargement_advanced():
    frames=("□□□□□0%"," ■□□□□20%","■■□□□40%","■■■□□60%","■■■■□80%","■■■■□90%","■■■■■100%")
    for frame in frames:
        print(frame,end="\r")
        sleep(1)


def clock():
    clocks=("🕐","🕑","🕒","🕓","🕔","🕕","🕜","🕦","🕧","🕛")
    for _ in range (2):
        for clock in clocks:
            print(clock,end="\r")
            sleep(0.3)

def play_sound(audio):
    import os
    out=open('out.txt','a')
    
# Remplacez 'chemin/vers/votre/fichier/audio.mp3' par le chemin de votre propre fichier audio
    audio_file = audio

# Utilise la commande système pour jouer le fichier audio
    #os.system(f"start {audio_file}")  # Sur Windows
    # os.system(f"afplay {audio_file}")  # Sur macOS
    subprocess.Popen(["mpv",audio_file],stdout=out,stderr=out)  # Sur termux (installer la commande mpv))
    out.close()

if __name__=="__main__":
    clock()
    barre_chargement_advanced()
