import string
from random import randint, choice
from tkinter import *


def generate_password():
    # Récupération des valeurs minimale et maximale entrées par l'utilisateur
    password_min = 12
    password_max = int(password_max_entry.get())
    all_chars = ""

    # Vérifie que les valeurs minimale et maximale sont correctes
    if password_min > password_max:
        password_entry.delete(0, END)
        password_entry.insert(0, "La valeur minimale doit être inférieure à la valeur maximale")
        return
    if password_min < 0:
        password_entry.delete(0, END)
        password_entry.insert(0, "La valeur minimale ne peut pas être négative")
        return

    # Récupération des choix de l'utilisateur
    if chk_var_letters.get() == 1:
        all_chars += string.ascii_letters
    if chk_var_digits.get() == 1:
        all_chars += string.digits
    if chk_var_special.get() == 1:
        all_chars += string.punctuation

    # Génération du mot de passe
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    # Récupération du mot de passe
    password_entry.delete(0, END)  # .delete permet de remttre à 0
    password_entry.insert(0, password)  # Le boutton insérera le contenu de password

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Création de l'interface graphique

# Création de la fenêtre avec ses paramètres
fenetre = Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("720x480")
fenetre.config(background='#4065A4')

# Création d'une frame (pour mettre le titre de la page)
frame = Frame(fenetre, bg="#4065A4")

# Creer un titre
label_title = Label(frame, text="Générateur de Mot de Passe", font=("Helvetica", 20), bg='#4065A4',fg='black')
label_title.pack()

# Creer un espace entre deux éléments (=texte vide)
label_title = Label(frame, text="", font=("Helvetica", 10), bg='#4065A4',fg='black')
label_title.pack()

# Création des entrées pour les valeurs minimale et maximale
# Creer un text
label_text = Label(frame, text="La taille minimum du mot de passe généré sera de 12 car c'est ce qui est conseillé par l'ANSCII", font=("Helvetica", 10), bg='#4065A4',fg='black')
label_text.pack()
# Creer un text
label_text = Label(frame, text="mais vous pouvez choisir la valeur pour la taille maximale du mot de passe", font=("Helvetica", 10), bg='#4065A4',fg='black')
label_text.pack()
#Input de la valeur maximal
password_max_entry = Entry(frame, font=("Helvetica", 20), bg='#4065A4',fg='black')
password_max_entry.pack(fill=X)

# Creer un espace entre deux éléments (=texte vide)
label_title = Label(frame, text="", font=("Helvetica", 5), bg='#4065A4',fg='black')
label_title.pack()

# Création des cases à cocher pour les choix de l'utilisateur
chk_var_letters = IntVar()
chk_var_digits = IntVar()
chk_var_special = IntVar()
chk_letters = Checkbutton(frame, text="Lettres", variable=chk_var_letters, onvalue=1, offvalue=0, bg='#4065A4')
chk_letters.pack()
chk_digits = Checkbutton(frame, text="Chiffres", variable=chk_var_digits, onvalue=1, offvalue=0, bg='#4065A4')
chk_digits.pack()
chk_special = Checkbutton(frame, text="Caractères spéciaux", variable=chk_var_special, onvalue=1, offvalue=0, bg='#4065A4')
chk_special.pack()

# Creer un espace entre deux éléments (=texte vide)
label_title = Label(frame, text="", font=("Helvetica", 5), bg='#4065A4',fg='black')
label_title.pack()

# Creer un Bouton
generate_password_button = Button(frame, text="Générer", font=("Helvetica", 15), bg='#4065A4', fg='black', command=generate_password)
generate_password_button.pack(fill=X) #Permet de prendre toute la ligne

# Creer un espace entre deux éléments (=texte vide)
label_title = Label(frame, text="", font=("Helvetica", 20), bg='#4065A4',fg='black')
label_title.pack()

# Creer un champs/entrée/input
password_entry = Entry(frame, font=("Helvetica", 15), bg='#4065A4',fg='black')
password_entry.pack(fill=X)

# Afficher la frame
frame.pack(expand=YES)

# Création d'un menu
menu_bar = Menu(fenetre)
quitter_menu = Menu(menu_bar, tearoff=0)
# Permettre de quitter le programme
quitter_menu.add_command(label="Fermer le programme", command=fenetre.quit)
menu_bar.add_cascade(label="Quitter", menu=quitter_menu)

# Ajouter le menu à la fenêtre
fenetre.config(menu=menu_bar)

# Affichage de la fenêtre
fenetre.mainloop()
