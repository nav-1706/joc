import speech_recognition as sr

AUDIO_FILE = ("./WEEK5/speech1.wav") # use audio file as source

r = sr.Recognizer(); # initialise the recognizer
with sr.AudioFile(AUDIO_FILE) as source: # read the entire audio file
    audio = r.record(source)
    
try:
    print("Transcription: " + r.recognize_google(audio)) # use google's speech
    
except sr.UnknownValueError: # exception is type of error
    print("Speech recoginitation can't understand the speech")
    
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service")