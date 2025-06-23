from tkinter import *
from tkinter import messagebox
import ast
import string
import random

# --- Fonction inscription ---
def Inscription():
    nom_utilisateur = user.get()
    mot_de_passe = code.get()
    confirmer_mot_de_passe = conform_code.get()

    if (nom_utilisateur == "Nom d'utilisateur" or mot_de_passe == "Mot de passe"
            or confirmer_mot_de_passe == "Confirmer le mot de passe"):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    if mot_de_passe == confirmer_mot_de_passe:
        try:
            with open('datasheet.txt', 'r', encoding='utf-8') as file:
                d = file.read()
                r = {} if d.strip() == "" else ast.literal_eval(d)

            if nom_utilisateur in r:
                messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà.")
            else:
                r[nom_utilisateur] = mot_de_passe
                with open('datasheet.txt', 'w', encoding='utf-8') as file:
                    file.write(str(r))
                messagebox.showinfo("Inscription", "Inscription réussie")
        except FileNotFoundError:
            with open('datasheet.txt', 'w', encoding='utf-8') as file:
                file.write(str({nom_utilisateur: mot_de_passe}))
            messagebox.showinfo("Inscription", "Inscription réussie (nouveau fichier créé)")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")
    else:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")

# --- Génération mot de passe ---
def generer_mot_de_passe(longueur=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def remplir_mot_de_passe():
    mot_de_passe = generer_mot_de_passe()
    code.delete(0, 'end')
    code.insert(0, mot_de_passe)
    code.config(show='*')
    conform_code.delete(0, 'end')
    conform_code.insert(0, mot_de_passe)
    conform_code.config(show='*')

# --- Interface principale ---
root = Tk()
root.title("Inscription")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# Image à gauche (si image login.png présente)
try:
    img = PhotoImage(file="login.png")
    Label(root, image=img, bg="#fff").place(x=50, y=50)
except Exception:
    pass  # Ignore si l'image n'est pas trouvée

frame = Frame(root, width=350, height=470, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="Inscription", bg="white", fg="#57a1f8",
                font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# --- Champ nom d'utilisateur ---
def on_enter_user(e):
    if user.get() == "Nom d'utilisateur":
        user.delete(0, 'end')

def on_leave_user(e):
    if user.get() == '':
        user.insert(0, "Nom d'utilisateur")

user = Entry(frame, width=25, fg="black", border=0, bg="white",
             font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")
user.bind("<FocusIn>", on_enter_user)
user.bind("<FocusOut>", on_leave_user)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# --- Champ mot de passe ---
def on_enter_code(e):
    if code.get() == "Mot de passe":
        code.delete(0, 'end')
        code.config(show="*")

def on_leave_code(e):
    if code.get() == '':
        code.insert(0, "Mot de passe")
        code.config(show="")

code = Entry(frame, width=25, fg="black", border=0, bg="white",
             font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Mot de passe")
code.bind("<FocusIn>", on_enter_code)
code.bind("<FocusOut>", on_leave_code)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# --- Bouton œil mot de passe ---
show_password = False
def toggle_password():
    global show_password
    if show_password:
        code.config(show="*")
        bouton_oeil.config(text="👁️")
        show_password = False
    else:
        code.config(show="")
        bouton_oeil.config(text="👁️‍🗨️")
        show_password = True

bouton_oeil = Button(frame, text="👁️", bg="white", border=0, command=toggle_password)
bouton_oeil.place(x=300, y=150)

# --- Champ confirmation mot de passe ---
def on_enter_confirm(e):
    if conform_code.get() == "Confirmer le mot de passe":
        conform_code.delete(0, 'end')
        conform_code.config(show="*")

def on_leave_confirm(e):
    if conform_code.get() == '':
        conform_code.insert(0, "Confirmer le mot de passe")
        conform_code.config(show="")

conform_code = Entry(frame, width=25, fg="black", border=0, bg="white",
                     font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=230)
conform_code.insert(0, "Confirmer le mot de passe")
conform_code.bind("<FocusIn>", on_enter_confirm)
conform_code.bind("<FocusOut>", on_leave_confirm)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=257)

# --- Bouton œil confirmation ---
show_confirm = False
def toggle_confirm():
    global show_confirm
    if show_confirm:
        conform_code.config(show="*")
        bouton_oeil_confirm.config(text="👁️")
        show_confirm = False
    else:
        conform_code.config(show="")
        bouton_oeil_confirm.config(text="👁️‍🗨️")
        show_confirm = True

bouton_oeil_confirm = Button(frame, text="👁️", bg="white", border=0, command=toggle_confirm)
bouton_oeil_confirm.place(x=300, y=230)

# --- Bouton Générer mot de passe (style amélioré) ---
Button(frame, text="Générer un mot de passe",  command=remplir_mot_de_passe,
        bg="white", fg="#57a1f8", border=0, cursor="hand2").place(x=100, y=280)

# --- Bouton S'inscrire ---
Button(frame, width=39, pady=7, text="S'inscrire", bg="#57a1f8",
       fg="white", border=0, command=Inscription).place(x=35, y=330)

# --- Lien vers Connexion (non actif) ---
Label(frame, text="Vous avez déjà un compte ?", bg="white", fg="black",
      font=("Microsoft YaHei UI Light", 9)).place(x=90, y=390)

Button(frame, width=6, text="Connexion", cursor="hand2", bg="white",
       fg="#57a1f8", border=0).place(x=260, y=390)

# --- Lancement de l'application ---
root.mainloop()
