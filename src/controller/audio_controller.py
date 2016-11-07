import vlc
import time
from threading import Thread

class AudioController(object):

	def play_audio(self, path):
		p = vlc.MediaPlayer(path)
		events = p.event_manager()
		events.event_attach(vlc.EventType.MediaPlayerEndReached, self.songFinished)
		p.play()

		self.finish = 0

		self.answer = None

		while self.finish == 0:
			sec = p.get_time() / 1000
			m, s = divmod(sec, 60)
			print ("%02d:%02d" % (m,s))
			time.sleep(1)

	def songFinished(self, event):
		print ("Event reports - finished")
		self.finish = 1
