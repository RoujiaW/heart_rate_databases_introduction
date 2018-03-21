from flask import Flask, jsonify, request 
from pymodm import connect
import models
import datetime
from m1 import create_user, add_heart_rate
app = Flask(__name__)
connect("mongodb://vcm-3551.vm.duke.edu:27017/heart_rate_app")
@app.route("/api/heart_rate", methods=["POST"])
def store():
	r = request.get_json()
#	connect("mongodb://vcm-3551.vm.duke.edu:27017/heart_rate_app")
	create_user(email=r["user_email"], age=r["user_age"], heart_rate=r["heart_rate"])
	add_heart_rate(r["user_email"], r["user_age"], datetime.datetime.now())
#	print_user(r["user_email"])
	info = r["user_email"]
	return info, 200
