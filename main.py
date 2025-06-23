from tkinter import *
from tkinter import messagebox
import subprocess
import ast

def ouvrir_inscription():
    try:
        subprocess.Popen(["python", "register.py"])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'ouvrir le formulaire d'inscription : {e}")

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
            code_word.config(show="*")  # Masquer le mot de passe
        else:
            # Si utilisateur pas trouvé, on peut vider ou laisser vide
            code_word.delete(0, END)
            code_word.insert(0, "Mot de passe")
            code_word.config(show="")
    except FileNotFoundError:
        # fichier pas trouvé, vide le champ
        code_word.delete(0, END)
        code_word.insert(0, "Mot de passe")
        code_word.config(show="")
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lecture fichier : {e}")

def toggle_password():
    if show_password.get():
        # cacher mot de passe
        code_word.config(show="*")
        show_password.set(False)
        bouton_oeil.config(text="👁️")
    else:
        # afficher mot de passe en clair
        code_word.config(show="")
        show_password.set(True)
        bouton_oeil.config(text="👁️‍🗨️")



root = Tk()
root.title("Connexion")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

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

    if nom_utilisateur in utilisateurs:
        if utilisateurs[nom_utilisateur] == mot_de_passe:
            # Connexion réussie
            screen = Toplevel(root)
            screen.title("Application")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")

            Label(screen, text=f"Bienvenue {nom_utilisateur} !", bg="white",
                  font=("Microsoft YaHei UI Light", 32)).pack(pady=50)

            # BOUTON DECONNEXION
            Button(screen, text="Déconnexion", bg="#ff4d4d", fg="white",
                   font=("Microsoft YaHei UI Light", 12),
                   command=screen.destroy).pack(pady=20)
        else:
            messagebox.showerror("Erreur", "Mot de passe incorrect")
    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur incorrect")

img = PhotoImage(file="login.png")
Label(root, image=img, bg="#fff").place(x=50, y=50)

frame =  Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Connexion", bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)



#################-------------------------------------------------

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e): 
    name= user.get()
    if name == '':
        user.insert(0, "Nom d'utilisateur")
      
user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#################-------------------------------------------------
def on_enter(e):
    code_word.delete(0, 'end')
def on_leave(e): 
    name= code_word.get()
    if name == '':
        code_word.insert(0, "Mot de passe")
    
        
code_word = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code_word.place(x=30, y=150)
code_word.insert(0, "Mot de passe")
code_word.bind("<FocusIn>", afficher_mdp)
code_word.bind("<FocusOut>", on_leave)
code_word.config(show="")

show_password = BooleanVar(value=False)
bouton_oeil = Button(frame, text="👁️", bg="white", border=0, command=toggle_password)
bouton_oeil.place(x=300, y=150)


Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#################-------------------------------------------------
Button(frame, width=39, pady=7, text="Connexion", bg="#57a1f8", fg="white",command = connexion , border=0).place(x=35, y=205)
label = Label(frame, text="Mot de passe oublié ?", bg="white", fg="black", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

Inscription = Button(frame, width=6, text="S'inscrire", cursor="hand2", bg="white",
       fg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 9), command=ouvrir_inscription).place(x=215, y=270)

#################-------------------------------------------------

root.mainloop() 