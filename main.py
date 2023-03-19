from tkinter import *
from tkinter import ttk
import tkinter as tk
from gestion import Gestion

#paramètre général de la fenetre
fenetre = tk.Tk()
fenetre.geometry('600x600')
fenetre.title('gestion de stock')
fenetre.configure(bg='#000000')

nom = StringVar()
description = StringVar()
prix = StringVar()
quantite = StringVar()
categorie = StringVar()

def supprimer_tous_affichage():
    produits = affichage_produit.get_children()
    for produit in produits:
        affichage_produit.delete(produit)

def afficher_produit():
    affichage = Gestion()
    supprimer_tous_affichage()
    for produit in affichage.getprendre_liste_produit():
        id = produit[0]
        affichage_produit.insert("", END, id, text=id, values=produit)

def supprimer_produit_liste():
    ID = affichage_produit.selection()[0]
    supprimer = Gestion()
    supprimer.getsupprimer_produit(ID)
    afficher_produit()

def ajouter_produit_liste():
    ajouter = Gestion()
    ajouter.get_ajouter_produit(entrer_nom_produit.get(), entrer_description_produit.get(),
                                entrer_prix_produit.get(), entrer_quantite_produit.get(),
                                entrer_id_categorie_produit.get())

    afficher_produit()

def remplir_case(event):
    id = affichage_produit.selection()[0]
    nom.set(affichage_produit.item(id, "values")[1])
    description.set(affichage_produit.item(id, "values")[2])
    prix.set(affichage_produit.item(id, "values")[3])
    quantite.set(affichage_produit.item(id, "values")[4])
    categorie.set(affichage_produit.item(id, "values")[5])

def modifier_produit_liste():
    id = affichage_produit.selection()[0]
    modifier = Gestion()
    modifier.getmodifier_liste_produit(id,entrer_nom_produit.get(), entrer_description_produit.get(),
                                entrer_prix_produit.get(), entrer_quantite_produit.get(),
                                entrer_id_categorie_produit.get())
    afficher_produit()

def exporter_liste():
    exporter = Gestion()
    exporter.get_exporter_produit()



#section nom produit
nom_produit = Label(fenetre, text='Nom', fg='WHITE', bg='BLACK')
nom_produit.grid(column=0, row=1)
entrer_nom_produit= Entry(fenetre , bg='WHITE', fg='BLACK', width=15, justify='right', textvariable=nom)
entrer_nom_produit.focus_set()
entrer_nom_produit.grid(column=1 , row=1)

#section description du produit
description_produit = Label(fenetre, text='description', fg='WHITE', bg='BLACK')
description_produit.grid(column=0, row=3)
entrer_description_produit = Entry(fenetre , bg='WHITE', fg='BLACK', width=15, justify='right', textvariable=description)
entrer_description_produit.focus_set()
entrer_description_produit.grid(column=1 , row=3)

#section prix du produit
prix_produit = Label(fenetre, text='Prix', fg='WHITE', bg='BLACK')
prix_produit.grid(column=2, row=1)
entrer_prix_produit = Entry(fenetre, bg='WHITE', fg='BLACK', width=15, justify='right', textvariable=prix)
entrer_prix_produit.focus_set()
entrer_prix_produit.grid(column=3, row=1)

#section quantitée du produit
quantite_produit = Label(fenetre, text='quantité', fg='WHITE', bg='BLACK')
quantite_produit.grid(column=2, row=2)
entrer_quantite_produit = Entry(fenetre, bg='WHITE', fg='BLACK', width=15, justify='right', textvariable=quantite)
entrer_quantite_produit.focus_set()
entrer_quantite_produit.grid(column=3, row=2)

#section id categorie du produit
categorie_produit = Label(fenetre, text='catégorie', fg='WHITE', bg='BLACK')
categorie_produit.grid(column=2, row=3)
entrer_id_categorie_produit = Entry(fenetre, bg='WHITE', fg='BLACK', width=15, justify='right', textvariable=categorie)
entrer_id_categorie_produit.focus_set()
entrer_id_categorie_produit.grid(column=3, row=3)

#section affichage des produit
section_affichage_produit = Frame()
section_affichage_produit.grid(row=4, columnspan=4)
colonnes = ('id', 'nom', 'description', 'prix', 'quantité', 'id_catégorie', 'catégorie')
affichage_produit = ttk.Treeview(section_affichage_produit, columns=colonnes)
affichage_produit.grid()

affichage_produit.column('#0', width=0,stretch=NO)
affichage_produit.heading('#0', text='')
affichage_produit.column('id', width=50, anchor=CENTER)
affichage_produit.heading('id', text='ID')
affichage_produit.column('nom', width=100)
affichage_produit.heading('nom', text='Nom')
affichage_produit.column('description', width=100)
affichage_produit.heading('description', text='Description')

affichage_produit.column('prix', width=50, anchor=CENTER)
affichage_produit.heading('prix', text='Prix')

affichage_produit.column('quantité', width=100, anchor=CENTER)
affichage_produit.heading('quantité', text='Quantité')
affichage_produit.column('id_catégorie', width=70, anchor=CENTER)
affichage_produit.heading('id_catégorie', text='id Catégorie')
affichage_produit.column('catégorie', width=100, anchor=CENTER)
affichage_produit.heading('catégorie', text='Catégorie')
affichage_produit.bind("<<TreeviewSelect>>", remplir_case)

    #section bouton
section_bouton = Frame(bg='BLACK')
section_bouton.grid(columnspan=4, row=5)
bouton_ajouter = Button(section_bouton, text='ajouter', command=lambda :ajouter_produit_liste())
bouton_ajouter.grid(row=0, column=1, padx=25)
bouton_supprimer = Button(section_bouton, text='Supprimer', command= lambda : supprimer_produit_liste())
bouton_supprimer.grid(column=2, row=0, padx=25 )
bouton_modifier = Button(section_bouton,text='Modifier', command=lambda : modifier_produit_liste())
bouton_modifier.grid(row=0, column=3, padx=25)
bouton_exporter = Button(section_bouton, text='Exporter', command=lambda :exporter_liste())
bouton_exporter.grid(row=0, column=4, padx=25)



#section graphique


afficher_produit()
fenetre.mainloop()