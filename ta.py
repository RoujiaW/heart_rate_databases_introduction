def ta(age, heart_rate):
	if age >=1 and age < 3 and heart_rate > 151:
		ta = 1
	elif age >=3 and age < 5 and heart_rate > 137:
		ta = 1
	elif age >= 5 and age < 8 and heart_rate > 133:
		ta = 1
	elif age >= 8 and age < 12 and heart_rate > 130:
		ta = 1
	elif age >= 12 and age < 15 and heart_rate > 119:
		ta = 1
	elif age >= 15 and heart_rate > 100:
		ta = 1
	else:
		ta = 0
	return ta
	
