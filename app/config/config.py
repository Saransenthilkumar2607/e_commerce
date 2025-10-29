import mysql.connector
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "mysql+pymysql://root:12345678@localhost/e_commerce"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="e_commerce"
    )

