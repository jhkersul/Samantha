#!/bin/bash

echo "==================="
echo "Installing packages"
echo "==================="

echo "Installing python3-pip..."
sudo apt install python3-pip

echo "Installing PyAudio..."
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev -y
sudo pip3 install PyAudio==0.2.9

echo "Installing SpeechRecognition..."
sudo pip3 install SpeechRecognition

echo "Installing gTTS..."
sudo pip install gTTS

echo "Installing ffmpeg..."
sudo apt-get install ffmpeg libavcodec-extra

echo "Installing pydub..."
sudo pip install pydub

echo "Installing Facebook API..."
sudo pip install facebook-sdk

echo "Installing GMusic libraries..."
sudo apt-get install libav-tools libavcodec-extra

echo "Install Google Music API..."
sudo pip install gmusicapi

echo "Installing VLC..."
sudo apt-get install vlc

echo "Install VLC Python..."
sudo pip install python-vlc