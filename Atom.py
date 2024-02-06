import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    Id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', Id)
    print("")
    print(f"==> EVA AI :{text}")
    engine.say(text=text)
    engine.runAndWait()


# speak("Hello I am EVA. How can I help you ")


def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")
        print("")
        print(f"==> Jaswant :{query}")
        return query.lower()

    except:
        return ""


def MainExecution(query):
    Query = str(query).lower()

    if "hello" in Query:
        speak("Hello I am EVA, How can I help you!")

    elif "bye" in Query:
        speak("Nice to meet you sir, Have a Nice Day!")
        exit


while True:
    print("")
    Query = speechrecognition()
    MainExecution(Query)
