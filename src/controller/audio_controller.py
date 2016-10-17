import pyaudio  
import wave
from pydub import AudioSegment

class AudioController(object):
	"""docstring for AudioController"""
	def __init__(self):
		super(AudioController, self).__init__()

	def convert_mp3_to_wav(self, file_path):
		song = AudioSegment.from_mp3(file_path)
		new_file_path = file_path[0:-3] + "wav"
		song.export(new_file_path, format="wav")

		return new_file_path

	def play_audio(self, file_path):
		#define stream chunk   
		chunk = 1024  

		#open a wav format music  
		f = wave.open(file_path,"rb")  
		#instantiate PyAudio  
		p = pyaudio.PyAudio()  
		#open stream  
		stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
		                channels = f.getnchannels(),  
		                rate = f.getframerate() + 3000,  
		                output = True)  
		#read data  
		data = f.readframes(chunk)  

		#paly stream  
		while data != b'':  
		    stream.write(data)  
		    data = f.readframes(chunk)

		#stop stream  
		stream.stop_stream()  
		stream.close()  

		#close PyAudio  
		p.terminate()
		