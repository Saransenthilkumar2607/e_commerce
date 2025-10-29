from flask import Blueprint
from app.api.customer.controller import upload_customer_zip, get_users


customer_bp = Blueprint('customer_bp', __name__)
customer_bp.route('/upload_zip', methods=['POST'])(upload_customer_zip)
customer_bp.route('/get_zip', methods=['GET'])(get_users)