from gtts import gTTS
from src.controller.audio_controller import AudioController

class SpeakController(object):
	FILE_FOLDER = "/tmp/"

	def speak(text):
		audio_file = SpeakController.FILE_FOLDER + "test.mp3"
		tts = gTTS(text=text, lang='pt-br')
		tts.save(audio_file)

		AudioController().play_audio(audio_file)