import webbrowser
from url_finder import find_first_result
import voice_synthesizer as vs
from listen_user import listen_user

engine = vs.getVoiceEngineInPortuguese()

vs.speak(engine, "Diga-me que música você deseja pesquisar.")
query = listen_user(engine)
print("Procurando por:", query)

video_url = find_first_result(query)
webbrowser.open(f'https://youtube.com/{video_url}')


