from flask_mysqldb import MySQL
from config import Config

mysql = MySQL()

class Fournisseur:
    def __init__(self, id, nom, contact):
        self.id = id
        self.nom = nom
        self.contact = contact

    @staticmethod
    def get_all():
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Fournisseur")
        fournisseurs = cur.fetchall()
        cur.close()
        return fournisseurs

    @staticmethod
    def create(nom, contact):
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO Fournisseur (nom, contact) VALUES (%s, %s)",
            (nom, contact)
        )
        mysql.connection.commit()
        cur.close()

    @staticmethod
    def delete_by_id(id):
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Fournisseur WHERE id = %s", (id,))
        mysql.connection.commit()
        rows_affected = cur.rowcount
        cur.close()
        return rows_affected > 0