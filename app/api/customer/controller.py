import os
import zipfile
import csv
import mysql.connector
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

BASE_DIR = os.getcwd()
UPLOAD_TEMP = os.path.join(BASE_DIR, "uploads", "temp")
UPLOAD_IMAGES = os.path.join(BASE_DIR, "uploads", "images")

os.makedirs(UPLOAD_TEMP, exist_ok=True)
os.makedirs(UPLOAD_IMAGES, exist_ok=True)

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="e_commerce"
    )

def create_customer_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id VARCHAR(255),
            name VARCHAR(255),
            email VARCHAR(255),
            image_path VARCHAR(500)
        )
    ''')
    conn.commit()
    conn.close()

def insert_customer(customer_id, name, email, image_path):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO customers (customer_id, name, email, image_path)
        VALUES (%s, %s, %s, %s)
    ''', (customer_id, name, email, image_path))
    conn.commit()
    conn.close()

# @app.route('/upload', methods=['POST'])
def upload_customer_zip():
    try:
        
        if 'file' not in request.files:
            return jsonify({"status": "error", "message": "No file uploaded"}), 400

        file = request.files['file']
        filename = secure_filename(file.filename)
        zip_path = os.path.join(UPLOAD_TEMP, filename)
        file.save(zip_path)

        if not os.path.exists(zip_path):
            return jsonify({"status": "error", "message": "Failed to save uploaded file"}), 500

        if not zipfile.is_zipfile(zip_path):
            os.remove(zip_path)
            return jsonify({"status": "error", "message": "Uploaded file is not a ZIP"}), 400

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(UPLOAD_TEMP)
        os.remove(zip_path)


        csv_file = None
        images_folder = None
        for root, dirs, files in os.walk(UPLOAD_TEMP):
            for d in dirs:
                if d.lower() == "images":
                    images_folder = os.path.join(root, d)
            for f in files:
                if f.lower().endswith(".csv"):
                    csv_file = os.path.join(root, f)

        if not csv_file:
            return jsonify({"status": "error", "message": "No CSV file found in ZIP"}), 400
        if not images_folder:
            return jsonify({"status": "error", "message": "No images folder found in ZIP"}), 400

        image_map = {}
        for root, dirs, files in os.walk(images_folder):
            for f in files:
                name, ext = os.path.splitext(f)
                image_map[name.lower()] = os.path.join(root, f)

        updated_rows = []
        image_paths = []
        passed = 0
        skipped = 0
        missing_rows = []

        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader)

            if len(headers) < 4:
                headers += ["image_url"] * (4 - len(headers))
            else:
                headers[3] = "image_url"
            updated_rows.append(headers)

            for row_num, row in enumerate(reader, start=2):
                while len(row) < 4:
                    row.append("")

                customer_id = row[1].strip()
                image_path = image_map.get(customer_id.lower())

                if image_path and os.path.exists(image_path):
                    dest_path = os.path.join(UPLOAD_IMAGES, os.path.basename(image_path))
                    os.rename(image_path, dest_path)
                    row[3] = dest_path
                    image_paths.append(dest_path)
                    passed += 1
                else:
                    row[3] = ""
                    skipped += 1
                    missing_rows.append({"row_num": row_num, "data": row})

                updated_rows.append(row)

                insert_customer(
                    customer_id=customer_id,
                    name=row[0].strip(),
                    email=row[2].strip(),
                    image_path=row[3]
                )

        updated_csv_path = os.path.join(UPLOAD_TEMP, "updated_" + os.path.basename(csv_file))
        with open(updated_csv_path, 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerows(updated_rows)

        return jsonify({
            "status": "success",
            "passed_rows": passed,
            "skipped_rows": skipped,
            "missing_row_numbers": missing_rows,
            "updated_csv": updated_csv_path,
            "image_paths": image_paths
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# @app.route('/customers', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, customer_id, name, email, image_path FROM customers")
    rows = cursor.fetchall()
    conn.close()

    users = [
        {
            "id": row[0],
            "customer_id": row[1],
            "name": row[2],
            "email": row[3],
            "image_path": row[4]
        }
        for row in rows
    ]
    return jsonify(users)

if __name__ == '__main__':
    create_customer_table()
    app.run(debug=True)
