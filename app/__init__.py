# from flask_mysql.connector import mysql.connector
# from flask_migrate import Migrate
# from app.config import Config   
# from app.models import User
from flask import Flask
# from app.route import register_route

def create_app():
   
    app = Flask(__name__)
    app.config.from_object("app.config.Config")   
    
    return app