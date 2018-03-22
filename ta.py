def ta(age, heart_rate):
	if age >=1 & age < 3 & heart_rate > 151:
		ta = 1
	elif age >=3 & age < 5 & heart_rate > 137:
		ta = 1
	elif age >= 5 & age < 8 & heart_rate > 133:
		ta = 1
	elif age >= 8 & age < 12 & heart_rate > 130:
		ta = 1
	elif age >= 12 & age < 15 & heart_rate > 119:
		ta = 1
	elif age >= 15 & heart_rate > 100:
		ta = 1
	else:
		ta = 0
	return ta
	
