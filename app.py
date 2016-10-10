from src.controller.speak_controller import SpeakController
from src.controller.listen_controller import ListenController
from src.module.module_manager import ModuleManager

i = 0
while i<2:
	#text = ListenController.listen()
	#speak_controller.speak(text)

	module_manager = ModuleManager()

	i += 1