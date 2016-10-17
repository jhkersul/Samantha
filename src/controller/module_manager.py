from src.controller.speak_controller import SpeakController
from src.controller.listen_controller import ListenController

# IMPORTED MODULES
from src.module.introduction.interface import Interface as IntroductionInterface # INTRO MODULE
from src.module.facebook.interface import Interface as FacebookInterface # FACEBOOK MODULE


class ModuleManager(object):

    def __init__(self):
        self.__modules = {}

        self.load_modules()
        self.run_intro()

    # Loading all modules
    def load_modules(self):
        intro_interface = IntroductionInterface(self)
        self.__modules['intro'] = intro_interface

        fb_interface = FacebookInterface(self)
        self.__modules['fb'] = fb_interface

    def run_intro(self):
        self.__modules['intro'].greetings()

    # Classifies a question and define the module
    def question_classifier(self, text):
        return None

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

    def keep_listening(self):
        while True:
            if ListenController.listen() == "Olá Samantha":
                SpeakController.speak("Olá! Em que posso ajudar?")

                module = None

                while module == None:
                    question = ListenController.listen()
                    module = self.question_classifier(question)

                    if question == "não":
                            break

                    if module == None: 
                        SpeakController.speak("Não entendi! Repita, por favor.")
    