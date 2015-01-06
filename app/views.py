from flask import render_template, request, jsonify
from models import *
from app import app


@app.route("/", methods=["POST","GET"])
def gateway():
    #db.create_all()
    ip = request.remote_addr
    insert_log(ip)
    return render_template("gateway.html")

@app.route("/index",methods=["POST","GET"])
def index2():
	ip = request.remote_addr
	insert_log(ip)
	return render_template("index.html")