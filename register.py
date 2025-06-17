from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Inscription")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)


def Inscription():
    nom_utilisateur = user.get()
    mot_de_passe = code.get()
    conform_mot_de_passe = conform_code.get()

    if mot_de_passe == conform_mot_de_passe:
        try:
            file = open("datasheet.txt", "r+")
            d = file.readlines()
            r=ast.literal_eval(d)

            dict2 = {nom_utilisateur:mot_de_passe}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file= open("datasheet.txt", "w")
            w=file.write(str(r))
           
            messagebox.showinfo("Inscription", "Inscription réussie")

        except:

            file = open("datasheet.txt", "w")
            pp=str({"username":"password"})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror("Invalide", "Les mots de passe ne correspondent pas")

            
            
img = PhotoImage(file="login.png")
Label(root, image=img, bg="#fff").place(x=50, y=50)

frame =  Frame(root, width=350, height=390, bg="white")
frame.place(x=480, y=50)

heading = Label(frame, text="Inscription", bg="white", fg="#57a1f8", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)


#################-------------------------------------------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e): 
    if user.get() == '':
        user.insert(0, "Nom d'utilisateur")

user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#################-------------------------------------------------
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e): 
    if code.get() == '':
        code.insert(0, "Mode de passe")
    
        
code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
code.place(x=30, y=150)
code.insert(0, "Mode de passe")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)


#################-------------------------------------------------
def on_enter(e):
    conform_code.delete(0, 'end')
def on_leave(e): 
    if conform_code.get() =='':
        conform_code.insert(0, "Confirmer le mode de passe")
    
        
conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("Microsoft YaHei UI Light", 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, "Mode de passe")
conform_code.bind("<FocusIn>", on_enter)
conform_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

#--------------------------------

Button(frame, width=39, pady=7, text="S'inscrire", bg="#57a1f8", fg="white", border=0, command=Inscription).place(x=35, y=290)
Label = Label(frame, text="Vous avez déjà un compte ?", bg="white", fg="black", font=("Microsoft YaHei UI Light", 9))
Label.place(x=90, y=340)

Inscription = Button(frame, width=6, text="Connexion",cursor="hand2", bg="white", fg="#57a1f8", border=0)
Inscription.place(x=260, y=340)


root.mainloop() 