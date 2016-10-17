class MainInterface(object):
	def __init__(self, manager):
		super(MainInterface, self).__init__()

		self.answer = manager.answer
		self.inquire = manager.inquire
		self.save_value = manager.save_value
		self.get_saved_value = manager.get_saved_value

	def question(self, command, text):
		pass

	def commands(self):
		pass
