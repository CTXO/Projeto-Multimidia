import webbrowser
from url_finder import find_first_video_id
import voice_synthesizer as vs
from listen_user import listen_user

engine = vs.getVoiceEngineInPortuguese()

vs.speak(engine, "Diga-me que música você deseja pesquisar.")
query = listen_user(engine)
print("Procurando por:", query)

video_id = find_first_video_id(query)
webbrowser.open(f'https://youtube.com/watch?v={video_id}')


