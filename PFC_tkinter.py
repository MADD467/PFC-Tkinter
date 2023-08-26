from tkinter import *
from tkinter import messagebox
import random
import time


# DEFINIR FONCTION POUR LE ROBOT 
# DEFINIR FONCTION POUR LE PLAYER

#choix = ("Rock", "Paper", "Scissors")
#computer = random.choice(choix)
# ESSAYER AVEC INPUT SUR L'INTERFACE GRAPHIQUE
# INPUT POUR TKINTER
'''value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()'''

fenetre = Tk()


choix = ("Rock", "Paper", "Scissors")
computer = random.choice(choix)

    # Création de la fenetre 

label = Label(fenetre, text="Pick One")
label.pack()

choix = ("Rock", "Paper", "Scissors")


def check1():
    computer = random.choice(choix)
    

    if rock_btn and computer == "Rock":
        messagebox.showinfo("EGALITE")
        print("robot a choist", computer)
    elif rock_btn and computer == "Paper":
        messagebox.showinfo("PERDU")
        print("robot a choist", computer)
    elif rock_btn and computer == "Scissors":
        messagebox.showinfo("GAGNE")
        print("robot a choist", computer)
        
                    
def check2():
    computer = random.choice(choix)

    if paper_btn and computer == "Rock":
        messagebox.showinfo("GAGNE")
        print("robot a choist", computer)
        #label = Label(fenetre, command=check, text='EGALITE')
    elif paper_btn and computer == "Paper":
        messagebox.showinfo("EGALITE")
        print("robot a choist", computer)
    elif paper_btn and computer == "Scissors":
        messagebox.showinfo("PERDU")
        print("robot a choist", computer)

                
def check3():
    computer = random.choice(choix)
     
    if scissors_btn and computer == "Rock":
        messagebox.showinfo("PERDU")
        print("robot a choist", computer)
    elif scissors_btn and computer == "Paper":
        messagebox.showinfo("GAGNE")
        print("robot a choist", computer)
    elif scissors_btn and computer == "Scissors":
        messagebox.showinfo("EGALITE")
        print("robot a choist", computer)



rock_btn = Button(fenetre, text="Rock", command=check1) #command=check
rock_btn.pack()
                
paper_btn = Button(fenetre, text="Paper", command=check2) #command=check  
paper_btn.pack()
                    
scissors_btn = Button(fenetre, text="Scissors", command=check3) #command=check
scissors_btn.pack()    
    











            



#for i in range(3):
    # Afficher le choix du robot pierre feuille ou ciseaux




    # Création de bouton
    
fenetre.mainloop()