# import os
# import mysql.connector
# from flask import Flask

# app = Flask(__name__)

# app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST", "localhost")
# app.config['MYSQL_USER'] = os.getenv("MYSQL_USER", "root")
# app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD", "12345678")
# app.config['MYSQL_DB'] = os.getenv("MYSQL_DB", "e_commerce")

# def get_db_connection():
#     conn = mysql.connector.connect(
#         host=app.config['MYSQL_HOST'],
#         user=app.config['MYSQL_USER'],
#         password=app.config['MYSQL_PASSWORD'],
#         database=app.config['MYSQL_DB']
#     )
#     return conn

import os
class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "12345678")
    MYSQL_DB = os.getenv("MYSQL_DB", "e_commerce")