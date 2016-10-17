from src.module.main_interface import MainInterface

class Interface(MainInterface):

	def __init__(self, manager):
		super(Interface, self).__init__(manager)

	def greetings(self):
		self.answer("Olá, estou aqui!")
		self.answer("Meu nome é Samantha! Eu sou a sua assistente pessoal.")

		confirmation = None

		while confirmation != "sim":
			name =  self.inquire("Qual é o seu nome?")
			confirmation = self.inquire("Seu nome é " + name + ", correto?")

		self.answer("Ok " + name + "! Vamos começar!")

		self.save_value("user_name", name)
