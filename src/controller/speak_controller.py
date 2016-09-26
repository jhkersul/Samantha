from gtts import gTTS
from src.controller.audio_controller import AudioController

class SpeakController(object):
	FILE_FOLDER = "/tmp/"

	"""docstring for SpeakController"""
	def __init__(self):
		super(SpeakController).__init__()


	def speak(self, text):
		audio_file = SpeakController.FILE_FOLDER + "test.mp3"
		tts = gTTS(text=text, lang='pt-br')
		tts.save(audio_file)

		audio_controller = AudioController()

		new_file_path = audio_controller.convert_mp3_to_wav(audio_file)
		audio_controller.play_audio(new_file_path)