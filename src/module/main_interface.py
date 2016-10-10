class MainInterface(object):
	def __init__(self):
		super(MainInterface, self).__init__()
		
	def load(self, manager):
		self.answer = manager.answer
		self.inquire = manager.inquire

		self.question("estou bem")

	def question(self, text):
		pass

	def commands(self):
		pass