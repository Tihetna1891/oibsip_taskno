import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def greet():
    return "Hello! How can I help you today?"

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}"

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today is {current_date}"

def search_web(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    return f"Searching the web for {query}"

def voice_assistant(command):
    if "hello" in command.lower():
        return greet()
    elif "time" in command.lower():
        return get_time()
    elif "date" in command.lower():
        return get_date()
    elif "search" in command.lower():
        query = command.split("search")[1].strip()
        return search_web(query)
    else:
        return "I'm sorry, I didn't understand that."

def main():
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)

        response = voice_assistant(command)
        print("Assistant:", response)

        engine.say(response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError as e:
        print(f"Error making the request: {e}")

if __name__ == "__main__":
    main()
