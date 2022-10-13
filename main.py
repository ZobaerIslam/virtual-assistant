# Import essential module for this project
import speech_recognition as sr
import pyttsx3

# Creating a Recognizer instance

# Create objects for text to speech
try:
    recognizer = sr.Recognizer()
    ts_eng = pyttsx3.init()

except Exception as e:
    print(e)


# Default female voice and voice rate
en_female_voice_id = 'english_rp+f3'
voice_rate = 160

# Set Female voice
ts_eng.setProperty('voice', en_female_voice_id)   # changes voices. to female

# Set voice rate
ts_eng.setProperty('rate', voice_rate)    # changes voice rate.


# Text to speech
def talk(text):
    print(text)
    ts_eng.say(text)
    ts_eng.runAndWait()


welcome_speech = """Hi, I am Siri, 
I am your virtual assistant. 
How may i help you, Sir? """

talk(welcome_speech)


try:
    with sr.Microphone() as source:
        print('Listening...')
        voice = recognizer.listen(source)
        command = recognizer.recognize_google(voice)
        command = command.lower()

        talk(command)

except Exception as e:
    print(e)
