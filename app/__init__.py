# from flask import Flask
# from app.api.user.route import user_blueprint

# def create_app():
    
#     app = Flask(__name__)

#     # Correct path to your Config class
#     app.config.from_object("app.config.config.Config")

#     # Register the user blueprint
#     app.register_blueprint(user_blueprint, url_prefix="/api")

#     return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.user.route import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/api")

    return app
