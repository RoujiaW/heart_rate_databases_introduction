from flask import Flask, jsonify, request
import requests
from pymodm import connect
import models
import datetime
import m1

r = requests.post("http://vcm-3551.vm.duke.edu:5000/api/heart_rate",json={"user_email": "suyash@suyashkumar.com",
    "user_age": 50, 
    "heart_rate": 100})
print(r) 
