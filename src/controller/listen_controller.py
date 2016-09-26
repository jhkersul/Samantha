import speech_recognition as sr

class ListenController(object):
	
	# It listens to an audio and returns a text
	def listen():
		# Record Audio
		r = sr.Recognizer()
		with sr.Microphone() as source:
		    print("Say something!")
		    audio = r.listen(source)
		 
		# Speech recognition using Google Speech Recognition
		try:
		    # for testing purposes, we're just using the default API key
		    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		    # instead of `r.recognize_google(audio)`
		    text = r.recognize_google(audio, language="pt-BR")
		    print("You said: " + text)
		    return text

		except sr.UnknownValueError:
   			print("Google Speech Recognition could not understand audio")
   			return ""
		except sr.RequestError as e:
		    print("Could not request results from Google Speech Recognition service; {0}".format(e))
		    return ""
