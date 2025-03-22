from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class Client:
    def __init__(self, id, nom, contact):
        self.id = id
        self.nom = nom
        self.contact = contact

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Client")
        clients = cur.fetchall()
        cur.close()
        return clients