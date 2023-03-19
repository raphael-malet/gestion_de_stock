import mysql.connector
import csv

class Gestion:
    def __init__(self):
        self.__admin = mysql.connector.connect(host='localhost', user='root', password='vatefaireencule', database='boutique')
        self.cursor = self.__admin.cursor()

#methode supprimer poduit de la liste
    def __supprimer_produit(self, id):
        commande_supprimer = 'delete from produit where id='+id
        self.cursor.execute(commande_supprimer)
        self.__admin.commit()

    def getsupprimer_produit(self,id):
        self.__supprimer_produit(id)

#methode prendre tous les produits de la database pour les afficher
    def __prendre_liste_produit(self):
        self.cursor.execute('select p.*, c.nom from produit p inner join categorie c on p.id_categorie = c.id;')
        produits = self.cursor.fetchall()
        return produits

    def getprendre_liste_produit(self):
        return self.__prendre_liste_produit()

#methode pour ajouter un prosuit a la database
    def __ajouter_produit(self,nom, description, prix, quantite, categorie):
        valeur = (nom, description, prix, quantite, categorie)
        commande = 'insert into produit (nom, description,prix,quantite,id_categorie) values (%s,%s,%s,%s,%s)'
        self.cursor.execute(commande, valeur)
        self.__admin.commit()

    def get_ajouter_produit(self, nom, description, prix,quantite, categorie):
        self.__ajouter_produit(nom, description, prix,quantite, categorie)

#methode pour modifier un produit de la database
    def __modifier_liste_produit(self, id,nom, description, prix, quantite,categorie):
        valeur = (nom, description, prix, quantite, categorie)
        commande = 'update produit set nom=%s, description=%s, prix=%s, quantite=%s, id_categorie=%s where id ='+id
        self.cursor.execute(commande, valeur)
        self.__admin.commit()

    def getmodifier_liste_produit(self,id, nom, description, prix, quantite, categorie):
        self.__modifier_liste_produit(id,nom, description, prix,quantite,categorie)

#methode exporter produit vers fichier csv
    def __exporter_produit(self):
        self.cursor.execute('select p.*, c.nom from produit p inner join categorie c on p.id_categorie = c.id;')
        produit = self.cursor.fetchall()
        with open('stock_produit.csv', 'w') as f:
            for i in produit:
                ecrire = csv.writer(f)
                ecrire.writerow(i)

    def get_exporter_produit(self):
        self.__exporter_produit()