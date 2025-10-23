# # import os
# # import mysql.connector

# # class Config:
# #     MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
# #     MYSQL_USER = os.getenv("MYSQL_USER", "root")
# #     MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "12345678")
# #     MYSQL_DB = os.getenv("MYSQL_DB", "e_commerce")

# # def get_db_connection():
# #     return mysql.connector.connect(
# #         host=Config.MYSQL_HOST,
# #         user=Config.MYSQL_USER,
# #         password=Config.MYSQL_PASSWORD,
# #         database=Config.MYSQL_DB
# #     )







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
