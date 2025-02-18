from flask import Flask
import mysql.connector
from pymongo import MongoClient
import time

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

def compute_stats():
    while True:
        # Read data from MySQL and compute stats
        cursor = mysql_db.cursor()
        cursor.execute("SELECT MAX(value), MIN(value), AVG(value) FROM data")
        result = cursor.fetchone()

        stats = {
            "max": result[0],
            "min": result[1],
            "avg": result[2]
        }

        # Write stats to MongoDB
        collection.insert_one(stats)
        print("Stats computed and written to MongoDB:", stats)
        time.sleep(60)  # Compute stats every 60 seconds

if __name__ == '__main__':
    compute_stats()