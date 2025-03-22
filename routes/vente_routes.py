from flask import Blueprint, jsonify
from models.vente import Vente

vente_bp = Blueprint('vente', __name__)

@vente_bp.route('/ventes', methods=['GET'])
def get_ventes():
    ventes = Vente.get_all()
    return jsonify(ventes)