import pyttsx3

def getDefaultVoiceEngine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("volume", 1.)
    return engine

def getVoiceEngineInPortuguese():
    engine = getDefaultVoiceEngine()
    engine.setProperty("voice", "brazil")
    return engine

def speak(engine, message):
    engine.say(message)
    engine.runAndWait()