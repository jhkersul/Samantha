#!/bin/bash

echo "==================="
echo "Installing packages"
echo "==================="

echo "Installing PyAudio..."
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev -y
pip install PyAudio==0.2.9

echo "Installing SpeechRecognition..."
pip install SpeechRecognition

echo "Installing gTTS..."
pip install gTTS

echo "Installing ffmpeg..."
sudo apt-get install -y ffmpeg libavcodec-extra

echo "Installing pydub..."
pip install pydub

echo "Installing Facebook API..."
pip install facebook-sdk

echo "Installing GMusic libraries..."
sudo apt-get install -y libav-tools libavcodec-extra

echo "Install Google Music API..."
pip install gmusicapi

echo "Installing VLC..."
sudo apt-get install -y vlc

echo "Install VLC Python..."
pip install python-vlc

echo "Installing Wikipedia"
pip install wikipedia

echo "Installing "
pip install simplejson requests
