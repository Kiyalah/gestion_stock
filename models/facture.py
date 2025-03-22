from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class Facture:
    def __init__(self, id, vente_id, montant, statut):
        self.id = id
        self.vente_id = vente_id
        self.montant = montant
        self.statut = statut

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Facture")
        factures = cur.fetchall()
        cur.close()
        return factures