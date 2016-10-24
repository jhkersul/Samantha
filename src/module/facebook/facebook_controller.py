from src.module.facebook.config import Config
import facebook

class FacebookController(object):
	def __init__(self):
		super(FacebookController, self).__init__()

		self.graph = facebook.GraphAPI(access_token=Config.FACEBOOK_TOKEN, version='2.7')

	def post(self, text):
		self.graph.put_object(parent_object='me', connection_name='feed', message=text)