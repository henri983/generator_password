from tkinter import *
from tkinter import messagebox
import ast  # Pour convertir une chaîne en dictionnaire Python en toute sécurité

# Création de la fenêtre principale
root = Tk()
root.title("Inscription")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


def Inscription():
    nom_utilisateur = user.get()
    mot_de_passe = code.get()
    confirmer_mot_de_passe = conform_code.get()

    if mot_de_passe == confirmer_mot_de_passe:
        try:
            with open('datasheet.txt', 'r') as file:
                d = file.read()
                if d.strip() == "":
                    r = {}
                else:
                    r = ast.literal_eval(d)

            if nom_utilisateur in r:
                messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà.")
            else:
                r[nom_utilisateur] = mot_de_passe

                with open('datasheet.txt', 'w') as file:
                    file.write(str(r))

                messagebox.showinfo("Inscription", "Inscription réussie")
        except FileNotFoundError:
            with open('datasheet.txt', 'w') as file:
                file.write(str({nom_utilisateur: mot_de_passe}))
            messagebox.showinfo("Inscription", "Inscription réussie (nouveau fichier créé)")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    else:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")


# Image de fond
img = PhotoImage(file="login.png")
Label(root, image=img, bg="#fff").place(x=50, y=50)

# Cadre de droite
frame = Frame(root, width=350, height=390, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="Inscription", bg="white", fg="#57a1f8", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# ---------- Champ Nom d'utilisateur ----------
def on_enter_user(e):
    if user.get() == "Nom d'utilisateur":
        user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, "Nom d'utilisateur")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ---------- Champ Mot de passe ----------
def on_enter_code(e):
    if code.get() == "Mot de passe":
        code.delete(0, 'end')
        code.config(show='*')

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, "Mot de passe")
        code.config(show='')

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Mot de passe")
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# ---------- Champ Confirmer le mot de passe ----------
def on_enter_confirm(e):
    if conform_code.get() == "Confirmer le mot de passe":
        conform_code.delete(0, 'end')
        conform_code.config(show='*')

def on_leave_confirm(e):
    if conform_code.get() == '':
        conform_code.insert(0, "Confirmer le mot de passe")
        conform_code.config(show='')

conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, "Confirmer le mot de passe")
conform_code.bind("<FocusIn>", on_enter_confirm)
conform_code.bind("<FocusOut>", on_leave_confirm)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

# ---------- Checkbox pour afficher/masquer les mots de passe ----------
def toggle_password():
    if show_password.get():
        if code.get() != "Mot de passe":
            code.config(show='')
        if conform_code.get() != "Confirmer le mot de passe":
            conform_code.config(show='')
    else:
        if code.get() != "Mot de passe":
            code.config(show='*')
        if conform_code.get() != "Confirmer le mot de passe":
            conform_code.config(show='*')

show_password = BooleanVar()
Checkbutton(frame, text="Afficher le mot de passe", variable=show_password, command=toggle_password,
            bg="white", font=("Microsoft YaHei UI Light", 9)).place(x=30, y=265)

# ---------- Bouton Inscription ----------
Button(frame, width=39, pady=7, text="S'inscrire", bg="#57a1f8", fg="white", border=0, command=Inscription).place(x=35, y=300)

# ---------- Lien Connexion (non fonctionnel pour l'instant) ----------
Label(frame, text="Vous avez déjà un compte ?", bg="white", fg="black", font=("Microsoft YaHei UI Light", 9)).place(x=90, y=340)
Button(frame, width=6, text="Connexion", cursor="hand2", bg="white", fg="#57a1f8", border=0).place(x=260, y=340)

# Lancement de l'application
root.mainloop()
