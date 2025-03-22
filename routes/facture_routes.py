from flask import Blueprint, jsonify
from models.facture import Facture

facture_bp = Blueprint('facture', __name__)

@facture_bp.route('/factures', methods=['GET'])
def get_factures():
    factures = Facture.get_all()
    return jsonify(factures)