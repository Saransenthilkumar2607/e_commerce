from flask import Flask
from app.api.user.route import user_blueprint

def create_app():
    
    app = Flask(__name__)

    # Correct path to your Config class
    app.config.from_object("app.config.config.Config")

    # Register the user blueprint
    app.register_blueprint(user_blueprint, url_prefix="/api")

    return app