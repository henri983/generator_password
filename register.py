from tkinter import *
from tkinter import messagebox
import mysql.connector
import string
import random
import os
import sys
import subprocess

# --- Connexion à la base de données ---
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # Modifier si besoin
        password="",         # Modifier si besoin
        database="utilisateur_app"
    )

# --- Fonction inscription ---
def Inscription():
    nom_utilisateur = user.get()
    mot_de_passe = code.get()
    confirmer_mot_de_passe = conform_code.get()

    if (nom_utilisateur == "Nom d'utilisateur" or mot_de_passe == "Mot de passe"
            or confirmer_mot_de_passe == "Confirmer le mot de passe"):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    if mot_de_passe != confirmer_mot_de_passe:
        messagebox.showerror("Erreur", "Les mots de passe ne correspondent pas")
        return

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM utilisateurs WHERE nom_utilisateur = %s", (nom_utilisateur,))
        if cursor.fetchone():
            messagebox.showerror("Erreur", "Ce nom d'utilisateur existe déjà.")
        else:
            cursor.execute("INSERT INTO utilisateurs (nom_utilisateur, mot_de_passe) VALUES (%s, %s)",
                           (nom_utilisateur, mot_de_passe))
            conn.commit()
            messagebox.showinfo("Inscription", "Inscription réussie")

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Erreur BDD", f"MySQL : {e}")

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

def ouvrir_connexion():
    root.destroy()
    python_exe = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    try:
        subprocess.Popen([python_exe, script_path])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'ouvrir la page de connexion : {e}")

# --- Interface graphique ---
root = Tk()
root.title("Inscription")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

try:
    img = PhotoImage(file="login.png")
    Label(root, image=img, bg="#fff").place(x=50, y=50)
except:
    pass

frame = Frame(root, width=350, height=470, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="Inscription", bg="white", fg="#57a1f8",
                font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# Nom utilisateur
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

# Mot de passe
def on_enter_pass(e):
    if code.get() == "Mot de passe":
        code.delete(0, 'end')
        code.config(show="*")

def on_leave_pass(e):
    if code.get() == '':
        code.config(show="")
        code.insert(0, "Mot de passe")

code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Mot de passe")
code.bind("<FocusIn>", on_enter_pass)
code.bind("<FocusOut>", on_leave_pass)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Confirmer mot de passe
def on_enter_conform_pass(e):
    if conform_code.get() == "Confirmer le mot de passe":
        conform_code.delete(0, 'end')
        conform_code.config(show="*")

def on_leave_conform_pass(e):
    if conform_code.get() == '':
        conform_code.config(show="")
        conform_code.insert(0, "Confirmer le mot de passe")

conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=230)
conform_code.insert(0, "Confirmer le mot de passe")
conform_code.bind("<FocusIn>", on_enter_conform_pass)
conform_code.bind("<FocusOut>", on_leave_conform_pass)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=257)

# --- Bouton œil pour mot de passe ---
def toggle_password():
 if show_password.get():
     if code.get() != "Mot de passe":
         code.config(show="")
     if conform_code.get() != "Confirmer le mot de passe":
         conform_code.config(show="")
 else:
     if code.get() != "Mot de passe":
         code.config(show="*")
     if conform_code.get() != "Confirmer le mot de passe":
            conform_code.config(show="*")

show_password = BooleanVar()
Checkbutton(frame, text="Afficher le mot de passe", variable=show_password,
           command=toggle_password, bg="white", font=("Microsoft YaHei UI Light",  9)).place(x=100, y=265)
        

# Bouton générer mot de passe
Button(frame, text="Générer un mot de passe", command=remplir_mot_de_passe,
       bg="white", fg="#57a1f8", border=0, cursor="hand2").place(x=100, y=295)

# Bouton S'inscrire
Button(frame, width=39, pady=7, text="S'inscrire", bg="#57a1f8",
       fg="white", border=0, command=Inscription).place(x=35, y=320)

# Lien Connexion
Label(frame, text="Vous avez déjà un compte ?", bg="white", fg="black",
      font=("Microsoft YaHei UI Light", 9)).place(x=90, y=360)

Button(frame, width=6, text="Connexion", cursor="hand2", bg="white",
       fg="#57a1f8", border=0, command=ouvrir_connexion).place(x=260, y=360)

root.mainloop()


