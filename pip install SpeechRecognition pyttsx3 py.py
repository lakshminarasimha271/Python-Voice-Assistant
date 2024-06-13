pip install SpeechRecognition pyttsx3 pyaudio wikipedia requests
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import requests

# Function to convert text to speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en')
        print(f"You: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't get that. Could you please repeat?")
        return recognize_speech()
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the internet.")
        return None

# Function to perform actions based on user input
def perform_action(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif 'thank you' in query:
        speak("You're welcome!")
    elif 'exit' in query:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I'm not sure how to help with that.")

# Main function for running the voice assistant
def main():
    speak("Hello! How can I assist you?")
    while True:
        query = recognize_speech()
        if query:
            perform_action(query)

if __name__ == "__main__":
    main()
