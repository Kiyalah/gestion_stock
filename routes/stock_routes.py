from flask import Blueprint, jsonify
from models.stock import Stock

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/stocks', methods=['GET'])
def get_stocks():
    stocks = Stock.get_all()
    return jsonify(stocks)