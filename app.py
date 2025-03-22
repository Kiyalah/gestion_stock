from flask import Flask, render_template
from flask_mysqldb import MySQL
from config import Config
from routes.user_routes import user_bp
from routes.client_routes import client_bp
from routes.fournisseur_routes import fournisseur_bp
from routes.produit_routes import produit_bp
from routes.stock_routes import stock_bp
from routes.vente_routes import vente_bp
from routes.facture_routes import facture_bp

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

app.register_blueprint(user_bp)
app.register_blueprint(client_bp)
app.register_blueprint(fournisseur_bp)
app.register_blueprint(produit_bp)
app.register_blueprint(stock_bp)
app.register_blueprint(vente_bp)
app.register_blueprint(facture_bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

