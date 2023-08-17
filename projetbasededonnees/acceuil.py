from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
from listedinscription import listeInscrit
import service as serv
from PIL import Image


class Personnage():
    def __init__(self, prenom, nom, photo):
        self.prenom = prenom
        self.nom = nom
        self.photo = photo

    def __eq__(self, other): #equal - permet de comparer des éléments personnelles - comparer un élément avec un autre
        return(self.prenom == other.prenom and self.nom == other.nom)  #des personnes dans le liste ne puissent pas avoir les mêmes prénoms et les mêmes noms

def parcourir():
    global imageName  #déclarer une variable nomée imageName
    imn = askopenfilename(initialdir="/", title="selectionner une image", filetypes=(("png files", "*.png"), ("jpeg files", "*.jpg")))
#imn - variable qui est local à la fonction et j'utilise la libratie que j'ai importé pour choisir une image :::: initialdir="/" - dossier initial qui nous amène a la dossier principal de l'utilisateur 

    if imn:  # si imn existe
        imageName = imn
    if imageName: 
        texte = imageName.split("/") #prendre l'adresse de l'image et le mettre dans un tableau -> récupérer les derniers éléments    
        photoEntre.configure(text=".../"+texte[-1])

"""def appartient(liste, val): #tester si un élément a déjà été ajouté
    for i in range(len(liste)): #parcourir la liste
        if liste[i].__eq__(val): 
            return 1  #true
    return 0 #false"""

def valider(): # valider les champs
    global imageName #variables
    if prenomEntre.get() and nomEntre.get() and imageName:  #get() - permet de récupérer ce qui se trouve dans les champs
        photo = 'images/'+imageName.split('/')[-1]  #dernière partie des fichiers
        pn = Personnage(prenomEntre.get(), nomEntre.get(), photo)
        img = Image.open(imageName)
        img.save(photo)
        serv.ajouter(pn)
        showinfo(title="Validation réussie",message="{} a bien été ajouté".format(prenomEntre.get()))
    else:
        showerror(title="Formulaire invalide",message="Complétez les champs!")


def reinitialiser():  #effacer tout ce qui se trouve dans les champs
    global imageName
    prenomEntre.delete(0,END) #0 du début END jusqu'à la fin
    nomEntre.delete(0,END)
    imageName='' #vide
    photoEntre.configure(text="aucune image séléctionée") 

imageName, listePersonne = '', []

#créer les différents éléments de la fenêtre
fen = Tk()
fen.geometry("320x320+320+150")  #géométrie de la fenêtre
fen.title("Page d'inscription")

contenu = Canvas(fen, bg="#FF7800")

fontLabel = 'arial 13 bold'
fontEntre = 'arial 11 bold'

prenom = Label(contenu, text="votre prénom :", font = fontLabel, fg='white', bg="#FF7800")
nom = Label(contenu, text="votre nom :", font = fontLabel, fg='white', bg="#FF7800")
photo = Label(contenu, text="votre photo :", font = fontLabel, fg='white', bg="#FF7800")
validation = Label(contenu, text="Entrer vos information ici", font = fontLabel, fg="#FF7800", bg='white')

prenomEntre = Entry(contenu, font=fontEntre)
nomEntre = Entry(contenu, font=fontEntre)
photoEntre = Label(contenu, text="aucune image séléctionnée", font = 'arial 8 bold', fg="white", bg='#FF7800')
buttonParcourir = Button(contenu, text="Pr", command=parcourir, fg="white", bg='#FF7800')  

validation.grid(row=0, column=0, columnspan=2)
prenom.grid(row=1, column=0, sticky=E, padx=5, pady=5) #sticky=E - orientation a l'est , aligné à droite 
nom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
photo.grid(row=3, column=0, sticky=E, padx=5, pady=5)

prenomEntre.grid(row=1, column=1, padx=5, pady=5) #sticky=E - orientation a l'est , aligné à droite 
nomEntre.grid(row=2, column=1, padx=5, pady=5)
photoEntre.grid(row=3, column=1, padx=5, pady=5, sticky=W)
buttonParcourir.grid(row=3, column=1, padx=5, pady=5, sticky=E)

b1 = Button(fen, text="Valider", command=valider, width=10, fg="white", bg="#FF7800") 
b2 = Button(fen, text="Réinitialiser", command=reinitialiser, width=10, fg="white", bg="#FF7800") 
b3 = Button(fen, text="Voir la liste", command= lambda: listeInscrit(fen), width=10, fg="white", bg="#FF7800")

b1.grid(row=4, column=0, pady=5)
b2.grid(row=5, column=0, pady=5)
b3.grid(row=6, column=0, pady=5)

contenu.grid(row=0, column=0, padx=5, pady=5)

fen.mainloop()

