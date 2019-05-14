#coding:utf-8

from pydub import AudioSegment


sound = AudioSegment.from_mp3('./100001.mp3')

sound.export('now.wav',format ='wav')

