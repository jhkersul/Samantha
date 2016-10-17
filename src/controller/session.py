from src.model.user import User

class Session(object):
	user = None

	@classmethod
	def create_user(cls, name):
		cls.user = User(name)		

	@classmethod
	def get_current_user(cls):
		return cls.user