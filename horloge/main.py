import time

def afficher_heure(heure, format_12h=False):
    if format_12h:
        suffixe = "AM" if heure[0] < 12 else "PM"
        heure_affichee = "{:02d}:{:02d}:{:02d} {}".format(heure[0] % 12, heure[1], heure[2], suffixe)
    else:
        heure_affichee = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    print(heure_affichee, end='\r')  # \r permet de revenir au début de la ligne dans le terminal

def regler_alarme(alarme, heure_actuelle):
    if alarme == heure_actuelle:
        print("Réveil ! C'est l'heure de l'alarme.")

def changer_mode_affichage():
    while True:
        choix = input("Choisissez le mode d'affichage (12h/24h) : ").lower()
        if choix in ['12h', '24h']:
            return choix
        else:
            print("Choix non valide. Veuillez entrer '12h' ou '24h'.")

def mettre_en_pause():
    input("Appuyez sur Entrée pour mettre en pause l'horloge...")

def horloge():
    mode_affichage = changer_mode_affichage()

    alarme = tuple(map(int, input("Entrez l'heure de l'alarme (hh:mm:ss) : ").split(':')))

    while True:
        heure_actuelle = time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec

        afficher_heure(heure_actuelle, mode_affichage == '12h')
        regler_alarme(alarme, heure_actuelle)

        time.sleep(1)  # Pause d'une seconde entre les mises à jour de l'heure

if __name__ == "__main__":
    horloge()
