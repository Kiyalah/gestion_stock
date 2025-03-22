from flask import Blueprint, jsonify, request
from models.produit import Produit

produit_bp = Blueprint('produit', __name__)

@produit_bp.route('/produits', methods=['GET'])
def get_produits():
    produits = Produit.get_all()
    return jsonify(produits)

@produit_bp.route('/produits/<int:id>', methods=['DELETE'])
def delete_produit(id):
    success = Produit.delete_by_id(id)
    if success:
        return jsonify({"message": "Produit supprimé avec succès !"}), 200
    else:
        return jsonify({"error": "Produit non trouvé"}), 404