from src.module.main_interface import MainInterface

class Interface(MainInterface):

	def __init__(self, manager):
		super(Interface, self).__init__(manager)

	def question(self, command, text):
		if command == "define_something":
            pass


	def commands(self):
		commands = {
			"define_something": ["defina", "quem é", "o que é"]
		}

		return commands
