from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class Produit:
    def __init__(self, id, nom, prix, stock_id):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.stock_id = stock_id

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Produit")
        produits = cur.fetchall()
        cur.close()
        return produits

    @staticmethod
    def delete_by_id(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Produit WHERE id = %s", (id,))
        mysql.connection.commit()
        rows_affected = cur.rowcount 
        cur.close()
        return rows_affected > 0 