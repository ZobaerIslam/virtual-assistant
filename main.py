# Import essential module for this project
import speech_recognition as sr

# Creating a Recognizer instance
r = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = r.listen(source)
        command = r.recognize_google(voice)
        print(command)

except:
    pass
