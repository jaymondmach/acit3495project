from flask import Flask, request, jsonify
import mysql.connector
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MySQL configuration
mysql_db = mysql.connector.connect(
    host="mysql-db",
    user="root",
    password="root",
    database="mydb"
)

# MongoDB configuration
mongo_client = MongoClient("mongodb://mongo-db:27017/")
mongo_db = mongo_client["analytics"]
collection = mongo_db["stats"]

@app.route('/compute-stats')
def compute_stats():
    cursor = mysql_db.cursor()
    cursor.execute("SELECT MAX(value), MIN(value), AVG(value) FROM data")
    result = cursor.fetchone()
    cursor.close()  # Close MySQL cursor to avoid connection issues

    stats = {
        "max": result[0],
        "min": result[1],
        "avg": result[2]
    }

    # Insert stats into MongoDB and get the inserted document
    inserted_doc = collection.insert_one(stats)
    
    stats["_id"] = str(inserted_doc.inserted_id)
    
    print("Stats computed and written to MongoDB:", stats, flush=True)


    return jsonify({"message": "Stats computed and written to MongoDB", "stats": stats}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
