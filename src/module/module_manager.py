from src.module.facebook.interface import Interface as FacebookInterface
from src.controller.speak_controller import SpeakController
from src.controller.listen_controller import ListenController

class ModuleManager(object):
    _instance = None

    def __init__(self):
        self.__modules = {}

        self.load_modules()

    # Loading all modules
    def load_modules(self):
        fb_interface = FacebookInterface()
        fb_interface.load(self)
        self.__modules['fb'] = fb_interface

    # Classifies a question and define the module
    def question_classifier(self, text):
        pass

    # I ask a question to module
    def question(self, text, module):
        module.question(text)

    # Module answer a question to me
    def answer(self, text):
        SpeakController.speak(text)

    # Module ask a question to me
    def inquire(self, text):
        SpeakController.speak(text)
        return ListenController.listen()