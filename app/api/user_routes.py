# from flask import Flask
# from app import route
# from app.config import Config
# from app.extensions import db, migrate

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     migrate.init_app(app, db)

#     # Register endpoints
#     app.add_url_rule("/users", view_func=route.create_user, methods=["POST"])
#     app.add_url_rule("/users", view_func=route.get_users, methods=["GET"])
#     app.add_url_rule("/users/<int:user_id>", view_func=route.update_user, methods=["PUT"])
#     app.add_url_rule("/users/<int:user_id>", view_func=route.delete_user, methods=["DELETE"])

    # return app
