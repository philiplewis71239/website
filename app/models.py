import sqlite3 as sql
from app import app
from app import db
from datetime import datetime

class Logs(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	ip_addr = db.Column(db.String)
	timestamp = db.Column(db.DateTime, default=datetime.now())


# def insert_log(ip_addr):
#     with sql.connect("database.db") as con:
#         cur = con.cursor()
#         timestamp = str(datetime.now())
#         cur.execute("INSERT into logs (ip_address,timestamp) VALUES (?,?)", (ip_addr, timestamp))
#         con.commit()

# def get_logs():
#     with sql.connect("database.db") as con:
#         cur = con.cursor()
#         result = cur.execute("select * from logs").fetchall()
#     return result

