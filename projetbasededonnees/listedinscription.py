from tkinter import *
from PIL import Image, ImageTk #python imaging library -open-source additional library , adds support for opening, manipulating, and saving many diff imagefile formats
import service as serv


def listeInscrit(window):
    newFen = Toplevel(window)
    newFen.geometry("350x600+350+150")
    newFen.title("Liste des personnes inscrites")

    listeCan = Canvas(newFen, bg="#FF7800")
    fontLabel = "arial 11 bold"

    resultat = Label(listeCan, text="Liste des personnes inscrits", font=fontLabel, fg="#FF7800", bg="white")
    prenom = Label(listeCan, text="prenom", width=15, font=fontLabel, fg="white", bg="#FF7800")
    nom = Label(listeCan, text="nom", width=6, font=fontLabel, fg="white", bg="#FF7800")
    photo = Label(listeCan, text="photo", width=12, font=fontLabel, fg="white", bg="#FF7800")
    status = Label(listeCan, text="Aucune inscription", font="arial 9 bold", fg="white", bg="#FF7800")

    listeCan.grid(row=0, column=0)
    resultat.grid(row=0, column=0, columnspan=3) #fusionner 3 columns
    photo.grid(row=1,column=0, padx=5, pady=5)
    prenom.grid(row=1,column=1, padx=5, pady=5)
    nom.grid(row=1,column=2, padx=5, pady=5)

    status.grid(row=2,column=0, columnspan=3)

    liste = serv.parcourir()


#récupérer des données et les afficher
    if liste: #parcourir la liste 
        r=2
        for p in liste:
            photoLab =  Label(listeCan, height=50)
            img = Image.open(p[3])
            img = img.resize((80,80), Image.ANTIALIAS) #ANTIALIAS - argument utilisé avec la méthode Image.resize() de la biblio PIL, l'antialiasing est une technique graphique utilisée pour réduire les irrégualités en adoucissant les bords des objets dans l'image( améliorer la qualité visuelle de l'image réduite)
            photoLab.img = ImageTk.PhotoImage(img)
            photoLab.configure(image=photoLab.img) #associer le label à l'image

            pre = Label(listeCan, text=p[1], font=fontLabel, fg="white", bg="#FF7800")
            no = Label(listeCan, text=p[2], font=fontLabel, fg="white", bg="#FF7800")

            photoLab.grid(row=r, column=0, pady=2)
            pre.grid(row=r, column=1)
            no.grid(row=r, column=2)
            listeCan.create_line(9,55,355,55, width=1, fill='white')

            r += 1 #aligner les photos

            status.configure(text="{} les personnes inscrites pour le moment".format(len(liste)))
            status.grid(row=r, column=0, columnspan=3, pady=2)
    
    newFen.mainloop()  #permet d'afficher la fênetre