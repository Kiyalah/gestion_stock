from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class Vente:
    def __init__(self, id, client_id, date, montant_total):
        self.id = id
        self.client_id = client_id
        self.date = date
        self.montant_total = montant_total

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Vente")
        ventes = cur.fetchall()
        cur.close()
        return ventes