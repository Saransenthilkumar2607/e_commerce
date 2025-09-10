from flask import Flask
from app.extensions import db, migrate
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    # DB Config
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@localhost/e_commerce"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from app import models  

    return app

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)