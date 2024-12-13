import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  

# Initialize recognizer and pyttsx3 engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)  # Use `.get()` to avoid KeyError
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song in the library.")
    
if __name__ == "__main__":
    speak("Initializing jarvis....")

    while True:
        # Listen for the wake word "hi"
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
                print("Say 'hey jarvis' to activate Jarvis")
                audio = recognizer.listen(source)
                word = recognizer.recognize_google(audio)
                print(f"Recognized word: {word}")

                if word.lower() == "hey jarvis":
                    speak("yaaaa")
                    # Now listen for the command after the wake word
                    with sr.Microphone() as source:
                        print("Jarvis is active... Please give a command.")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        print(f"Command recognized: {command}")
                        processCommand(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {str(e)}")
