import speech_recognition as sr
import voice_synthesizer as vs

def listen_user(engine):
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        print("Aguardando resposta...")
        audio = mic.listen(source, timeout=4000)
        try:
            query = mic.recognize_google(audio, language='pt-BR')
            return query
        except:
            vs.speak(engine, "Não entendi o que você disse, repita por favor.")
            return listen_user(engine)


