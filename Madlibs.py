import pyttsx3
import random
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    newVoiceRate = 200
    engine.setProperty('rate',newVoiceRate)

if __name__ == "__main__":
    mad = random.randint(1,3)
    if mad == 1:
        os.system('poem.py')
        myfile = open('output.txt', 'rt')
        contents = myfile.read()
        myfile.close()
        print(contents)
        speak(contents)
    elif mad == 2:
        os.system('text.py')
        myfile = open('output.txt', 'rt')
        contents = myfile.read()
        myfile.close()
        print(contents)
        speak(contents)
    else:
        os.system('text2.py')
        myfile = open('output.txt', 'rt')
        contents = myfile.read()
        myfile.close()
        print(contents)
        speak(contents)