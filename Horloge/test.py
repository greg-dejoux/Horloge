import time
from datetime import datetime

def heure_actuelle():
    while True:
        heure = str(datetime.now().time())
        heure = heure[:-7]
        print(heure)
        time.sleep(1)

#heure_actuelle()

def afficher_heure():
    heure_modifier = [16, 30, 0]
    heure = heure_modifier[0]
    minutes = heure_modifier[1]
    secondes = heure_modifier[2]
    while True:
        secondes= secondes + 1
        if secondes == 60:
            secondes = 0
            minutes = minutes + 1
        if minutes == 60:
            minutes = 0
            heure = heure + 1
        if heure == 24:
            heure = 0
            print(heure + minutes + secondes)
            time.sleep(1)

afficher_heure()