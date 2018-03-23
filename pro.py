from flask import Flask, jsonify, request 
from pymodm import connect
import models
import datetime
import time
from m1 import create_user, add_heart_rate
from ta import ta
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
	tah = ta(user.age, aver)
	if tah > 1:
		stm = "this person may have Tachycardia"
	else:
		stm = "this person's heart rate is normal"
	average = {
		"average": aver,
		"health condition": stm
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
	"heart_rate_times": user.heart_rate_times,
	}		
	return jsonify(message), 200

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
	first_time = time_begin
	for i in range(len(user.heart_rate_times)):
		user_time[i] = user.heart_rate_times[i].strftime("%Y-%m-%d %H:%M:%S.%f")
	sum_interval = 0
	if first_time > user_time[len(user.heart_rate_times)-1]:
		case = {"error": "There is no time after this",
		"all heart_rate": user.heart_rate,
		"heart_rate_times": user.heart_rate_times
		}
	else:
		for i in range(len(user.heart_rate_times)-1):
			if first_time < user_time[0]:
				sum_interval = sum(user.heart_rate)
				average_interval = sum_interval/len(user.heart_rate)
			elif first_time >= user_time[i] and first_time < user_time[i+1]:
				for n in range(i, len(user.heart_rate_times),1):
					sum_interval = user.heart_rate[n] + sum_interval
				average_interval = sum_interval/(len(user.heart_rate_times)-i+1)	
			elif first_time == user_time[len(user.heart_rate)-1]:
				average_interval = user.heart_rate[len(user.heart_rate)-1]
		tah1 = ta(user.age, average_interval)
		if tah1 > 1:
			stm = "this person may have Tachycardia"
		else:
			stm = "this person's heart rate is normal"
		case = {"average_interval": average_interval,
		"health condition": stm
		} 
	return jsonify(case), 200
