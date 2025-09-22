from flask import request, jsonify
from app.config.config import get_db_connection


# CREATE table in python code its easy to maintain the code for everyone
def create_user():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    values = (data['username'], data['email'], data['password'])
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User created successfully"}), 201


# READ to show the details
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)


# UPDATE the old details of users
def update_user(user_id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE users SET username=%s, email=%s WHERE id=%s"
    values = (data.get("username"), data.get("email"), user_id)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User updated successfully"})


# DELETE the user by there user id
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM users WHERE id=%s"
    cursor.execute(sql, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "User deleted successfully"})