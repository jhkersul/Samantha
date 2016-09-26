#!/usr/bin/env python3

from gtts import gTTS
from pydub import AudioSegment
import pyaudio  
import wave  

audio_file = "test.mp3"
tts = gTTS(text='Olá, tudo bem?', lang='pt-br')
tts.save(audio_file)

#define stream chunk   
chunk = 1024  

#open a wav format music  
f = wave.open(r"song.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#paly stream  
while data != '':  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  