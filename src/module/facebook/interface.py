from src.module.main_interface import MainInterface
from src.module.facebook.facebook_controller import FacebookController

class Interface(MainInterface):

	def __init__(self, manager):
		super(Interface, self).__init__(manager)

	def question(self, command, text):
		if command == "post":
			message = self.inquire("Ok, pode dizer sua mensagem!")
			FacebookController().post(message)
			self.answer("Sua mensagem foi postada com sucesso")



	def commands(self):
		commands = {
			"post": ["postar no facebook", "postar no face"]
		}

		return commands