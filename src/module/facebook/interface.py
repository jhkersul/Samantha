from src.module.main_interface import MainInterface

class Interface(MainInterface):

	def __init__(self, manager):
		super(Interface, self).__init__(manager)

	def question(self, command, text):
		if text == "estou bem":
			ans = self.inquire("tem certeza que está bem?")

			if ans == "não":
				self.answer("Que triste mano brown")
			elif ans == "sim":
				self.answer("Então beleza manolo")


	def commands(self):
		return ["postar no facebook", 
				"ver notificações"]