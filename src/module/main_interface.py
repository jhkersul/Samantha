class MainInterface(object):
	def __init__(self, manager):
		super(MainInterface, self).__init__()

		self.answer = manager.answer
		self.inquire = manager.inquire

	def question(self, command, text):
		pass

	def commands(self):
		pass