import tkinter as tk
from tkinter import messagebox
import string
import random

# Fonction pour générer le mot de passe
def generator():
    longueur = int(Entre_longueur.get())

    caracteres = ""
    if var_majuscule.get():
        caracteres += string.ascii_uppercase
    if var_minuscule.get():
        caracteres += string.ascii_lowercase
    if var_chiffre.get():
        caracteres += string.digits
    if var_special.get():
        caracteres += string.punctuation
    if not caracteres:
        messagebox.showerror("Erreur", "Veuillez sélectionner au moins un type de caractère.")
        return

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    entre_resultat.delete(0, tk.END)
    entre_resultat.insert(0, mot_de_passe)
# Fonction pour copier le mot de passe dans le presse-papiers
def copier():
    mot_de_passe = entre_resultat.get()
    if mot_de_passe:
        root.clipboard_clear()
        root.clipboard_append(mot_de_passe)
        messagebox.showinfo("Copié", "Le mot de passe a été copié dans le presse-papiers.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Générateur de mot de passe")
root.geometry("400x350") 
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Titre de la fenêtre
tk.Label(root, text="Longueur du mot de passe :", bg="#f0f0f0").pack(pady=5)
Entre_longueur = tk.Entry(root, width=5)
Entre_longueur.pack(pady=5)
Entre_longueur.insert(0, "12")  # Valeur par défaut

# variable pour les cases à cocher
var_majuscule = tk.BooleanVar(value=True)
var_minuscule = tk.BooleanVar(value=True)
var_chiffre = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

# Cases à cocher pour sélectionner les types de caractères
tk.Checkbutton(root, text="Majuscules", 
variable = var_majuscule).pack(anchor=tk.W, padx=30)
tk.Checkbutton(root, text="Minuscules",
variable = var_minuscule).pack(anchor=tk.W, padx=30)
tk.Checkbutton(root, text="Chiffres",
variable = var_chiffre).pack(anchor=tk.W, padx=30)
tk.Checkbutton(root, text="Caractères spéciaux",    
variable = var_special).pack(anchor=tk.W, padx=30)


# Champ pour afficher le mot de passe généré
entre_resultat = tk.Entry(root, width=30, font=("Arial", 12))
entre_resultat.pack(pady=10)

# Boutons pour générer et copier le mot de passe
tk.Button(root, text="Générer", command=generator).pack(pady=5)
tk.Button(root, text="Copier", command=lambda: copier()).pack(pady=5)

# Afficher la fenêtre principale
root.mainloop()
          
