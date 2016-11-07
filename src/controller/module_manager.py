from src.controller.speak_controller import SpeakController
from src.controller.listen_controller import ListenController
from src.controller.session import Session

# IMPORTED MODULES
from src.module.introduction.interface import Interface as IntroductionInterface # INTRO MODULE
from src.module.facebook.interface import Interface as FacebookInterface # FACEBOOK MODULE
from src.module.gmusic.interface import Interface as GMusicInterface # GOOGLE MUSIC MODULE
from src.module.search.interface import Interface as SearchInterface # SEARCH MODULE


class ModuleManager(object):

    def __init__(self):
        self.__modules = []

        self.load_modules()
        #self.run_intro()

    # Loading all modules
    def load_modules(self):
        fb_interface = FacebookInterface(self)
        self.__modules.append(fb_interface)

        gmusic_interface = GMusicInterface(self)
        self.__modules.append(gmusic_interface)

        search_interface = SearchInterface(self)
        self.__modules.append(search_interface)

    def run_intro(self):
        intro_interface = IntroductionInterface(self)
        intro_interface.greetings()

    # Classifies a question and define the module
    def question_classifier(self, text):
        for module in self.__modules:
            for key, value in module.commands().items():
                for comm in value:
                    if text.lower().find(comm) != -1 :
                        return module, key, text


        return None, None, None

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

    # Saves a value on Session
    def save_value(self, key, value):
        Session.save(key, value)

    # Get a saved value on Session
    def get_saved_value(self, key):
        return Session.get(key)

    def keep_listening(self):
        while True:
            listen_text = ListenController.listen().lower()
            if  listen_text.find("olá samantha") != -1:
                SpeakController.speak("Olá! Em que posso ajudar?")

                module = None

                while module == None:
                    question = ListenController.listen()
                    module, command, text = self.question_classifier(question)

                    if question == "não":
                            break

                    if module == None:
                        SpeakController.speak("Não entendi! Repita, por favor.")
                    else:
                        module.question(command, text)
