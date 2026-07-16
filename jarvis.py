+ import pyttsx3
+ import speech_recognition as sr
+ import datetime
+ import wikipedia
+ import webbrowser
+ import os

# -------------------- INITIALIZATION --------------------
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

# -------------------- SPEAK FUNCTION --------------------
def speak(text):
    engine.say(text)
    engine.runAndWait()

# -------------------- WISH USER --------------------
def wish_me():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may I help you.")

# -------------------- TAKE COMMAND --------------------
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable.")
        return ""

    except Exception as e:
        speak("An error occurred.")
        return ""

# -------------------- COMMAND HANDLER --------------------
def execute_command(query):

    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        try:
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(result)
        except Exception:
            speak("Unable to fetch Wikipedia results.")

    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")

    elif "open google" in query:
        webbrowser.open("https://www.google.com")

    elif "play music" in query:
        music_path = "C:\\Users\\hp\\Music\\manu.mp3"
        if os.path.exists(music_path):
            os.startfile(music_path)
        else:
            speak("Music file not found.")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {current_time}")

    elif "open code" in query:
        code_path = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        if os.path.exists(code_path):
            os.startfile(code_path)
        else:
            speak("VS Code not found.")

    elif "exit" in query or "quit" in query or "stop" in query:
        speak("Goodbye sir. Have a nice day.")
        exit()

    else:
        speak("Sorry, command not recognized. Please try again.")

# -------------------- MAIN DRIVER --------------------
if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if query:
            execute_command(query)
