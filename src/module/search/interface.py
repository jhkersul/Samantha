from src.module.main_interface import MainInterface
from src.module.search.search_google import SearchGoogle
from src.module.search.search_wiki import SearchWiki

class Interface(MainInterface):

    def __init__(self, manager):
        super(Interface, self).__init__(manager)

    def question(self, command, text):
        if command == "define_something":
            self.answer("Ok, aguarde um instante.")

            wiki_title = SearchGoogle.get_wikipedia_title(text)
            summary = SearchWiki.get_summary(wiki_title)

            self.answer(summary)


    def commands(self):
        commands = {
            "define_something": ["defina", "quem é", "o que é", "quem são", "me fale sobre"]
        }

        return commands
