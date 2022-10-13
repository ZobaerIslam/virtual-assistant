# Import essential module for this project
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


# Set female voice and voice rate
en_female_voice_id = 'english_rp+f3'
voice_rate = 160

# Create instances for text to speech
try:
    recognizer = sr.Recognizer()
    ts_eng = pyttsx3.init()

    # Set Female voice
    ts_eng.setProperty('voice', en_female_voice_id)  # changes voices. to female
    # Set voice rate
    ts_eng.setProperty('rate', voice_rate)  # changes voice rate.

except Exception as e:
    print("Exception: " + str(e))


# Text to speech
def talk(text):
    print(text)
    ts_eng.say(text)
    ts_eng.runAndWait()


# Set Virtual assistant name
bot_name = 'eliza'

welcome_speech = f"Hi, I am {bot_name}, I am your virtual assistant. How may i help you, Sir? "
talk(welcome_speech)


# Take command from speech
def take_command():
    with sr.Microphone() as source:
        print('Listening...')
        voice = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(voice)

        except Exception as ex:
            print('Exception: ' + str(ex))
            print('Say something...')

    return command


# Perform commands
def run_eliza():
    command = take_command().lower()
    if 'eliza' in command:
        command = command.replace('eliza', '')
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is: ' + str(time))
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'play' in command:
        song = command.replace('play', 'playing')
        talk(song)
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())


while True:
    run_eliza()
