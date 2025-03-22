from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class User:
    def __init__(self, id, nom, email, role):
        self.id = id
        self.nom = nom
        self.email = email
        self.role = role

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Utilisateur")
        users = cur.fetchall()
        cur.close()
        return users