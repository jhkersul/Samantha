from src.controller.speak_controller import SpeakController
from src.controller.listen_controller import ListenController

speak_controller = SpeakController()
while (1==1):
	text = ListenController.listen()
	speak_controller.speak(text)