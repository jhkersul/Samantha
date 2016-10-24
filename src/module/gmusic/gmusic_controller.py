from src.module.gmusic.config import Config
from gmusicapi import Mobileclient
import vlc

class GMusicController(object):
	"""docstring for GMusicController"""
	def __init__(self):
		super(GMusicController, self).__init__()

		self.api = Mobileclient()
		self.api.login(Config.GMAIL, Config.PASSWORD, Config.MAC_ADDRESS)
		
	def search_song(self, text):
		result = self.api.search(text)

		try:
			song_id = result['song_hits'][0]['track']['storeId']
			stream_url = self.api.get_stream_url(song_id, device_id=Config.DEVICE_ID)

			return stream_url
		except Exception as e:
			return None

