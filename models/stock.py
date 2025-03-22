from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class Stock:
    def __init__(self, id, produit_id, quantité, date_maj):
        self.id = id
        self.produit_id = produit_id
        self.quantité = quantité
        self.date_maj = date_maj

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Stock")
        stocks = cur.fetchall()
        cur.close()
        return stocks