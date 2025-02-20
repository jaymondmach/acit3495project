from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="mysql-db",
    user="root",
    password="root",
    database="mydb"
)

@app.route('/enter-data', methods=['POST'])
def enter_data():
    data = request.json
    user_token = request.headers.get('Authorization')
    
    
    # Validate token (mock validation)
    if user_token != 'fake-token':
        return jsonify({"message": "Unauthorized"}), 401

    # Insert data into MySQL
    cursor = db.cursor()
    sql = "INSERT INTO data (value) VALUES (%s)"
    cursor.execute(sql, (data['value'],))
    db.commit()

    return jsonify({"message": "Data entered successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)