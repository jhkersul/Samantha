
class Session(object):
	
	keys = None

	@classmethod
	def save(cls, key, value):
		if cls.keys is None:
			cls.keys = {}

		cls.keys[key] = value

	@classmethod
	def get(cls, key):
		if key in cls.keys:
			return cls.keys[key]
		else:
			return None