import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Sorry, I couldn't understand. Please try again.")
        return None

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Main function to interact with the user
def main():
    greet()
    speak("Hello,How can I assist you today?")
    while True:
        query = listen()
        if query:
            if "hello" in query:
                speak("Hello! How can I help you?")
            elif "time" in query:
                tell_time()
            elif "search" in query:
                speak("What would you like me to search?")
                search_query = listen()
                if search_query:
                    search_web(search_query)
            elif "exit" in query or "thank you" in query:
                speak("You are Welcome!!")
                break

if __name__== "__main__":
 main()

