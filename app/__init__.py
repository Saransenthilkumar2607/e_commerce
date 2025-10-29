from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.config.Config")  # Your DB/config settings

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app.models import user, customer

    # Register blueprints
    from app.api.user.route import user_blueprint
    from app.api.customer.route import customer_bp
    app.register_blueprint(user_blueprint, url_prefix="/api/users")
    app.register_blueprint(customer_bp, url_prefix="/api/customers")

    # Ensure tables exist
    with app.app_context():
        db.create_all()

    return app
