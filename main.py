from tkinter import *
from tkinter import messagebox
import subprocess

def ouvrir_inscription():
    try:
        subprocess.Popen(["python", "register.py"])
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'ouvrir le formulaire d'inscription : {e}")

root = Tk()
root.title("Connexion")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

def connexion():
    userrname = user.get()
    password = code_word.get()

    if userrname == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("Application")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen, text="Bienvenue à vous ", bg="white", font=("Microsoft YaHei UI Light", 50)).pack(expand=True)

        screen.mainloop()
    elif userrname != "admin" or password != "1234":
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    elif password != "1234":
        messagebox.showerror("Erreur", "Mot de passe incorrect")  

    elif userrname != "admin":
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
code_word.bind("<FocusIn>", on_enter)
code_word.bind("<FocusOut>", on_leave)



######hIDE AND SHOW PASSWORD
button_mode=True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye, activebackground="black")
        code_word.config(show="*")
        button_mode=False
    else:
        eyeButton.config(image=openeye, activebackground="black")
        code_word.config(show="*")
        button_mode=True


openeye=PhotoImage(file="view.png")
closeeye=PhotoImage(file="hide.png")
eyeButton = Button(frame, image=openeye, border=0, bg="white", command=hide)
eyeButton.place(x=780, y=410)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

#################-------------------------------------------------
Button(frame, width=39, pady=7, text="Connexion", bg="#57a1f8", fg="white",command = connexion , border=0).place(x=35, y=205)
label = Label(frame, text="Mot de passe oublié ?", bg="white", fg="black", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

Inscription = Button(frame, width=6, text="S'inscrire", cursor="hand2", bg="white",
       fg="#57a1f8", border=0, font=("Microsoft YaHei UI Light", 9), command=ouvrir_inscription).place(x=215, y=270)

#################-------------------------------------------------

root.mainloop() 