import vlc
import time
from threading import Thread
from src.controller.non_blocking_console import NonBlockingConsole

class AudioController(object):

	def play_audio(self, path):
		p = vlc.MediaPlayer(path)
		events = p.event_manager()
		events.event_attach(vlc.EventType.MediaPlayerEndReached, self.songFinished)
		p.play()

		self.finish = 0

		self.answer = None

		# Console não bloqueante
		with NonBlockingConsole() as nbc:
			while self.finish == 0:
				sec = p.get_time() / 1000
				m, s = divmod(sec, 60)
				print ("%02d:%02d" % (m,s))
				time.sleep(1)

				# Caso o usuário aperta a tecla esc, o audio é interrompido
				if nbc.get_data() == '\x1b':  # x1b is ESC
					p.stop() # Parando o audio
					self.finish = 1 # Marcando como parado


	def songFinished(self, event):
		print ("Event reports - finished")
		self.finish = 1
