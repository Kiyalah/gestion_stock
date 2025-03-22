from flask import Blueprint, jsonify
from models.client import Client

client_bp = Blueprint('client', __name__)

@client_bp.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.get_all()
    return jsonify(clients)