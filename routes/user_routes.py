from flask import Blueprint, jsonify
from models.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.get_all()
    return jsonify(users)