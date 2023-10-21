from pathlib import Path
import time
import datetime


"""def time():
    temps_actuel = time.time()
    temps_formate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(temps_actuel))
    return temps_formate

#print(path,path.exists())
temps_actuel = time.time()
	temps_formate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(temps_actuel))
"""
path=Path.cwd()/"data"

data=[
        "matieres",
        "moyenne",
        "username",
        ]
def create_file(name:str):
    """ cette fonction cree le fichier pour enregistrer le bulletin"""
    file=path/f"{name}.txt"
    file.touch()
    return file
#print(create_file("toti"))

