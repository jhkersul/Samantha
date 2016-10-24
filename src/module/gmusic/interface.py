from src.module.main_interface import MainInterface
from src.module.gmusic.gmusic_controller import GMusicController
from src.controller.audio_controller import AudioController

class Interface(MainInterface):

	def __init__(self, manager):
		super(Interface, self).__init__(manager)

	def question(self, command, text):
		if command == "listen_music":
			song_name = self.inquire("Ok, qual música deseja ouvir?")
			gmusic = GMusicController()
			stream_url = gmusic.search_song(song_name)

			if stream_url is None:
				self.answer("Desculpe, não encontrei a música")
			else:
				AudioController().play_audio(stream_url)


	def commands(self):
		commands = {
			"listen_music": ["ouvir música"]
		}

		return commands