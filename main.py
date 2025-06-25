from tkinter import *
from tkinter import messagebox
import subprocess
import mysql.connector
import hashlib
import os 
import sys   

# --- Connexion à la base de données ---
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",         # ➜ À adapter selon ton setup
        password="",         # ➜ Mot de passe MySQL
        database="utilisateur_app"
    )

# --- Fonction pour ouvrir le formulaire d'inscription ---
def ouvrir_inscription():
    try:
        subprocess.Popen(["python", "register.py"])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'ouvrir le formulaire d'inscription : {e}")

# --- Fonction de connexion ---
def connexion():
    nom_utilisateur = user.get()
    mot_de_passe = code_word.get()

    try:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT mot_de_passe FROM utilisateurs WHERE nom_utilisateur = %s", (nom_utilisateur,))
        result = cursor.fetchone()

        if result:
            mot_de_passe_bdd = result[0]
            messagebox.showinfo("Mot de passe (hash)", f"Hash stocké : {mot_de_passe_bdd}")

            if verify_password(mot_de_passe_bdd, mot_de_passe):
                # Connexion réussie
                screen = Toplevel(root)
                screen.title("Application")
                screen.geometry("925x500+300+200")
                screen.config(bg="white")

                # Image de fond (optionnelle)
                try:
                    bg_image = PhotoImage(file="background.png")
                    background_label = Label(screen, image=bg_image)
                    background_label.image = bg_image
                    background_label.place(x=0, y=0, relwidth=1, relheight=1)
                except:
                    pass

                # Message de bienvenue
                message = f"Bienvenue {nom_utilisateur} !"
                label_bienvenue = Label(screen, text=message, font=("Helvetica", 24, "bold"), fg="#57a1f8", bg="white")
                label_bienvenue.place(x=925, y=50)

                def defiler(x=925):
                    if x + label_bienvenue.winfo_reqwidth() > 0:
                        label_bienvenue.place(x=x, y=50)
                        screen.after(20, lambda: defiler(x - 2))
                    else:
                        defiler(925)

                screen.after(100, defiler)

                # Déconnexion
                Button(screen, text="Déconnexion", bg="#ff4d4d", fg="white",
                       font=("Microsoft YaHei UI Light", 12),
                       command=screen.destroy).pack(pady=200)
            else:
                messagebox.showerror("Erreur", "Mot de passe incorrect")
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur incorrect")

        cursor.close()
        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Erreur BDD", f"MySQL : {e}")


def verify_password(stored_password, provided_password):
    salt = bytes.fromhex(stored_password[:32])
    stored_hash = stored_password[32:]
    new_hash = hashlib.pbkdf2_hmac('sha256', provided_password.encode(), salt, 100000).hex()
    return new_hash == stored_hash

# --- Interface graphique (identique à ta version) ---
root = Tk()
root.title("Connexion")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# --- Image ---
try:
    img = PhotoImage(file="login.png")
    Label(root, image=img, bg="#fff").place(x=50, y=50)
except:
    pass

# --- Cadre interface ---
frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Connexion", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# --- Champ Nom d'utilisateur ---
def on_enter_user(e):
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

# --- Champ Mot de passe ---
def on_enter_pass(e):
    code_word.delete(0, 'end')
    nom_utilisateur_saisi = user.get().strip()

    if os.path.exists("dernier_utilisateur.txt"):
        with open("dernier_utilisateur.txt", "r") as f:
            lignes = f.read().splitlines()
            for ligne in lignes:
                if ":" in ligne:
                    nom_stocke, mdp_stocke = ligne.split(":", 1)
                    if nom_utilisateur_saisi == nom_stocke:
                        code_word.insert(0, mdp_stocke)
                        code_word.config(show="*")
                        break
def on_leave_pass(e):
    if code_word.get() == '':
        code_word.config(show="")
        code_word.insert(0, "Mot de passe")

code_word = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code_word.place(x=30, y=150)
code_word.insert(0, "Mot de passe")
code_word.bind("<FocusIn>", on_enter_pass)
code_word.bind("<FocusOut>", on_leave_pass)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


# --- Bouton œil ---
show_password = BooleanVar(value=False)
def toggle_password():
    if show_password.get():
        code_word.config(show="*")
        show_password.set(False)
        bouton_oeil.config(text="👁️")
    else:
        code_word.config(show="")
        show_password.set(True)
        bouton_oeil.config(text="👁️‍🗨️")

bouton_oeil = Button(frame, text="👁️", bg="white", border=0, command=toggle_password)
bouton_oeil.place(x=300, y=150)

# --- Bouton Connexion ---
Button(frame, width=39, pady=7, text="Connexion", bg="#57a1f8", fg="white",
       command=connexion, border=0).place(x=35, y=205)

# --- Lien vers inscription ---
Label(frame, text="Pas encore de compte ?", bg="white", fg="black",
      font=("Microsoft YaHei UI Light", 9)).place(x=75, y=270)

Button(frame, width=6, text="S'inscrire", cursor="hand2", bg="white",
       fg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 9),
       command=ouvrir_inscription).place(x=220, y=270)

root.mainloop()
