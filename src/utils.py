import string
import random

def code_generator(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
	"""Generate a random string of lenght 'size' and with chars 'chars'"""
	return string.join(random.choice(chars) for x in range(size))
