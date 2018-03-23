def test_ta():
	"""
	test ta function which return whether this person is normal or not
	"""	
	age1 = 70
	heart_rate1 = 150
	test_answer1 = 1
	age2 = 70
	heart_rate2 = 70
	test_answer2 = 0
	assert test_answer1 == ta(age1, heart_rate1)
	assert test_answer2 == ta(age1, heart_rate2)
