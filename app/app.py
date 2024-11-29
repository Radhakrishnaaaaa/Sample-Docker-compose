from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    "host": "db",  # This must match the `service name` of the database in docker-compose.yml
    "user": "flaskuser",
    "password": "flaskpass",
    "database": "flaskdb"
}

@app.route("/")
def index():
    return jsonify(message="Hello, World!")

@app.route("/db")
def db_check():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        return jsonify(tables=tables or "No tables found.")
    except mysql.connector.Error as e:
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
