""" ce module comporte les menus a presenter selon le choix de l'utilisateur le menu1 presente les semestre le menu2 presente les trimestres
"""

def menu1():
    """ le  menu à presenter si l'utilisateur choisir semestre """
    print("""
    1) 1ER SEMESTRE
    2) 2E SEMESTRE 
    """)
    choix=int(input("VOTRE CHOIX??? ")) 
    if choix == 1 :
        return " 1er semestre"
    elif choix== 2 :
        return " 2e semestre"
        


    

def menu2():
    """ le menu à presenter si l'utilisateur choisir trimestre"""
    print("""
    1)1ER TRIMESTRE
    2)2E TRIMESTRE
    3) 3E TRIMESTRE
""")
    choix=int(input("VOTRE CHOIX??? "))
    if choix == 1 :
        return " 1er trimestre"
    elif choix== 2 :
        return " 2e trimestre"
    elif choix == 3 :
        return " 3e trimestre"


    
    


