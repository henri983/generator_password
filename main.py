from tkinter import *
from tkinter import messagebox
import subprocess
import ast  # Pour convertir une chaîne de caractères en dictionnaire Python

# Fonction pour ouvrir le formulaire d'inscription (register.py)
def ouvrir_inscription():
    try:
        subprocess.Popen(["python", "register.py"])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'ouvrir le formulaire d'inscription : {e}")

# Fonction pour afficher automatiquement le mot de passe enregistré lors du focus sur le champ mot de passe
def afficher_mdp(event):
    nom_utilisateur = user.get()
    try:
        with open('datasheet.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            utilisateurs = {} if data.strip() == "" else ast.literal_eval(data)
        if nom_utilisateur in utilisateurs:
            mdp = utilisateurs[nom_utilisateur]
            code_word.delete(0, END)
            code_word.insert(0, mdp)
            code_word.config(show="*")  # Masquer le mot de passe avec des étoiles
        else:
            # Si utilisateur non trouvé, on réinitialise le champ
            code_word.delete(0, END)
            code_word.insert(0, "Mot de passe")
            code_word.config(show="")
    except FileNotFoundError:
        # Si le fichier n'existe pas, on réinitialise le champ
        code_word.delete(0, END)
        code_word.insert(0, "Mot de passe")
        code_word.config(show="")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lecture fichier : {e}")

# Fonction pour basculer l'affichage du mot de passe (voir/cacher)
def toggle_password():
    if show_password.get():
        code_word.config(show="*")  # Masquer
        show_password.set(False)
        bouton_oeil.config(text="👁️")  # Icône pour cacher
    else:
        code_word.config(show="")  # Afficher
        show_password.set(True)
        bouton_oeil.config(text="👁️‍🗨️")  # Icône pour montrer

# Création de la fenêtre principale
root = Tk()
root.title("Connexion")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# Fonction exécutée lorsqu'on clique sur le bouton Connexion
def connexion():
    nom_utilisateur = user.get()
    mot_de_passe = code_word.get()

    try:
        with open('datasheet.txt', 'r', encoding='utf-8') as file:
            data = file.read()
            utilisateurs = {} if data.strip() == "" else ast.literal_eval(data)
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Aucun utilisateur enregistré.")
        return
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lecture fichier : {e}")
        return

    # Vérification des identifiants
    if nom_utilisateur in utilisateurs:
        if utilisateurs[nom_utilisateur] == mot_de_passe:
            # Connexion réussie
            screen = Toplevel(root)
            screen.title("Application")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")

            # ✅ Image d’arrière-plan (indentation corrigée)
            bg_image = PhotoImage(file="background.png")
            background_label = Label(screen, image=bg_image)
            background_label.image = bg_image  # Garde une référence
            background_label.place(x=0, y=0, relwidth=1, relheight=1)

            # Message de bienvenue
            # Créer un label pour afficher le message de bienvenue
            message = f"Bienvenue {nom_utilisateur} !"
            label_bienvenue = Label(screen, text=message, font=("Helvetica", 24, "bold"), fg="#57a1f8", bg="white")
            label_bienvenue.place(x=925, y=50)  # Commence à droite (en dehors de la fenêtre)

            # Fonction pour faire défiler le texte de droite à gauche
            def defiler(x=925):
                if x + label_bienvenue.winfo_reqwidth() > 0:
                    label_bienvenue.place(x=x, y=50)
                    screen.after(20, lambda: defiler(x - 2))  # Vitesse du défilement
                else:
                    # Recommence à droite quand il a disparu à gauche
                    defiler(925)

            # Lancer le défilement
            screen.after(100, defiler)

            # Bouton Déconnexion
            Button(screen, text="Déconnexion", bg="#ff4d4d", fg="white",
                   font=("Microsoft YaHei UI Light", 12),
                   command=screen.destroy).pack(pady=200)
        else:
            messagebox.showerror("Erreur", "Mot de passe incorrect")
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur incorrect")

# Affichage de l'image de gauche
img = PhotoImage(file="login.png")
Label(root, image=img, bg="#fff").place(x=50, y=50)

# Création du cadre de connexion
frame =  Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

# Titre
heading = Label(frame, text="Connexion", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# ------------------ Champ NOM UTILISATEUR ------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e): 
    name = user.get()
    if name == '':
        user.insert(0, "Nom d'utilisateur")

# Entrée du nom d'utilisateur
user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

# Ligne sous le champ
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ------------------ Champ MOT DE PASSE ------------------

def on_enter(e):
    code_word.delete(0, 'end')

def on_leave(e): 
    name = code_word.get()
    if name == '':
        code_word.insert(0, "Mot de passe")
    
# Entrée du mot de passe
code_word = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code_word.place(x=30, y=150)
code_word.insert(0, "Mot de passe")
code_word.bind("<FocusIn>", afficher_mdp)  # Afficher le mot de passe enregistré si l'utilisateur est connu
code_word.bind("<FocusOut>", on_leave)
code_word.config(show="")  # Par défaut, mot de passe visible

# Bouton pour afficher/cacher mot de passe (l'œil)
show_password = BooleanVar(value=False)
bouton_oeil = Button(frame, text="👁️", bg="white", border=0, command=toggle_password)
bouton_oeil.place(x=300, y=150)

# Ligne sous le champ
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# ------------------ BOUTONS ------------------

# Bouton Connexion
Button(frame, width=39, pady=7, text="Connexion", bg="#57a1f8", fg="white", command=connexion, border=0).place(x=35, y=205)

# Texte pour mot de passe oublié
label = Label(frame, text="Mot de passe oublié ?", bg="white", fg="black", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

# Bouton S'inscrire
Inscription = Button(frame, width=6, text="S'inscrire", cursor="hand2", bg="white",
       fg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 9), command=ouvrir_inscription).place(x=215, y=270)

# ------------------ FIN ------------------

# Lancement de la boucle principale Tkinter
root.mainloop()