import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)
    try:
        print("You said: " + recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
