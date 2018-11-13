import speech_recognition as sr

AUDIO_FILE=('example.wav')

#use audio file as audio source

r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
	#listen
	audio=r.record(source)

try:
	print('u said:' + r.recognize_google(audio))
except sr.UnknownValueError:
	print('Google Speech Recognition didnt understand')

except sr.RequestError as e:
	print('Could not request result from Google service;{0}'.forma)
