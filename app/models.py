import sqlite3 as sql
from app import app
from datetime import datetime
# class Logs(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     ip_address = db.Column(db.String(40))
#     timestamp = db.Column(db.String(120))

def insert_log(ip_addr):
    with sql.connect("database.db") as con:
        cur = con.cursor()
        timestamp = str(datetime.now())
        cur.execute("INSERT into logs (ip_address,timestamp) VALUES (?,?)", (ip_addr, timestamp))
        con.commit()

def get_logs():
    with sql.connect("database.db") as con:
        cur = con.cursor()
        result = cur.execute("select * from logs").fetchall()
    return result

