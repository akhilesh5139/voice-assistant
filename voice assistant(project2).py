import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


def chatbot(query):
    # Add your chatbot logic here
    if "hello" in query:
        return "Hi there! How can I assist you today?"
    elif "goodbye" in query or "bye" in query:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I'm not sure how to help with that."


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you?")

    while True:
        query = listen().lower()

        if query:
            response = chatbot(query)
            speak(response)

        if "goodbye" in query or "bye" in query:
            break
