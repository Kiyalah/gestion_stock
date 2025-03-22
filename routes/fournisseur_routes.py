from flask import Blueprint, jsonify, request
from models.fournisseur import Fournisseur

fournisseur_bp = Blueprint('fournisseur', __name__)

@fournisseur_bp.route('/fournisseurs', methods=['GET'])
def get_fournisseurs():
    fournisseurs = Fournisseur.get_all()
    return jsonify(fournisseurs)

@fournisseur_bp.route('/fournisseurs', methods=['POST'])
def add_fournisseur():
    data = request.get_json()
    nom = data.get('nom')
    contact = data.get('contact')
    
    if not nom or not contact:
        return jsonify({"error": "Nom et contact sont requis"}), 400
    
    Fournisseur.create(nom, contact)
    return jsonify({"message": "Fournisseur ajouté avec succès !"}), 201

@fournisseur_bp.route('/fournisseurs/<int:id>', methods=['DELETE'])
def delete_fournisseur(id):
    success = Fournisseur.delete_by_id(id)
    if success:
        return jsonify({"message": "Fournisseur supprimé avec succès !"}), 200
    else:
        return jsonify({"error": "Fournisseur non trouvé"}), 404