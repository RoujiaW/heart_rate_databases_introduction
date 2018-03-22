from flask import Flask, jsonify, request 
from pymodm import connect
import models
import datetime
from m1 import create_user, add_heart_rate
import numpy as np
app = Flask(__name__)
connect("mongodb://vcm-3551.vm.duke.edu:27017/heart_rate_app")

@app.route("/api/heart_rate/<user_email>",methods=["GET"])
def alldata(user_email):
	"""
	return all heart rate measurements for that user
	"""
	user = models.User.objects.raw({"_id": user_email}).first()
	measurements = {
		"measurements": user.heart_rate
	}
	return jsonify(measurements)


@app.route("/api/heart_rate/average/<user_email>",methods=["GET"])
def average_all(user_email):
	"""
	return average for all measurements
	"""
	user = models.User.objects.raw({"_id": user_email}).first()
	aver = sum(user.heart_rate)/len(user.heart_rate)
	average = {
		"average": aver
	}
	return jsonify(average)

@app.route("/api/heart_rate",methods=["POST"])
def store_user():
	"""
	post the new information about the heart rate measurement
	and time
	"""
	r = request.get_json()
	try:
		add_heart_rate(r["user_email"], r["heart_rate"],datetime.datetime.now())
	except NameError:
		create(email= r["user_email"], age= r["user_age"], heart_rate=r["heart_rate"])
	user = models.User.objects.raw({"_id": r["user_email"]}).first()
	message = {"information": "new information has been added",
	"heart_rate": user.heart_rate,
	"heart_rate": user.heart_rate_times,
	}		
	return jsonify(message)

@app.route("/api/heart_rate/interval_average",methods=["POST"])
def average_now():
	"""
	return return the average heart rate for the user since the time specified
	"""
	r = request.get_json()
	try:
		user = models.User.objects.raw({"_id": r["user_email"]}).first()
	except NameError:
		error1 = {"error": "This user does not exist"}
		return jsonify(error1)
		
	time_begin = r["heart_rate_average_since"]
	if time_begin not in user.heart_rate_times:
		case = {"error": "This time does not exist before",
		"average_interval": r["heart_rate"]
		}
	else:
		begin_location = user.heart_rate_times_list.index(time_begin)
		for i in range(begin_location-1, len(user.heart_rate_times),1):
			sum_interval += heart_rate[i]
			average = sum_interval/(len(user.heart_rate_times)-begin_location+1)
	case = {"average_interval": average} 
	return jsonify(case)
