import serial
import time
import pyttsx3
import speech_recognition as sr 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing... wait a minute")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please... icannot recognizing")  
        query = "none"
    return query



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",140)
engine.setProperty("volume",1000)


if __name__ == "__main__":
    ard = serial.Serial('com10' ,9600)
    time.sleep(2)
  
    var = 'pt'
    query=takeCommand().lower()
    if 'tell me temperature' in query:
        var ='a'
        c=var.encode()
        speak("yeah..")

    if var == 'a':
        ard.write(c)
        time.sleep(1)
        iny =(ard.readline())
        iny=iny.decode()
        iny=str(iny)
        print(iny)
        speak(str(iny)+"degree centigrade is the temperature!!")

    if var == 'b':
        ard.write(c)