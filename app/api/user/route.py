from flask import Blueprint
from app.api.user.controller import create_user, create_user_bulk, get_users, update_user, delete_user
    
user_blueprint = Blueprint('user', __name__)

user_blueprint.add_url_rule("/users", view_func=create_user, methods=["POST"])
user_blueprint.add_url_rule("/users_bulk", view_func=create_user_bulk, methods=["POST"])
user_blueprint.add_url_rule("/users", view_func=get_users, methods=["GET"])
user_blueprint.add_url_rule("/users/<int:user_id>", view_func=update_user, methods=["PUT"])
user_blueprint.add_url_rule("/users/<int:user_id>", view_func=delete_user, methods=["DELETE"])


