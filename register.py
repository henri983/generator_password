from tkinter import *
from tkinter import messagebox
import ast  # Pour convertir une chaîne en dictionnaire Python en toute sécurité

# Création de la fenêtre principale
root = Tk()
root.title("Inscription")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)  # Empêche le redimensionnement

def Inscription():
    nom_utilisateur = user.get()
    mot_de_passe = code.get()
    confirmer_mot_de_passe = conform_code.get()

    if mot_de_passe == confirmer_mot_de_passe:
        try:
            with open('datasheet.txt', 'r') as file:
                d = file.read()
                if d.strip() == "":
                    r = {}  # Si fichier vide, créer un dictionnaire vide
                else:
                    r = ast.literal_eval(d)  # Charger les données existantes

            # Ajouter le nouvel utilisateur sans supprimer les anciens
            if nom_utilisateur in r:
                messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà.")
            else:
                r[nom_utilisateur] = mot_de_passe

                with open('datasheet.txt', 'w') as file:
                    file.write(str(r))  # Réécrire toutes les données mises à jour

                messagebox.showinfo("Inscription", "Inscription réussie")
        except FileNotFoundError:
            # Si le fichier n'existe pas, le créer avec la première entrée
            with open('datasheet.txt', 'w') as file:
                file.write(str({nom_utilisateur: mot_de_passe}))
            messagebox.showinfo("Inscription", "Inscription réussie (nouveau fichier créé)")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    else:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")



# Chargement et affichage de l'image
img = PhotoImage(file="login.png")
Label(root, image=img, bg="#fff").place(x=50, y=50)

# Cadre blanc contenant les champs de saisie
frame = Frame(root, width=350, height=390, bg="white")
frame.place(x=480, y=50)

# Titre du formulaire
heading = Label(frame, text="Inscription", bg="white", fg="#57a1f8", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)


# -------------------- Champ nom d'utilisateur --------------------
def on_enter(e):
    user.delete(0, 'end')  # Efface le texte par défaut quand on clique

def on_leave(e): 
    if user.get() == '':
        user.insert(0, "Nom d'utilisateur")  # Remet le texte si champ vide

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")  # Texte par défaut
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)  # Ligne sous le champ


# -------------------- Champ mot de passe --------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e): 
    if code.get() == '':
        code.insert(0, "Mot de passe")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Mot de passe")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


# -------------------- Champ confirmation de mot de passe --------------------
def on_enter(e):
    conform_code.delete(0, 'end')

def on_leave(e): 
    if conform_code.get() == '':
        conform_code.insert(0, "Confirmer le mot de passe")

conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, "Confirmer le mot de passe")
conform_code.bind("<FocusIn>", on_enter)
conform_code.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)


# -------------------- Bouton d'inscription --------------------
Button(frame, width=39, pady=7, text="S'inscrire", bg="#57a1f8", fg="white", border=0, command=Inscription).place(x=35, y=280)

# Texte d'aide et bouton Connexion (non fonctionnel ici)
Label = Label(frame, text="Vous avez déjà un compte ?", bg="white", fg="black", font=("Microsoft YaHei UI Light", 9))
Label.place(x=90, y=340)

Inscription = Button(frame, width=6, text="Connexion", cursor="hand2", bg="white", fg="#57a1f8", border=0)
Inscription.place(x=260, y=340)


# Boucle principale de l'application
root.mainloop()