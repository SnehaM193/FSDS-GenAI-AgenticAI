
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pk

listening = sr.Recognizer()
engine = pt.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    cmd = ""

    try:
        with sr.Microphone() as mic:
            print("Listening...")

            listening.adjust_for_ambient_noise(mic, duration=1)

            voice = listening.listen(mic, timeout=5, phrase_time_limit=8)

            cmd = listening.recognize_google(voice)
            cmd = cmd.lower()

            print("You said:", cmd)

            if "sneha" in cmd:
                cmd = cmd.replace("sneha", "").strip()

    except sr.WaitTimeoutError:
        print("No speech detected.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")

    except sr.RequestError:
        print("Google Speech Recognition service is unavailable.")

    except Exception as e:
        print("Error:", e)

    return cmd


def run():
    cmd = hear()

    if "play" in cmd:
        song = cmd.replace("play", "").strip()

        if song:
            speak("Playing " + song)
            pk.playonyt(song)

        else:
            speak("Please tell me the song name.")

    else:
        speak("Sorry, I don't understand that command.")


run()
