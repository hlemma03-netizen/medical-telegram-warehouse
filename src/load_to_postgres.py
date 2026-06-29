import os
import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="medical_warehouse",
    user="postgres",
    password="YOUR_PASSWORD"
)

cursor = conn.cursor()

DATA_FOLDER = "data/raw/telegram_messages"
for root, dirs, files in os.walk(DATA_FOLDER):
    for file in files:
        if file.endswith(".json"):

            path = os.path.join(root, file)

            with open(path, "r") as f:
                messages = json.load(f)  

channel_name = file.replace(".json", "")